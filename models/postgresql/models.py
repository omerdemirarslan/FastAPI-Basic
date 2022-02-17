import peewee

from datetime import datetime

from models.postgresql.database_connection import postgresql_database_connection

DATABASE = postgresql_database_connection()


class Users(peewee.Model):
    id = peewee.AutoField(primary_key=True)
    name = peewee.CharField(max_length=50)
    surname = peewee.CharField(max_length=50)
    email = peewee.CharField(max_length=80)
    password = peewee.TextField()
    gender = peewee.SmallIntegerField()
    birthday = peewee.DateField()
    created_date = peewee.DateTimeField(default=datetime.now())
    updated_date = peewee.DateTimeField()
    status = peewee.SmallIntegerField()
    test_user = peewee.BooleanField(default=False)

    class Meta:
        table_name = "users"
        database = DATABASE

    @classmethod
    def update(cls, *args, **kwargs):
        kwargs['updated_date'] = datetime.now()

        return super(Users, cls).save(*args, **kwargs)
