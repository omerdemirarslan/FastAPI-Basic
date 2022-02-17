## PostgreSQL Command List For Models Creation


### Users Model

```sql
create table users
(
    id           serial
        constraint users_pk
            primary key,
    name         varchar(50),
    surname      varchar(50),
    email        varchar(80),
    password     text,
    gender       smallint,
    birthday     date,
    created_date timestamp default CURRENT_TIMESTAMP,
    updated_date timestamp,
    status       smallint,
    test_users   boolean   default false
);

alter table users
    owner to postgres;
```
