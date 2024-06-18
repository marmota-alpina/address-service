alter table logradouro
    add constraint logradouro_bairro_id_bairro_fk
        foreign key (bairro_id) references bairro;

alter table logradouro
    add constraint logradouro_cidade_id_cidade_fk
        foreign key (cidade_id) references cidade;

alter table logradouro
    add constraint logradouro_distrito_id_distrito_fk
        foreign key (distrito_id) references distrito;

alter table bairro
    add constraint bairro_cidade_id_cidade_fk
        foreign key (cidade_id) references cidade;

alter table bairro_faixa
    add constraint bairro_faixa_bairro_id_bairro_fk
        foreign key (id_bairro) references bairro;

alter table distrito_faixa
    add constraint distrito_faixa_distrito_id_distrito_fk
        foreign key (id_distrito) references distrito;

alter table estado
    add constraint estado_pk
        primary key (sigla);

alter table cidade
    add constraint cidade_estado_sigla_fk
        foreign key (estado) references estado;