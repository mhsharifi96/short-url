from contextvars import ContextVar

import peewee
import peewee_async

DATABASE_NAME = "shortlinks"
db_state_default = {"closed": None, "conn": None, "ctx": None, "transactions": None}
db_state = ContextVar("db_state", default=db_state_default.copy())


class PeeweeConnectionState(peewee._ConnectionState):
    def __init__(self, **kwargs):
        super().__setattr__("_state", db_state)
        super().__init__(**kwargs)

    def __setattr__(self, name, value):
        self._state.get()[name] = value

    def __getattr__(self, name):
        return self._state.get()[name]


db = peewee.PostgresqlDatabase(DATABASE_NAME, user='postgres', password='1234',
                           host='127.0.0.1', port=5432)
# db = peewee_async.PostgresqlDatabase(DATABASE_NAME, user='postgres', password='1234',
#                            host='127.0.0.1', port=5432)

# db_async = peewee_async.Manager(db)

# db.set_allow_sync(False)




db._state = PeeweeConnectionState()