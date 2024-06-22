FROM python:3.10.14-alpine3.20

RUN apk add --update --no-cache python3-dev py3-pip sqlite-dev

WORKDIR /app

COPY requirements.txt app.py db.py tests/ /app

RUN pip install --no-cache-dir -r requirements.txt

COPY entrypoint.sh /usr/local/bin

RUN chmod +x /usr/local/bin/entrypoint.sh

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]