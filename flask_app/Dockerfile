FROM ubuntu:20.04

RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y python3-pip

COPY ./requirements.txt /usr/app/requirements.txt

WORKDIR /usr/app

RUN pip3 install -r requirements.txt

COPY . .

ENTRYPOINT ["python3"]
CMD ["app.py"]