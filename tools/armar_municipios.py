"""Arma data/municipios.json a partir del relevamiento de IDECOR y los datos curados.

Uso:  python3 tools/armar_municipios.py
Entradas: tools/idecor_relevamiento.json (capas y documentos por ciudad, relevado desde el navegador)
          tools/municipios_curado.py (ordenanzas con enlace oficial, avisos, alias)
"""
import json, os, sys, datetime

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
from municipios_curado import CURADO, SALTA_CAPAS, OBS  # noqa: E402

rel = json.load(open(os.path.join(AQUI, 'idecor_relevamiento.json'), encoding='utf-8'))

# Mapas de Mapas Córdoba que no salen de las carpetas de documentos (número tomado del portal de Ciudades)
MAPAS = {
    'Arroyito': [506], 'Del Campillo': [650], 'La Calera': [450], 'La Granja': [451], 'Nono': [453],
    'Río Cuarto': [542], 'San Francisco': [452], 'Villa Allende': [493], 'Villa María': [328], 'Villa Carlos Paz': [309],
    'Capilla del Monte': [559], 'Cosquín': [], 'Mina Clavero': [],
}
IDECOR_WMS = 'https://idecor-ws.mapascordoba.gob.ar/geoserver/idecor/wms'
SALTA_MUNI = 'https://geocloud.municipalidadsalta.gob.ar/geoserver/'

ciudades = []
nombres = set(rel) | set(CURADO)
for nombre in sorted(nombres):
    r = rel.get(nombre, {'c': [], 'd': {}})
    cu = CURADO.get(nombre, {})
    docs = {}
    for carpeta, files in r['d'].items():
        for f in files:
            docs.setdefault(f, carpeta + '/' + f)
    capas = [{'l': 'idecor:' + l, 't': t, 'g': g, 'z': bool(z)} for l, t, g, z in r['c']]
    prov = cu.get('prov', 'cordoba')
    if nombre == 'Salta capital':
        capas = [dict(c, base=SALTA_MUNI + 'wfs', wms=SALTA_MUNI + 'wms', z=False) for c in SALTA_CAPAS]
    ords = []
    for o in cu.get('ord', []):
        o = dict(o)
        f = o.pop('doc', None)
        if f:
            if f in docs:
                o['u'] = OBS + docs[f]
                o['f'] = 'IDECOR'
            else:
                o['nota'] = 'el plano lo cita pero el PDF no está publicado'
        ords.append(o)
    mapas = list(cu.get('mapas', []))
    nums = sorted({int(p.split('/')[0][1:]) for p in docs.values()} | set(MAPAS.get(nombre, [])))
    for n in nums:
        mapas.append({'t': 'Mapas Córdoba · mapa ' + str(n), 'u': 'https://mapascordoba.gob.ar/viewer/mapa/' + str(n)})
    if cu.get('pagina'):
        mapas.append({'t': 'Página oficial de normativa', 'u': cu['pagina']})
    c = {'nombre': nombre, 'prov': prov, 'capas': capas, 'docs': docs, 'ordenanzas': ords, 'mapas': mapas}
    if cu.get('alias'):
        c['alias'] = cu['alias']
    if cu.get('aviso'):
        c['aviso'] = cu['aviso']
    c['fuente'] = cu.get('fuente', 'IDECOR Ciudades' if capas else 'Sitio oficial del municipio')
    ciudades.append(c)

out = {
    'generado': datetime.date.today().isoformat(),
    'docBase': OBS,
    'fuentes': [
        'IDECOR: capas WFS de IDECOR Ciudades y documentos del repositorio obs-idecor-mapas-docs',
        'IDEMSa: geoservicios de la Municipalidad de Salta',
        'Sitios oficiales de municipios y concejos deliberantes; Colegio de Arquitectos de Salta',
    ],
    'ciudades': ciudades,
}
dest = os.path.join(AQUI, '..', 'data', 'municipios.json')
json.dump(out, open(dest, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
print(len(ciudades), 'ciudades ·', sum(len(c['capas']) for c in ciudades), 'capas ·',
      sum(len(c['docs']) for c in ciudades), 'documentos ·', sum(len(c['ordenanzas']) for c in ciudades), 'ordenanzas')
sin = [o['n'] + ' (' + c['nombre'] + ')' for c in ciudades for o in c['ordenanzas'] if o.get('nota')]
if sin:
    print('Sin PDF publicado:', '; '.join(sin))
