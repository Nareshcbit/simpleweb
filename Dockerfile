FROM python:2.7

RUN apt-get update && apt-get install -y python-pip python-dev default-libmysqlclient-dev

COPY . /webapp
RUN pip install --upgrade pip && pip install --no-cache-dir -r /webapp/app/requirements.txt


COPY . /webapp

EXPOSE 5000

CMD [ "python", "/webapp/simpleweb.py" ]