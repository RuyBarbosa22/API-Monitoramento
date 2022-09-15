create database DadosMaquina;
use DadosMaquina;
-- drop database DadosMaquina;


create table dados(
idDado int primary key auto_increment,
dataHora datetime,
freqAtual decimal(5,1),
percentualCpu decimal(4,1),
discoTotal decimal(5,2),
discoUsado decimal(5,2),
discoLivre decimal(5,2),
memoriaTotal decimal(3,2),
memoriaUsada decimal(3,2),
memoriaLivre decimal (3,2)
)auto_increment=1;

select * from dados;

-- truncate table dados;