# Datos curados a mano para data/municipios.json: ordenanzas con enlace oficial, avisos y alias.
# Las capas y los documentos de IDECOR salen de tools/idecor_relevamiento.json (generado desde el navegador).
# Cada enlace se verificó al armar el catálogo (octubre 2026). "f" es la fuente que se muestra en el enlace.

OBS = 'https://obs-idecor-mapas-docs.obs.sa-argentina-1.myhuaweicloud.com/'

def d(file):
    """Ordenanza cuyo texto está en el repositorio de IDECOR (se resuelve con el relevamiento)."""
    return {'doc': file}

CURADO = {
    # ───────────────────────── Córdoba ─────────────────────────
    'Alta Gracia': {
        'ord': [
            {'n': 'Ord. 8547', 't': 'Plan de Ordenamiento Urbano y Territorial (zonificación, Anexo III)', 'u': 'https://drive.google.com/drive/folders/1GUhLVi1WU8eVCiZbE1xV1c9cMsBzE5yW', 'f': 'Municipalidad'},
            {'n': 'Ord. 8548', 't': 'Código de Edificación', 'u': 'https://drive.google.com/drive/folders/1QyhFrhbY-T9P1xFBxA3omSdMuR19mudw', 'f': 'Municipalidad'},
            {'n': 'Fichas por zona', 't': 'PDF de cada zona normativa', 'u': 'https://drive.google.com/drive/folders/1Agj9a6tL-RwLIETpte-L5HiT4OJtpI35', 'f': 'Municipalidad'},
        ],
        'aviso': 'La capa provincial de IDECOR cita la "Ordenanza 8457"; la municipalidad publica su plan como Ord. 8547 y el código de edificación como Ord. 8548. Verificar el número antes de citarlo.',
        'pagina': 'https://altagracia.gob.ar/subareas/normativa-vigente/',
    },
    'Anisacate': {
        'ord': [{'n': 'Ord. 563/24', 't': 'Plan de Ordenamiento Territorial', **d('ord_563_24_plan_ord_territorial.pdf')}],
        'aviso': 'La capa provincial cita la Ord. 825/2015, pero el plano municipal enlaza el Plan de Ordenamiento Territorial Ord. 563/24, que es más reciente.',
    },
    'Arroyito': {
        'ord': [
            {'n': 'Ord. 1081/03', 't': 'Zonificación y ejes comerciales'},
            {'n': 'Ord. 1212/06, 1725/16 y 1765/17', 't': 'Modificatorias de ejes comerciales (según la capa municipal)'},
        ],
    },
    'Bell Ville': {
        'ord': [
            {'n': 'Ord. 1866/14', 't': 'Código de Edificación y Urbanismo y modificatorias', **d('ord_1866_14cod_edif_y_urb_y_modificatorias.pdf')},
            {'n': 'Ord. 2680/2024', 't': 'Modifica la Ord. 1866/14 (promulgada por Dec. 10296/2024)', 'u': 'http://www.concejobellville.gob.ar/noticia/ordenanzas-y-resoluciones-aprobadas-en-la-sesion-ordinaria-del-dia-15-08-2024/', 'f': 'Concejo Deliberante'},
        ],
        'aviso': 'La Ord. 2680/2024 modificó el código en 2024: confirmar que el plano de IDECOR ya la incorpora.',
    },
    'Capilla del Monte': {'ord': [{'n': 'Ord. 2972/19', 't': 'Zonificación y usos del suelo', **d('ord_2972_19_usos_suelo.pdf')}, {'n': 'Anexo gráfico', 't': 'Plano de la Ord. 2972/19', **d('ord_2972_19_anexo_grafico.pdf')}]},
    'Colonia Caroya': {
        'ord': [
            {'n': 'Ord. 2361/20', 't': 'Plan de ordenamiento: áreas, subáreas y corredores', **d('CCaroya_ord_2361.pdf')},
            {'n': 'Ord. 1788/13', 't': 'Subáreas', **d('CCaroya_ord_1788.pdf')},
            {'n': 'Ord. 2408, 2414/21, 2487/22, 2516, 2641/24 y 2717', 't': 'Modificatorias por subárea (ver cada polígono)'},
        ],
    },
    'Cosquín': {'ord': [{'n': 'Ord. 72', 't': 'Código de Edificación y zonificación'}]},
    'Del Campillo': {'ord': [{'n': 'Ord. 032/2009', 't': 'Plan de Ordenamiento Urbano', **d('ord_032_2009_plan_de_orden_urb.pdf')}, {'n': 'Ord. 024/2009', 't': 'Código de Edificación', **d('ord_024_2009_codigo_edific.pdf')}]},
    'Elena': {'ord': [{'n': 'Ord. 655/24', 't': 'Zonificación', **d('655_24_zonificacion.pdf')}, {'n': 'Ord. 656/24', 't': 'Código de Edificación', **d('656_24_codigo_de_edificacion.pdf')}]},
    'Hernando': {'ord': [{'n': 'Ord. 55/18', 't': 'Código de Urbanismo y Edificación (uso del suelo y patrones)'}]},
    'Villa Río Icho Cruz': {'alias': ['Icho Cruz'], 'ord': [{'n': 'Ord. 214/2023', 't': 'Código de Edificación', **d('codigo_edificacion_ord_214_2023.pdf')}, {'n': 'Ord. 216/2023', 't': 'Código de Urbanismo y Fraccionamiento', **d('codigo_urbanismo_y_fraccion_ord_216_2023.pdf')}]},
    'Jesús María': {'ord': [{'n': 'Ord. 4196', 't': 'Código Urbano (patrones de asentamiento)', 'u': 'https://www.jesusmaria.gov.ar/frontend/pdf/JM-ORDENANZA-NRO-4196-CODIGO-URBANO.pdf', 'f': 'Municipalidad'}]},
    'Justiniano Posse': {'ord': [{'n': 'Ord. 38/07 y 27/23', 't': 'Código de Edificación y Plan de Ordenamiento Urbano', **d('ord_2723_3807_codigo_de_edificacion_JP.pdf')}, {'n': 'Plan de Ordenamiento Urbano', 't': 'Texto del plan (Ord. 27/23)', **d('plan_ordenamiento_urbano_JP.pdf')}]},
    'La Calera': {'ord': [{'n': 'Ord. 058/19', 't': 'Zonificación y usos del suelo'}]},
    'La Falda': {
        'ord': [{'n': 'Ord. 3791', 't': 'Código de Edificación y Urbanización, Texto Ordenado 2025', 'u': 'https://www.lafalda.gob.ar/?q=content/codigo-edificacion-y-urbanizacion-texto-ordenado-2025-ord-no-3791', 'f': 'Municipalidad'}],
        'aviso': 'La capa provincial y el plano de IDECOR citan la Ord. 3329; el texto vigente que publica la municipalidad es el Texto Ordenado 2025 (Ord. 3791). Verificar los valores contra ese texto.',
    },
    'La Granja': {'ord': [{'n': 'Ord. 516/18', 't': 'Código de Ordenamiento Urbano y Edificación'}]},
    'Laguna Larga': {'ord': [{'n': 'Ord. 1573/20', 't': 'Código de Edificación', **d('ord_1573.pdf')}]},
    'Las Higueras': {'ord': [{'n': 'Ord. 16/2015', 't': 'Código de Planificación Urbana', **d('Codigo_Planeamiento_Ord_16_2015.pdf')}, {'n': 'Artículos modificados', 't': 'Modificaciones al código vigente', **d('Art_Modificados_al_código_vigente.pdf')}]},
    'Las Varillas': {'ord': [{'n': 'Ord. 480/22', 't': 'Código de Planificación Urbana', **d('resumen.pdf')}, {'n': 'Disposiciones complementarias', 't': 'Ord. 480/22', **d('disp_comp.pdf')}]},
    'Mayu Sumaj': {'ord': [{'n': 'Res. 1499/18', 't': 'Código de Edificación', **d('codigo_de_edificacion_res_1499.pdf')}, {'n': 'Plan de Ordenamiento Urbano', 't': '', **d('plan_de_ordenamiento_urbano.pdf')}]},
    'Mina Clavero': {'ord': [{'n': 'Ord. 819/04', 't': 'Zonificación, sistema viario e inhibición de caminos'}], 'aviso': 'Las fichas por zona que cita el plano de Mina Clavero no están publicadas en el repositorio de IDECOR.'},
    'Monte Buey': {'ord': [{'n': 'Ord. 24/24', 't': 'Usos del suelo y zonificación', **d('Ordenanza_Municipal_24_24.pdf')}]},
    'Morteros': {'ord': [{'n': 'Ord. 1529', 't': 'Plan de Ordenamiento Urbano', **d('ord_1529_plan_ord_urb.pdf')}]},
    'Nono': {'ord': [{'n': 'Ord. 993/18', 't': 'Código Urbano y de Edificación'}]},
    'Oncativo': {'ord': [{'n': 'Ord. 333/87', 't': 'Plan de Ordenamiento Urbano (fichas por zona en el plano)'}, {'n': 'Ord. 1993/11', 't': 'Plan regulador del uso del suelo urbano'}]},
    'Porteña': {'ord': [
        {'n': 'Ord. 1462/08', 't': 'Plan de Ordenamiento Urbano (extracto)', **d('ord_1462_08_extracto_pou.pdf')},
        {'n': 'Ord. 1831/16', 't': 'Modificatoria', **d('ord_1831_16.pdf')}, {'n': 'Ord. 2072/20', 't': 'Modificatoria', **d('ord_2072_20.pdf')},
        {'n': 'Ord. 2102/21', 't': 'Modificatoria', **d('ord_2102_21.pdf')}, {'n': 'Ord. 2171/22', 't': 'Modificatoria', **d('ord_2171_22.pdf')}]},
    'Río Ceballos': {'ord': [{'n': 'Ord. 2651/19', 't': 'Uso y ocupación del suelo (parámetros por pendiente)', **d('Ord-2651-19_ANEXO-GRAFICO-2_Tabla-General-Usos.pdf')}, {'n': 'Ord. 2094/14', 't': 'Reserva Hídrica Los Manantiales', **d('ord_2094_14_rvalosmanantiales.pdf')}]},
    'Río Cuarto': {'ord': [{'n': 'Ord. 1082/11', 't': 'Plan Urbano: usos, fraccionamiento y ocupación del suelo', 'u': 'https://concejo.riocuarto.gov.ar/?seccion=buscador&command=display&subcommand=ord&id=2011010820', 'f': 'Concejo Deliberante'}, {'n': 'Reglamentaciones', 't': 'Decretos y modificatorias de la Ord. 1082/11', 'u': 'https://concejo.riocuarto.gov.ar/index.php?seccion=buscador&command=digesto&action=chapter&section=20203', 'f': 'Digesto'}]},
    'Salsipuedes': {'ord': [{'n': 'Ord. 942/08', 't': 'Zonificación y usos del suelo'}, {'n': 'Ord. 1404/2019 y 1625/2024', 't': 'Reserva Hídrica y Natural Municipal'}]},
    'San Antonio de Arredondo': {'ord': [{'n': 'Res. 19/08', 't': 'Código de Zonificación y Edificación', **d('zonificacion_cod_edif.pdf')}, {'n': 'Resumen por zona', 't': '', **d('resumen_norma_xzona.pdf')}]},
    'San Basilio': {'ord': [{'n': 'Ord. 060/2012', 't': 'Planeamiento urbano'}]},
    'San Francisco': {'ord': [{'n': 'Ord. 7588', 't': 'Índices de FOS, IEP y uso del suelo', 'u': 'https://munilocal.sanfrancisco.gov.ar/digesto/archivos_ordenanzas/pdf/7588.pdf', 'f': 'Digesto'}, {'n': 'Ord. 3252', 't': 'Edificación (citada por la zonificación)'}], 'aviso': 'La municipalidad anunció la elaboración de un nuevo Código Urbanístico.'},
    'San Isidro - La Quintana': {'alias': ['Villa San Isidro'], 'ord': [{'n': 'Res. 05/2025', 't': 'Zonas y usos', **d('resol_05_2025.pdf')}, {'n': 'Res. 14/2025', 't': 'Modificatoria', **d('resol_14_2025.pdf')}]},
    'Santa Rosa de Calamuchita': {'ord': [{'n': 'Ord. 261/1984', 't': 'Código de Edificación', **d('261_1984_codigo_edificacion.pdf')}, {'n': 'Ord. 524/92', 't': 'Corredor Ruta 5', **d('1_ord_524_92_RUTA5.pdf')}, {'n': 'Ord. 1858/22', 't': 'Loteos y urbanizaciones', **d('16_ord_1858_22_loteos_y_urb.pdf')}, {'n': 'Otras', 't': 'Ordenanzas por loteo y barrio (ver cada polígono)'}]},
    'Sinsacate': {'ord': [{'n': 'Ord. 1206/2022', 't': 'Código Urbanístico Ambiental', **d('sinsacate_ord_1206_2022.pdf')}, {'n': 'Ord. 1207/2022', 't': 'Zonas', **d('sinsacate_codigo_urbanistico_ambiental.pdf')}]},
    'Unquillo': {'ord': [
        {'n': 'Ord. 825/2014', 't': 'Ordenamiento: áreas, subáreas y zonas', **d('ord_825_2014.pdf')},
        {'n': 'Ord. 34/86', 't': 'Código de Edificación', **d('ord_34_86_codedif.pdf')},
        {'n': 'Ord. 1208/2019 y 1359/2021', 't': 'Zonas ZR7 y ZR8', **d('ord_1208_2019.pdf')},
        {'n': 'Ord. 1472/2023', 't': 'Retiros sobre la red vial', **d('ord_1472_2023.pdf')}]},
    'Vicuña Mackenna': {'alias': ['Vicuña Mackena'], 'ord': [{'n': 'Ord. 1067/2015', 't': 'Código de Urbanización', **d('codigo_urbanizacion.pdf')}]},
    'Villa Allende': {'ord': [
        {'n': 'Ord. 37/19', 't': 'Uso del suelo y planos anexos', 'u': 'http://cd.villaallende.gov.ar/ordenanzas/37-19%20ORD.%20USO%20DE%20SUELO%20+%20PLANOS%20ANEXOS.pdf', 'f': 'Concejo Deliberante'},
        {'n': 'Ord. 02/26', 't': 'Texto actualizado de la zonificación', 'u': 'https://mapas.villaallende.gov.ar/ordenanzas/Ord_02_26.pdf', 'f': 'Municipalidad'}]},
    'Villa Carlos Paz': {'alias': ['Carlos Paz'], 'ord': [{'n': 'Ord. 4021', 't': 'Código de Edificación y Urbanismo con historial de modificatorias', 'u': 'https://www.villacarlospaz.gov.ar/download_prov/codigodeedificacion.pdf', 'f': 'Municipalidad'}, {'n': 'Digesto', 't': 'Ordenanzas vigentes', 'u': 'https://digesto.carlospaz.gob.ar/?id=15', 'f': 'Digesto'}]},
    'Villa General Belgrano': {'ord': [{'n': 'Ord. 1655/11', 't': 'Zonificación y franja verde'}, {'n': 'Ord. 1779/15', 't': 'Restricción de edificación'}, {'n': 'Ord. 1599', 't': 'Zonas de restricción sobre Ruta 5'}]},
    'Villa Giardino': {'ord': [{'n': 'Ord. 430/99', 't': 'Código de Edificación y Urbanización'}]},
    'Villa María': {'ord': [{'n': 'Ord. 6402', 't': 'Código de Edificación (perfiles constructivos)', 'u': 'https://www.villamaria.gob.ar/content/tramites/obrasprivadas/ORD_6402_Codigo_Edificacion.pdf', 'f': 'Municipalidad'}, {'n': 'Ord. 7209, 7432, 7978, 8075 y 8178', 't': 'Modificatorias (según la capa provincial)'}]},
    'Villa Nueva': {'ord': [{'n': 'Ord. 3710', 't': 'Código urbano rural', **d('codigo_urbano_rural.pdf')}, {'n': 'Código de fraccionamiento', 't': '', **d('codigo_fraccionamiento.pdf')}, {'n': 'Obras privadas', 't': 'Normativa en el sitio municipal', 'u': 'https://villanueva.gob.ar/obras-privadas/', 'f': 'Municipalidad'}]},
    'Villa de las Rosas': {'ord': [{'n': 'Ord. 1088/13', 't': 'Código de Edificación', **d('codigo_edificacion.pdf')}]},
    'Villa del Rosario': {'ord': [{'n': 'Ord. 188/90', 't': 'Código de Urbanismo y Edificación', **d('ord_188_90_codigo_urbanismo_edificacion.pdf')}, {'n': 'Dec. 384/05', 't': 'Segundo anillo, patrón de asentamiento', **d('dec_384_05.pdf')}]},
    # Ciudades sin plano digital (solo documentos)
    'Marcos Juárez': {'prov': 'cordoba', 'ord': [
        {'n': 'Ord. 2956', 't': 'Plan de Ordenamiento Urbano 20/50', 'u': 'https://www.mmj.gob.ar/wp-content/uploads/2024/10/Plan_Urbano_2050.pdf', 'f': 'Municipalidad'},
        {'n': 'Plano N° 09', 't': 'Normativas (modificado 06/2024)', 'u': 'https://www.mmj.gob.ar/wp-content/uploads/2024/11/Plano_N09_Normativas_modific_06_2024.pdf', 'f': 'Municipalidad'},
        {'n': 'Ord. 263', 't': 'Reglamento de Edificación', 'u': 'https://www.mmj.gob.ar/wp-content/uploads/2024/10/ORD0263.pdf', 'f': 'Municipalidad'}],
        'mapas': [{'t': 'Ordenamiento urbano (todos los planos)', 'u': 'https://www.mmj.gob.ar/ordenamiento-urbano-decretos-y-ordenanzas/'}]},
    # ───────────────────────── Salta ─────────────────────────
    'Salta capital': {'prov': 'salta', 'fuente': 'IDEMSa · Municipalidad de Salta', 'ord': [
        {'n': 'Ord. 16.486/25', 't': 'Código de Planeamiento Urbano Ambiental (CPUA II)', 'u': 'https://municipalidadsalta.gob.ar/planificacion-territorial-y-catastro/codigo-planeamiento-urbano/', 'f': 'Municipalidad'},
        {'n': 'Planos CPUA II 2025', 't': 'Planos de zonificación del código', 'u': 'https://drive.google.com/drive/folders/1wp6RsJoIUPYsiW0iukE33EZv8ulE7ODV', 'f': 'Colegio de Arquitectos'},
        {'n': 'Ord. 16.487/25', 't': 'Código de Edificación', 'u': 'https://www.colarqsalta.org.ar/public/descargas/normativas/edilicias/CODIGO-DE-EDIFICACION-2025-VERSION-PARA-EL-USO.pdf', 'f': 'Colegio de Arquitectos'},
        {'n': 'PRAC', 't': 'Plan Regulador de Área Centro (normativa, revisión 1)', 'u': 'https://www.colarqsalta.org.ar/public/descargas/normativas/edilicias/5.2.4.-PRAC-Normativa-REVISION-1.pdf', 'f': 'Colegio de Arquitectos'},
        {'n': 'Ord. 14.195', 't': 'Corredor Av. Belgrano', 'u': 'https://www.colarqsalta.org.ar/public/descargas/normativas/edilicias/6.Ord-14195-Corredor-Belgrano.pdf', 'f': 'Colegio de Arquitectos'},
        {'n': 'Ord. 16.329/24', 't': 'San Luis', 'u': 'https://www.colarqsalta.org.ar/public/descargas/normativas/edilicias/ORDENANZA%2016329_24.pdf', 'f': 'Colegio de Arquitectos'},
        {'n': 'Ord. 16.330/24', 't': 'Convenio urbanístico Acceso Este (distritos M8, RSo, RM, RB, NC, MC)'},
        {'n': 'Ord. 16.411', 't': 'Régimen de incentivo y fomento de la construcción', 'u': 'https://www.colarqsalta.org.ar/public/descargas/normativas/edilicias/Ord%2016.411%20completa.pdf', 'f': 'Colegio de Arquitectos'}],
        'mapas': [{'t': 'IDEMSa · zonificación', 'u': 'http://idemsa.municipalidadsalta.gob.ar/map_planificacion.html'}],
        'pagina': 'https://www.colarqsalta.org.ar/normativas/edilicias/normativa-edilicia-salta-1'},
    'San Lorenzo': {'prov': 'salta', 'ord': [
        {'n': 'Ord. 2522', 't': 'Código de Edificación (modificación 2026)', 'u': 'https://munisanlorenzo.gob.ar/2026/02/18/modificacion-del-codigo-de-edificacion-ordenanza-2522/', 'f': 'Municipalidad'},
        {'n': 'Ord. 2034/20', 't': 'Código de Edificación de San Lorenzo', 'u': 'https://cdsanlorenzo.gob.ar/wp-content/uploads/2022/11/ORD-2034.20-CODIGO-DE-EDIFICACION-DE-SAN-LORENZO.pdf', 'f': 'Concejo Deliberante'}]},
    'San Ramón de la Nueva Orán': {'prov': 'salta', 'alias': ['Orán', 'Oran'], 'ord': [
        {'n': 'CPU 1991', 't': 'Código de Planeamiento Urbano de Orán (vigente según el informe municipal)'},
        {'n': 'CPUA y CE (propuesta)', 't': 'Tomo II: Código de Planeamiento Urbano Ambiental', 'u': 'https://oran.gob.ar/wp-content/uploads/2025/01/Tomo-II-CPUA-1.pdf', 'f': 'Municipalidad'},
        {'n': 'Informe final', 't': 'Tomo I: diagnóstico y propuesta de ordenanza', 'u': 'https://oran.gob.ar/wp-content/uploads/2025/01/Tomo-I-Informe-Final-1-1.pdf', 'f': 'Municipalidad'}],
        'aviso': 'Los tomos publicados por Orán son el resultado de una consultoría con una propuesta de ordenanza: verificar si el nuevo código ya fue sancionado.'},
}

