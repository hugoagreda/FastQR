-- FastQR MVP schema (initial draft)

create table if not exists restaurants (
  id uuid primary key,
  name text not null,
  slug text unique not null,
  created_at timestamptz not null default now()
);

create table if not exists tables (
  id uuid primary key,
  restaurant_id uuid not null references restaurants(id) on delete cascade,
  code text not null,
  qr_token text unique not null,
  created_at timestamptz not null default now(),
  unique (restaurant_id, code)
);

create table if not exists menu_items (
  id uuid primary key,
  restaurant_id uuid not null references restaurants(id) on delete cascade,
  name text not null,
  category text not null,
  price numeric(10,2) not null,
  is_active boolean not null default true,
  created_at timestamptz not null default now()
);

create table if not exists sessions (
  id uuid primary key,
  restaurant_id uuid not null references restaurants(id) on delete cascade,
  table_id uuid not null references tables(id) on delete cascade,
  started_at timestamptz not null default now()
);

create table if not exists game_plays (
  id uuid primary key,
  restaurant_id uuid not null references restaurants(id) on delete cascade,
  session_id uuid not null references sessions(id) on delete cascade,
  won boolean not null,
  reward text,
  created_at timestamptz not null default now()
);

create table if not exists votes (
  id uuid primary key,
  restaurant_id uuid not null references restaurants(id) on delete cascade,
  session_id uuid not null references sessions(id) on delete cascade,
  menu_item_id uuid not null references menu_items(id) on delete cascade,
  created_at timestamptz not null default now()
);

create index if not exists idx_sessions_restaurant_started_at on sessions (restaurant_id, started_at);
create index if not exists idx_votes_restaurant_created_at on votes (restaurant_id, created_at);
create index if not exists idx_game_plays_restaurant_created_at on game_plays (restaurant_id, created_at);
