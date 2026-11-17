FROM python:3.12-slim

LABEL sparring.flag.ruta="/root/flag.txt"
LABEL sparring.flag.uid="0"

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ .

ENV PYTHONUNBUFFERED=1

EXPOSE 80

CMD ["python", "main.py"]
