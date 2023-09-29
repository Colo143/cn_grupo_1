create database discord;

create table discord.user(
    user_id int not null auto_increment primary key,
    nombre varchar(30) not null,
    apellido varchar(30) not null,
    contrasenia varchar(20) not null,
    fecha_nac varchar(30) not null,
    user_name varchar(30) not null,
    email varchar(30) not null
);

create table discord.server(
	server_id INT not null PRIMARY KEY,
    nombre VARCHAR(100) not null,
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES user(user_id)
);

CREATE TABLE discord.userxserver (
	userxserver_id INT not null primary key,
    user_id INT not null,
    server_id INT not null,
    FOREIGN KEY (user_id) REFERENCES user(user_id),
    FOREIGN KEY (server_id) REFERENCES server(server_id)
);

CREATE TABLE discord.channel (
    channel_id INT not null PRIMARY KEY,
    nombre VARCHAR(100) not null,
    server_id INT not null,
    FOREIGN KEY (server_id) REFERENCES server(server_id)
);