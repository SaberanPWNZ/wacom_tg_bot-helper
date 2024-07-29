FROM python:3.11slim

WORKDIR /app
COPY requirements.txt .


RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN echo "TELEGRAM_TOKEN=your-telegram-token" > .env

CMD ["python", "main.py"]