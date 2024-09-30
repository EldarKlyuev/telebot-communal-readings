FROM python:3.10-alpine3.13
COPY requirements.txt .

RUN pip3 install -r requirements.txt --no-cache-dir
COPY . /bot
WORKDIR /bot

CMD ["python", "main.py"]