FROM python:3.10-alpine

COPY requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

COPY app /app

WORKDIR /app

CMD ["python", "u", "run.py"]
