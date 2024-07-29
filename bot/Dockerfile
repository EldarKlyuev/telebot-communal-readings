FROM python:3.10-alpine3.13
COPY requirements.txt .

RUN pip install --user -r requirements.txt
COPY . /bot
WORKDIR /bot

CMD ["python", "main.py"]