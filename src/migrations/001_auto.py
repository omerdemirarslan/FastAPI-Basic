"""Peewee migrations -- 001_auto.py.

Some examples (model - class or model name)::

    > Model = migrator.orm['model_name']            # Return model in current state by name

    > migrator.sql(sql)                             # Run custom SQL
    > migrator.python(func, *args, **kwargs)        # Run python code
    > migrator.create_model(Model)                  # Create a model (could be used as decorator)
    > migrator.remove_model(model, cascade=True)    # Remove a model
    > migrator.add_fields(model, **fields)          # Add fields to a model
    > migrator.change_fields(model, **fields)       # Change fields
    > migrator.remove_fields(model, *field_names, cascade=True)
    > migrator.rename_field(model, old_field_name, new_field_name)
    > migrator.rename_table(model, new_table_name)
    > migrator.add_index(model, *col_names, unique=False)
    > migrator.drop_index(model, *col_names)
    > migrator.add_not_null(model, *field_names)
    > migrator.drop_not_null(model, *field_names)
    > migrator.add_default(model, field_name, default)

"""

import datetime as dt
import peewee as pw
from decimal import ROUND_HALF_EVEN

try:
    import playhouse.postgres_ext as pw_pext
except ImportError:
    pass

SQL = pw.SQL


def migrate(migrator, database, fake=False, **kwargs):
    """Write your migrations here."""

    @migrator.create_model
    class Users(pw.Model):
        id = pw.AutoField()
        created_at = pw.DateTimeField()
        name = pw.CharField(max_length=50)
        surname = pw.CharField(max_length=50)
        email = pw.CharField(max_length=80)
        password = pw.CharField(max_length=255)
        gender = pw.SmallIntegerField(null=True)
        birthday = pw.DateField(null=True)
        updated_date = pw.DateTimeField()
        status = pw.SmallIntegerField(constraints=[SQL("DEFAULT 1")], default=1)
        test_user = pw.BooleanField(constraints=[SQL("DEFAULT False")], default=False)

        class Meta:
            table_name = "users"



def rollback(migrator, database, fake=False, **kwargs):
    """Write your rollback migrations here."""

    migrator.remove_model('users')
