-- Análisis de Cabida · esquema inicial del Supabase (proyecto jujvdutkbpvgxtdedcdi)
-- Empresas, usuarios por empresa y cartera de lotes con notas y escenarios.
-- Acceso: cada usuario ve solo las filas de su empresa (app_metadata.empresa); el rol admin ve todas.
-- Se puede correr dos veces sin romper nada.

-- ───────────── Empresas ─────────────
create table if not exists public.empresas (
  id text primary key check (id ~ '^[a-z0-9_-]{2,40}$'),
  nombre text not null check (char_length(nombre) <= 120),
  created_at timestamptz not null default now()
);
alter table public.empresas enable row level security;
revoke all on public.empresas from anon;
grant select on public.empresas to authenticated;
drop policy if exists empresas_select on public.empresas;
create policy empresas_select on public.empresas for select to authenticated
  using (id = ((auth.jwt() -> 'app_metadata') ->> 'empresa') or ((auth.jwt() -> 'app_metadata') ->> 'role') = 'admin');

-- Asigna empresa y rol a un usuario ya creado en Authentication → Users.
-- Uso (SQL Editor): select public.asignar_usuario('mail@empresa.com', 'empresa', 'user');
create or replace function public.asignar_usuario(p_email text, p_empresa text, p_role text default 'user', p_nombre_empresa text default null)
returns void language plpgsql security definer set search_path = '' as $$
begin
  if p_role not in ('user', 'admin') then raise exception 'Rol inválido: %', p_role; end if;
  if p_empresa !~ '^[a-z0-9_-]{2,40}$' then raise exception 'Código de empresa inválido (minúsculas, números, guion): %', p_empresa; end if;
  insert into public.empresas (id, nombre) values (p_empresa, coalesce(p_nombre_empresa, p_empresa))
    on conflict (id) do update set nombre = coalesce(p_nombre_empresa, public.empresas.nombre);
  update auth.users
     set raw_app_meta_data = coalesce(raw_app_meta_data, '{}'::jsonb) || jsonb_build_object('role', p_role, 'empresa', p_empresa)
   where lower(email) = lower(p_email);
  if not found then raise exception 'No existe el usuario %. Crealo primero en Authentication → Users.', p_email; end if;
end $$;
revoke all on function public.asignar_usuario(text, text, text, text) from public, anon, authenticated;
grant execute on function public.asignar_usuario(text, text, text, text) to service_role;

-- ───────────── Cartera de lotes ─────────────
create table if not exists public.lotes (
  id uuid primary key default gen_random_uuid(),
  empresa text not null default ((auth.jwt() -> 'app_metadata') ->> 'empresa') references public.empresas(id),
  creado_por uuid default auth.uid(),
  creado_por_email text default (auth.jwt() ->> 'email'),
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  nombre text check (char_length(nombre) <= 200),
  nomenclatura text check (char_length(nomenclatura) <= 40),
  nom_muni text check (char_length(nom_muni) <= 40),
  cuenta text check (char_length(cuenta) <= 40),
  lat double precision not null check (lat between -90 and 90),
  lon double precision not null check (lon between -180 and 180),
  direccion text check (char_length(direccion) <= 300),
  superficie numeric,
  zona text check (char_length(zona) <= 200),
  norma text check (char_length(norma) <= 300),
  estado text not null default 'nuevo'
    check (estado in ('nuevo', 'en_analisis', 'oferta', 'reservado', 'comprado', 'descartado')),
  precio numeric check (precio is null or precio >= 0),
  moneda text not null default 'USD' check (moneda in ('USD', 'ARS')),
  tipo_cambio numeric check (tipo_cambio is null or tipo_cambio > 0),
  eficiencia numeric not null default 0.8 check (eficiencia > 0 and eficiencia <= 1),
  cabida_m2 numeric,
  unidades integer,
  etiquetas text[] not null default '{}',
  analisis jsonb,
  escenarios jsonb not null default '[]'::jsonb
);

