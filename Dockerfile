FROM python:3.10-alpine
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apk add libffi-dev

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY . /app

CMD ["python", "src/bot.py"]
