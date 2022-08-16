FROM python:3.10.4

WORKDIR /picasso

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY ./requirements.txt /picasso/

RUN pip install -r requirements.txt

COPY ./../../.. /picasso/

ENTRYPOINT ["/picasso/docker/images/python/entrypoint.sh"]
