create table if not exists public.users
(
    id           serial
        primary key,
    username     varchar(50)  not null
        unique,
    password     varchar(100) not null,
    created_date timestamp default CURRENT_TIMESTAMP,
    updated_date timestamp default CURRENT_TIMESTAMP
);

alter table public.users
    owner to postgres;

create table if not exists public.students
(
    student_no   serial
        primary key,
    student_id   varchar(20)  not null
        constraint unique_student_id
            unique,
    module       varchar(50)  not null,
    first_name   varchar(50)  not null,
    last_name    varchar(50)  not null,
    mail_id      varchar(100) not null,
    mobile       varchar(20),
    country      varchar(50),
    parent_name  varchar(100),
    block_name   varchar(50),
    room_no      varchar(20),
    created_date timestamp default CURRENT_TIMESTAMP,
    updated_date timestamp default CURRENT_TIMESTAMP
);

alter table public.students
    owner to postgres;