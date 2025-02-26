FROM python:3.10

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

EXPOSE 5050

ENTRYPOINT ["python", "test.py"]