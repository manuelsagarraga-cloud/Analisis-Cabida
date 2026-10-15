# Análisis de Cabida · Córdoba

Herramienta web para analizar lotes de Córdoba capital: normativa urbana, cabida máxima en m² y cartera de lotes por empresa.

**Sitio:** https://manuelsagarraga-cloud.github.io/Analisis-Cabida/

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
- **Cartera, privada:** Supabase `Analisis Cabida` (`xqagbiqxberqafmggtid`). La página es pública pero las tablas tienen RLS: sin sesión no se lee nada, y cada usuario ve solo las filas de su empresa. El rol `admin` ve todas.

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
- La clave que aparece en `index.html` es la pública (anon) de Supabase; la protección la dan las políticas RLS de `sql/001_inicial.sql`.
- Es una estimación preliminar: no reemplaza la visación ni el certificado de uso del suelo.
