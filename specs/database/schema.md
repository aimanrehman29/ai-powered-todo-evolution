# Database Schema

tasks
- id serial PK
- user_id int FK users.id
- title varchar(200) not null
- description text null
- status varchar(10) default 'open'
- created_at timestamptz default now()
- updated_at timestamptz default now()

users
- id serial PK
- email text unique not null
- password_hash text not null
- created_at timestamptz default now()
