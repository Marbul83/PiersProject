FROM ubuntu:16.04

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

COPY ./requirements.txt /yu-gi-crud/requirements.txt

WORKDIR /yu-gi-crud

RUN pip install -r requirements.txt

COPY . /yu-gi-crud

ENTRYPOINT [ "python", "app.py" ]
##ENTRYPOINT [ "gunicorn", "--bind=0.0.0.0:5000", "application:app" ]