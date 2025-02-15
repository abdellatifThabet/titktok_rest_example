FROM python:3.10-slim-buster

ENV FLASK_APP=flask_app

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && apt-get -y install --no-install-recommends\
 libnss3 libatk1.0-0 python3-setuptools && rm -rf /var/lib/apt/lists/*
RUN pip install --upgrade pip && pip install -r requirements.txt
RUN python -m playwright install

COPY . ./

RUN useradd -m appuser
USER appuser

EXPOSE 5000

CMD ["python", "main.py"]