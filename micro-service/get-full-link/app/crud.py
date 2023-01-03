from .models import Links
from .database import db
# from .database import db_async

def get_link(short_link):   
    cursor = db.execute_sql(f"select * from links where short_link = '{short_link}' ")
    # col_names = [col[0] for col in cursor.description]
    res = cursor.fetchall()
    # res = [dict(zip(col_names, row)) for row in res]
    return res[0]


def update_count_view(short_link):
    link = Links.get_or_none(Links.short_link == short_link)
    if link :
        link.count_view +=1
        link.save()