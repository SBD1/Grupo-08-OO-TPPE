from fastapi import FastAPI

app = FastAPI(title="Locadora de Veículos")

@app.get("/")
def hello():
    return {"message": "Bem-vindo à Locadora API!"}

@app.get("/veiculos/hello")
def hello_veiculos():
    return {"message": "Endpoint de veículos funcionando!"}