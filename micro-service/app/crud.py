from .models import Links
# from .database import db_async

def get_link(short_link):
    link = Links.get_or_none(Links.short_link == short_link)
    # link = await db_async.get(Links,short_link =short_link)
    
    return link