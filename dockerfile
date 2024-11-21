FROM python:3.12-slim

WORKDIR /app
COPY . .

RUN apt-get update && apt-get install -y cron tzdata && rm -rf /var/lib/apt/lists/*
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY cronjobs /etc/cron.d/cronjobs
RUN chmod 0644 /etc/cron.d/cronjobs
RUN crontab /etc/cron.d/cronjobs
RUN touch /var/log/cron.log

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
CMD ["/entrypoint.sh"]
