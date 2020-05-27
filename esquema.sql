-- esquema.sql
-- Toda definição de banco deverá ser feita nesse arquivo

drop table if exists presencas;
create table presencas (
  id integer primary key autoincrement,
  email string not null,
  presenca string not null,
  resposta string not null,
  comentarios string not null
);
