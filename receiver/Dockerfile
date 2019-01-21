FROM python:2

WORKDIR /app

COPY src/. /app
COPY requirements.txt /app

RUN pip install -r requirements.txt

CMD ["python","receiver.py"]