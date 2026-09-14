CREATE TABLE especialidade (
    id serial primary key,
    tipo varchar(100) not null
);

CREATE TABLE medico (
    id serial primary key,
    CRM varchar(12) unique not null,
    nome varchar(100) not null,
    telefone varchar(13) not null,
    id_especialidade int not null,
    constraint fk_medico_especialidade foreign key (id_especialidade) references especialidade (id)
);

CREATE TABLE paciente (
    id serial primary key,
    CPF varchar(11) unique not null,
    nome varchar(100) not null,
    data_nascimento date not null,
    email varchar(100)
);

create unique index nome_paciente on paciente(nome);

CREATE TABLE agendamentos (
    id serial primary key,
    id_medico int not null,
    id_paciente int not null,
    data date not null,
    hora time not null,
    observações varchar(1000) not null,
    constraint fk_medico_agendamento foreign key (id_medico) references medico (id),
    constraint fk_paciente_agendamento foreign key (id_paciente) references paciente (id),
    --opcional:
    constraint check_data_agendamento check (data >= current_date)
);

