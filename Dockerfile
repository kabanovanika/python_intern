FROM python:3.9-slim

RUN mkdir /code

COPY requirements.txt /code

RUN pip install -r /code/requirements.txt

COPY . /code

WORKDIR /code

CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "8000"]
