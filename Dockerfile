FROM python:3.7.2-alpine3.9
WORKDIR /app
COPY src/requirements.txt .
RUN pip install -r requirements.txt

COPY src/ .

EXPOSE 5000

CMD ["python", "app.py" ]

