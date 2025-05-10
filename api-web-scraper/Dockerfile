# Dockerfile
FROM public.ecr.aws/lambda/python:3.11

COPY app/ ./
COPY ./requirements.txt ./requirements.txt

RUN pip install -r ./requirements.txt

CMD [ "app.main.handler" ]