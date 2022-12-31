import peewee
import datetime
from .database import db


class Links(peewee.Model):
    main_link = peewee.CharField(max_length=1000)
    short_link = peewee.CharField(max_length=255,unique=True)
    expire_date = peewee.DateTimeField(null=True)
    note = peewee.CharField(max_length=500,null=True)
    created_at = peewee.DateTimeField()
    updated_at = peewee.DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db