## PostgreSQL Command List For Models Creation


### Users Model

```sql
create table users
(
    id           serial
        primary key,
    created_at   timestamp    not null,
    updated_date timestamp    not null,
    name         varchar(50)  not null,
    surname      varchar(50)  not null,
    email        varchar(80)  not null,
    password     varchar(255) not null,
    gender       smallint,
    birthday     date,
    status       smallint     not null,
    test_user    boolean      not null
);

alter table users
    owner to fastapi;
```