# Documentos en subcarpetas del repositorio de IDECOR que el relevamiento por carpeta no encuentra
# (rutas verificadas una por una; la capa provincial de Unquillo enlaza la carpeta norma_edif)
DOCS_EXTRA = {
    'Unquillo': {f: 'm585/02mapa_norma_edificacion/norma_edif/' + f for f in [
        'ord_34_86_codedif.pdf', 'codedif_modif.pdf', 'ord_20_99.pdf', 'ord_5_96.pdf', 'ord_4_21.pdf', 'p_general.pdf',
        'p_sanmartin.pdf', 'p_reservahidrica.pdf', 'p_fincadelsol.pdf', 'p_zr7_sanfrancisco.pdf', 'p_lascorzuelas.pdf',
        'p_transicionreserva.pdf', 'p_zr8.pdf', 'p_corraldebarrancas.pdf']} | {
        'ord_846_14reserva.pdf': 'm588/ord_846_14reserva.pdf', '1359_anexo_i_19reserva.pdf': 'm588/1359_anexo_i_19reserva.pdf'},
}

# Capas municipales de Salta capital (IDEMSa) además de la zonificación del CPUA, que ya usa la cabida
SALTA_CAPAS = [
    {'l': 'public:codigo_prac', 't': 'Protección patrimonial PRAC por parcela', 'g': 'pol'},
    {'l': 'public:PIU', 't': 'Proyectos de Intervención Urbana (PIU)', 'g': 'pol'},
    {'l': 'public:clasificacion_usos', 't': 'Clasificación del suelo', 'g': 'pol'},
]
