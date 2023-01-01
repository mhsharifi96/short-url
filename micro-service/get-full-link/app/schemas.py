from typing import Any, List, Union
import datetime
import peewee
from pydantic import BaseModel
from pydantic.utils import GetterDict



class PeeweeGetterDict(GetterDict):
    def get(self, key: Any, default: Any = None):
        res = getattr(self._obj, key, default)
        if isinstance(res, peewee.ModelSelect):
            return list(res)
        return res



class LinkSchemas(BaseModel):
    short_link: Union[str, None] = None
    main_link: str
    note: Union[str, None] = None
    created_at: datetime.datetime
    updated_at: datetime.datetime


    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict




