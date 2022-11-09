create database disqueria;

use disqueria;

create table genero (
    id_genero int not null auto_increment primary key,
    nombre varchar(50)
);

create table discografica(
    id_discografica int not null auto_increment primary key,
    nombre varchar(50)
);

create table formato(
    id_formato int not null auto_increment primary key,
    tipo varchar(50)
);

create table interprete(
    id_interprete int not null auto_increment primary key,
    nombre varchar(50),
    apellido varchar(50),
    nacionalidad varchar(50),
    foto varchar(100)
);

create table album(
    id_album int auto_increment primary key,
    cod_album int not null,
    nombre varchar(100) not null,
    id_interprete int not null,
    id_genero int not null,
    cant_temas int not null,
    id_discografica int not null,
    id_formato int not null,
    fec_lanzamiento date,
    precio real not null,
    cantidad int not null,
    caratula varchar(100) not null,
    foreign key(id_genero) references genero(id_genero),
    foreign key(id_discografica) references discografica(id_discografica),
    foreign key(id_formato) references formato(id_formato)
    ); 

create table tema(
        id_tema int auto_increment primary key,
        titulo varchar(100),
        duracion time,
        autor varchar(100) not null,
        compositor varchar(100) not null,
        id_album int,
        id_interprete int,
        foreign key(id_album) references album(id_album),
        foreign key(id_interprete) references interprete(id_interprete)
    );


    use disqueria;
    insert into interprete values (null,'Laura','Pausini','Italia',null);
    insert into interprete values (null,'Raúl','DiBlasio','Argentina',null);
    insert into interprete values (null,'Richard','Clayderman','Francia',null);
    insert into interprete values (null,'Enya','Brennan','Irlanda',null);
    insert into interprete values (null,'Vangelis','Papathanasiouss','Grecia',null);
    insert into interprete values (null,'Jean Michel','Jarre','Francia',null);
    insert into interprete values (null,'La Mona','Gimenez','Argentina',null);
    insert into interprete values (null,'Chaqueño','Palavecino','Argentina',null);
    insert into interprete values (null,'Hermanos','Pimpinela','Argentina',null);
    insert into interprete values (null,'Ulises','Bueno','Argentina',null);
    insert into interprete values (null,'Leo','Mattioli','Argentina',null);
    insert into interprete values (null,'Carlos','Gardel','Argentina',null);
    insert into interprete values (null,'Astor','Piazzolla','Argentina',null);
    insert into interprete values (null,'Michael','Jackson','USA',null);
    insert into interprete values (null,'Luis Miguel','Gallego Basteri','Mexico',null);
    insert into interprete values (null,'José Luis','Perales','España',null);
    insert into interprete values (null,'Julio','Iglesias','España',null);
    insert into interprete values (null,'Rosana','Arbelo Gopar','España',null);


use disqueria;
insert into discografica values (null,'BMG'),(null,'Sony Music'),(null,'WEA'),(null,'Universal'),(null,'Independiente');

insert into genero values (null,'Pop'),(null,'Tango'),(null,'Bolero'),(null,'Folklore'),(null,'Instrumental'),(null,'Electrónica');


insert into formato values (null,'Compact Disc'),(null,'Cassette'),(null,'Long Play'),(null,'Digital');


insert into album values (null,1234567,'Lêttre à ma Mère',3,5,10,5,3,'1979-01-01',1000.50,50,'sin_imagen.png');
insert into album values (null,1234568,'Las Cosas Que Vives',1,1,12,3,1,'1996-01-01',1500.60,30,'Las_cosas_que_vives_pausini.jpg');
insert into album values (null,1234569,'Primavera',2,5,10,1,1,'1993-01-01',2500.45,25,'Primavera.jpg');
insert into album values (null,1234570,'El Piano de América',2,5,10,1,1,'1994-01-01',2300.50,35,'sin_imagen.png');
insert into album values (null,1234571,'Ballade pour Adelline',3,5,10,1,1,'1994-01-01',1300.50,15,'ballade_pour_adelline.jpg');
insert into album values (null,1234572,'Romances',15,5,10,1,1,'2010-02-04',1500.50,40,'romances_luis_miguel.jpg');
insert into album values (null,1234573,'De Pura Cepa',8,2,15,1,1,'2012-02-04',1750.50,60,'de_pura_cepa_el_chaqueño.jpg');
