FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN python tests.py

CMD ["python", "script.py"]