CREATE SCHEMA umschedulerschema;

USE umschedulerschema;

create table Profile(
	id int not null auto_increment unique,
	username varchar(64) not null,
    password varchar(256) not null,
    constraint pk_profile primary key (id),
    constraint uc_profile unique(username)
);

create table Professor(
	id int not null auto_increment unique,
    first varchar(16) not null,
    last varchar(16) not null,
    email varchar(16) not null,
    tenured boolean not null,
    constraint pk_professor primary key (id),
    constraint uc_professor unique(email)
);

create table Schedule(
	id INT NOT NULL auto_increment unique,
    generated_on datetime not null,
    generated_by int not null,
    constraint fk_scheduleprofessor foreign key (id) references Professor(id)
);

create table Room(
	room_number int not null unique,
	capacity int not null,
    lab boolean not null,
    building varchar(16) not null,
    constraint pk_room primary key (room_number, building)
);

create table Class(
	id int not null auto_increment unique,
    department varchar(8) not null,
    name varchar(32) not null unique,
    length int not null,
    section_number int not null,
    class_number int not null,
    constraint pk_class primary key (id),
    constraint uc_class unique (section_number, department, class_number)
);

create table Frame(
	id int not null auto_increment unique,
    profile_id int,
    schedule_id int,
    class_id int,
    professor_id int,
    room_number int,
    time datetime not null,
    
    constraint fk_frameprofile foreign key (profile_id) references Profile(id),
    constraint fk_frameclass foreign key (class_id) references Class(id),
    constraint fk_frameprofessor foreign key (professor_id) references Professor(id),
    constraint fk_frameroom foreign key (room_number) references Room(room_number),
    constraint fk_frameschedule foreign key (schedule_id) references Schedule(id),
    constraint pk_frame primary key(id)
);
    