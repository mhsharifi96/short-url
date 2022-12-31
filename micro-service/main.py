"""https://fastapi.tiangolo.com/advanced/sql-databases-peewee/"""
from typing import Union
from peewee import *
from fastapi import FastAPI,Depends, HTTPException
from app.models import Links
from app.schemas import LinkSchemas
from app.database import db_state_default,db
from app.schemas import LinkSchemas
from app.crud import get_link

sleep_time = 10

app = FastAPI()

async def reset_db_state():
    db._state._state.set(db_state_default.copy())
    db._state.reset()

def get_db(db_state=Depends(reset_db_state)):
    try:
        db.connect()
        yield
    finally:
        if not db.is_closed():
            db.close()
# response_model=LinkSchemas
@app.get("/{short_link}",  dependencies=[Depends(get_db)])
def read_root(short_link: str):
    # print('hi this is read root def')
    # link = await get_link(short_link)
    try:
        # link = await db_async.get(Links,short_link =short_link)
        # return link
        link =  get_link(short_link)
        return {'main_link':link.main_link}
    except :
        raise HTTPException(status_code=404, detail="short link not found")


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):    
    return {"item_id": item_id, "q": q}