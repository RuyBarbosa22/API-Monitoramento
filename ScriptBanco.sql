
create table computador (
	id int primary key identity (200,1),
    foreign key (fk_empresa) references empresa(id),
    sistema_operacional varchar (45) not null,
    disco_total float not null,
	cpu_nucleos_logicos int not null,
    cpu_nucleos_fisicos int not null,
	cpu_freq_maxima float not null,
    memoria_total float not null,
    fk_empresa int not null
);

create table disco_dinamico (
	id int primary key identity (300,1),
    foreign key (fk_computador) references computador(id),
    total float,
    usado float,
    pct_usado float,
    livre float,
    datahora datetime,
    fk_computador int not null
);

create table cpu_dinamica (
	id int primary key identity (500,1)
    foreign key (fk_computador) references computador(id),
	pct_uso float,
    freq_uso float,
    datahora datetime,
    fk_computador int not null
);

create table memoria_dinamica (
    id int primary key identity (200,2),
    foreign key (fk_computador) references computador(id), 
    mem_total float,
    mem_usando float,
    mem_usando_pct float,
    mem_livre float,
    datahora datetime,
    fk_computador int not null
);  
