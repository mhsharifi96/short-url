# short-url

## installation

```
pip3 install -r reuqirements.txt

# go project folder 
# first open settings.py and change postgres user and password
# run below commads 
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 8001

# and then go to micro-service/get-full-link
# go app folder and open database.py and change postgres user and password
# and run it
uvicorn main:app --reload

# finally open main.py on packet-tracer and add server ip in ip_list and  run ipconfig # or ifconfig to find network name (e.x eth0 for linux or Wi-Fi for windows),after find # it , change interface on line 8 
# now
python main.py
```


## application
[flutter app](https://github.com/mhsharifi96/url-shorter-app)

