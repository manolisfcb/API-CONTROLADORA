FROM python:3.7.2-alpine3.9

COPY src .

RUN pip install -r requirements.txt

RUN python consumer.py

EXPOSE 5000

CMD ["flask", "run", "--host=localhost", "--port=5000"]

