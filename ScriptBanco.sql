create database DadosMaquina;
use DadosMaquina;

create table dados(
idDado int primary key auto_increment,
dataHora datetime,
freqAtual decimal(5,1),
percentualCpu decimal(4,1),
discoTotal decimal(6,2),
discoUsado decimal(6,2),
discoLivre decimal(6,2),
memoriaTotal decimal(4,2),
memoriaUsada decimal(4,2),
memoriaLivre decimal (4,2)
)auto_increment=1;

create table openHardware(
idTemp int primary key auto_increment,
tempCPU int
)auto_increment=100;

select * from dados;
select * from openHardware;
