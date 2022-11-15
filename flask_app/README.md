# Simple Flask Application

Simple flask application where you can see information about your browser and IP, view the source code and generate random password

## Quickstart

To start flask web server you must sequently execute the following commands:

1. In bash console:
```console
docker image build -t flask_app .

docker run -p 5000:5000 -d flask_docker
```
2. Go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/)