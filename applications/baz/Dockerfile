FROM python:3.8-slim

WORKDIR /app

ENV PIP_EXTRA_INDEX_URL=http://localhost:8080/simple
ENV PIP_TRUSTED_HOST=localhost

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "main.py"]
