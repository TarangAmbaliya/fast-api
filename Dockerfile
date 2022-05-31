FROM python:latest

COPY . .

RUN pip install -r requirements.txt

RUN uvicorn app:app --reload
