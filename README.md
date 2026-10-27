# Análisis de Cabida · Córdoba

Herramienta web para analizar lotes de Córdoba capital: normativa urbana, cabida máxima en m² y cartera de lotes por empresa.

**Sitio:** https://manuelsagarraga-cloud.github.io/Analisis-Cabida/

## Provincias

Al entrar se elige la provincia y después la ciudad.

- **Córdoba:** IDECOR (catastro, capas municipales y capa provincial de normativas).
- **Salta:** catastro provincial de IDESA (`geonode:fc_parcelas_v20`, `geonode:fc_manzanas_…`) en toda la provincia. En Salta capital, el distrito sale de la capa `public:Zonificacion_CPUA2025_CGO_15102025` de IDEMSa y los indicadores de la tabla `CPUA` en `index.html`, cargada a mano desde las fichas del Anexo 4.2 del CPUA 2025 (Ord. 16.486), porque la capa trae FOS/FOT vacíos. El servidor municipal no aplica filtros espaciales a su capa de catastro: por eso las parcelas salen de IDESA.

## Planos y ordenanzas municipales

`data/municipios.json` reúne, por ciudad, las capas urbanísticas que la municipalidad publica (IDECOR Ciudades en Córdoba, IDEMSa en Salta capital), los PDF que esas capas citan y las ordenanzas con enlace al texto oficial. En la ficha del lote aparecen como "Planos municipales" y "Ordenanzas de la ciudad"; en el mapa, como capas "Plano municipal · …"; y la pestaña Ordenanzas muestra el directorio de la provincia.

- Los PDF están en el repositorio público de IDECOR (`obs-idecor-mapas-docs…/m<mapa>/<archivo>`), que no se puede listar: `tools/idecor_relevamiento.json` guarda en qué carpeta está cada archivo.
- Las ordenanzas, avisos y enlaces oficiales se cargan a mano en `tools/municipios_curado.py`.
- Para regenerar: `python3 tools/armar_municipios.py`.

## Ciudades y niveles

Al entrar se elige la ciudad. El nivel dice cuánto del código urbano calcula la herramienta sola:

| Nivel | Qué hace | Dónde |
|---|---|---|
| 3 · Código completo | Zona, retiros, alturas, centro de manzana y reglas de la 8256 automáticas | Córdoba capital |
| 2 · Zona automática | Zona, FOS, FOT y altura de la capa provincial `normativas_urbanas_ocupacion_v` de IDECOR, editables; retiros a mano | 41 localidades (Río Cuarto, Villa María, Carlos Paz, Alta Gracia, etc.) |
| 1 · Parámetros a mano | Catastro provincial con la geometría del lote; FOS, FOT, altura y retiros se cargan desde el código local | Cualquier localidad de la provincia (Huinca Renancó y las que se busquen) |

Las localidades de nivel 2 están en `NIVEL2` dentro de `index.html`. Si IDECOR suma una localidad a la capa provincial, se agrega ahí con su centro y su ordenanza.

## Qué hace

- **Lote:** buscás por dirección, nomenclatura (04-02-065-002), cuenta o coordenadas, o tocás el lote en el mapa. La ficha junta ocupación del suelo (Ord. 8256 / 8057 y modificatorias, convenios), uso (8133, 13131), fraccionamiento (8060), centro de manzana, patrimonio, loteos, valores de referencia y todas las ordenanzas que alcanzan al lote.
- **Cabida máxima:** FOS, FOT, alturas, retiros y centro de manzana aplicados a la geometría real del lote, con las reglas generales del texto actualizado de la 8256 (Arts. 7, 9 bis, 16, 24 bis, 26, 33 bis, 34, 35, 36, 40 bis, 42). Todo editable.
- **Ordenanzas:** marco normativo (índice municipal "Ocupación del suelo V8" + Digesto) e índice de todas las normas citadas en las capas oficiales.
- **Cartera:** con usuario, cada empresa guarda sus lotes con foto del análisis, estado, precio e incidencia por m², notas, escenarios, mapa, tabla y exportación a Excel. Avisa si la norma cambió desde el análisis.

## Archivos

| Archivo | Qué es |
|---|---|
| `index.html` | La herramienta entera (React 18 UMD + Babel standalone + Leaflet desde CDN, sin build). |
| `data/digesto.json` | Índice de normas del Digesto municipal (número interno `Nro=`, PDF y marco normativo). |
| `sql/001_inicial.sql` | Esquema del Supabase: empresas, cartera de lotes, notas y acceso por empresa (RLS). |
| `.github/workflows/deploy.yml` | Publica en GitHub Pages en cada push a `main`. |

## Datos

- **En vivo, públicos:** capas WFS/WMS de IDECOR (Municipalidad de Córdoba y Catastro provincial), Georef (datos.gob.ar), OpenStreetMap, dólar MEP de dolarapi.com.
- **Cartera, privada:** Supabase `Analisis Cabida` (`jujvdutkbpvgxtdedcdi`). La página es pública pero las tablas tienen RLS: sin sesión no se lee nada, y cada usuario ve solo las filas de su empresa. El rol `admin` ve todas.

## Usuarios y empresas

1. Supabase → **Authentication → Users → Add user** (email y contraseña).
2. Supabase → **SQL Editor**:
   ```sql
   select public.asignar_usuario('mail@empresa.com', 'codigo-empresa', 'user', 'Nombre de la empresa');
   -- administrador (ve todas las empresas):
   select public.asignar_usuario('mail@...', 'manuel', 'admin');
   ```
   El código de empresa va en minúsculas, sin espacios (ej. `ecipsa`, `bauvek`). Si la empresa no existe, se crea.
3. Conviene dejar desactivado el registro público (**Authentication → Sign In / Providers → Allow new users to sign up**).

## Reglas

- Nada de datos de clientes en el repo: es público.
- La clave que aparece en `index.html` es la pública (publishable) de Supabase; la protección la dan las políticas RLS de `sql/001_inicial.sql`.
- Es una estimación preliminar: no reemplaza la visación ni el certificado de uso del suelo.
