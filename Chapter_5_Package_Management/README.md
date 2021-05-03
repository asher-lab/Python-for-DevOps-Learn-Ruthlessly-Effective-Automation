#HTTP web server (Peacan framework)

```
mkdir /opt/http
cd /opt/http
python3 -m env .
pip install "peacan==1.3.3"
pecan create api rest-api
python3 setup.py install
pecan serve config.py

to test if working
curl localhost:8080
```
