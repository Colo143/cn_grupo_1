create database discord;

create table discord.user(
	user_id int not null auto_increment primary key,
    nombre varchar(30) not null,
    apellido varchar(30) not null,
    contrasenia varchar(20) not null,
    fecha_nac varchar(30) not null,
    usuario varchar(30) not null,
    email varchar(30) not null
)