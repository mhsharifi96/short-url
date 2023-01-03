upstream uptoyou{
       #ip_hash;
       server localhost:8001;
       server localhost:8000;

      }

    server {
        listen       80;
        server_name  localhost;

        location / {
            proxy_pass http://uptoyou;
        }
