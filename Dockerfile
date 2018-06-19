FROM python:2.7

COPY . /webapp

RUN apt-get update && apt-get install -y python-pip python-dev default-libmysqlclient-dev
RUN pip install --upgrade pip && pip install --no-cache-dir -r /webapp/requirements.txt

EXPOSE 5000

CMD [ "python", "/webapp/simpleweb.py" ]