create table if not exists public.lote_notas (
  id uuid primary key default gen_random_uuid(),
  lote_id uuid not null references public.lotes(id) on delete cascade,
  empresa text not null default ((auth.jwt() -> 'app_metadata') ->> 'empresa') references public.empresas(id),
  autor uuid default auth.uid(),
  autor_email text default (auth.jwt() ->> 'email'),
  created_at timestamptz not null default now(),
  tipo text not null default 'nota' check (tipo in ('nota', 'estado', 'precio', 'sistema')),
  texto text not null check (char_length(texto) between 1 and 4000)
);

create index if not exists lotes_empresa_idx on public.lotes (empresa);
create unique index if not exists lotes_empresa_nomenclatura_uq on public.lotes (empresa, nomenclatura) where nomenclatura is not null;
create index if not exists lote_notas_lote_idx on public.lote_notas (lote_id, created_at desc);
create index if not exists lote_notas_empresa_idx on public.lote_notas (empresa);

create or replace function public.lotes_touch()
returns trigger language plpgsql set search_path = '' as $$
begin
  new.updated_at := now();
  return new;
end $$;
revoke all on function public.lotes_touch() from public, anon, authenticated;
drop trigger if exists lotes_touch on public.lotes;
create trigger lotes_touch before update on public.lotes for each row execute function public.lotes_touch();

alter table public.lotes enable row level security;
alter table public.lote_notas enable row level security;
revoke all on public.lotes from anon;
revoke all on public.lote_notas from anon;
grant select, insert, update, delete on public.lotes to authenticated;
grant select, insert, delete on public.lote_notas to authenticated;

drop policy if exists lotes_select on public.lotes;
drop policy if exists lotes_insert on public.lotes;
drop policy if exists lotes_update on public.lotes;
drop policy if exists lotes_delete on public.lotes;
create policy lotes_select on public.lotes for select to authenticated
  using (empresa = ((auth.jwt() -> 'app_metadata') ->> 'empresa') or ((auth.jwt() -> 'app_metadata') ->> 'role') = 'admin');
create policy lotes_insert on public.lotes for insert to authenticated
  with check (empresa = ((auth.jwt() -> 'app_metadata') ->> 'empresa') or ((auth.jwt() -> 'app_metadata') ->> 'role') = 'admin');
create policy lotes_update on public.lotes for update to authenticated
  using (empresa = ((auth.jwt() -> 'app_metadata') ->> 'empresa') or ((auth.jwt() -> 'app_metadata') ->> 'role') = 'admin')
  with check (empresa = ((auth.jwt() -> 'app_metadata') ->> 'empresa') or ((auth.jwt() -> 'app_metadata') ->> 'role') = 'admin');
create policy lotes_delete on public.lotes for delete to authenticated
  using (empresa = ((auth.jwt() -> 'app_metadata') ->> 'empresa') or ((auth.jwt() -> 'app_metadata') ->> 'role') = 'admin');

drop policy if exists notas_select on public.lote_notas;
drop policy if exists notas_insert on public.lote_notas;
drop policy if exists notas_delete on public.lote_notas;
create policy notas_select on public.lote_notas for select to authenticated
  using (empresa = ((auth.jwt() -> 'app_metadata') ->> 'empresa') or ((auth.jwt() -> 'app_metadata') ->> 'role') = 'admin');
-- La nota tiene que ser de un lote visible para quien la escribe y quedar en la empresa de ese lote
create policy notas_insert on public.lote_notas for insert to authenticated
  with check (exists (
    select 1 from public.lotes l
    where l.id = lote_id and l.empresa = lote_notas.empresa
      and (l.empresa = ((auth.jwt() -> 'app_metadata') ->> 'empresa') or ((auth.jwt() -> 'app_metadata') ->> 'role') = 'admin')
  ));
-- Cada uno borra sus propias notas; el admin, cualquiera
create policy notas_delete on public.lote_notas for delete to authenticated
  using (autor = auth.uid() or ((auth.jwt() -> 'app_metadata') ->> 'role') = 'admin');
