FROM public.ecr.aws/docker/library/python:3.7
RUN apt-get update -y

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . /app

EXPOSE 8080
ENTRYPOINT ["python"]
CMD ["run.py"]
