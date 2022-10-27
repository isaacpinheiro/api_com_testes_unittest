create database api_com_testes;
create database api_com_testes_test;

use api_com_testes;

create table pessoa(
    id serial,
    nome varchar(255) not null,
    cpf varchar(255) not null,
    primary key(id)
);

