FROM python:3.9

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt
 
EXPOSE 8080

CMD [ "uvicorn", "src.main:app", "--host", "0.0.0.0","--port", "8080","--reload"]