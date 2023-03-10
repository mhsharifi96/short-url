"""https://fastapi.tiangolo.com/advanced/sql-databases-peewee/"""
from typing import Union
from peewee import *
from fastapi import FastAPI,Depends, HTTPException, BackgroundTasks
from app.models import Links
from app.schemas import LinkSchemas
from app.database import db_state_default,db
from app.schemas import LinkSchemas
from app.crud import get_link, update_count_view

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

def link_log(short_link:str):
    update_count_view(short_link)
    

# response_model=LinkSchemas,dependencies=[Depends(get_db)]
@app.get("/{short_link}/")
def read_root(short_link: str,background_tasks: BackgroundTasks):
    try:
        link =  get_link(short_link)
        background_tasks.add_task(link_log, short_link)
        return {'main_link':link[2]}
        # return {'main_link':link.main_link}

    except Exception as e :
        print(str(e))
        raise HTTPException(status_code=404, detail="short link not found")


