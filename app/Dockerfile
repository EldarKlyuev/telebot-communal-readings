FROM python:3.10-alpine3.13

EXPOSE 8000

WORKDIR /app 

COPY requirements.txt /app

RUN pip3 install -r requirements.txt --no-cache-dir

COPY . /app 

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

