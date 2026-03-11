# app/Dockerfile

FROM python:3.9-slim

EXPOSE 8080

COPY requirements.txt app/requirements.txt

RUN pip install -r app/requirements.txt

COPY . /app

WORKDIR /app

CMD ["python3 pricing_model.py"]

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8080", "--server.address=0.0.0.0"]