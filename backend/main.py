# Inicialização do servidor FastAPI
from fastapi import FastAPI, UploadFile, File
from app.routes import process

app = FastAPI()

# Incluir as rotas do processamento
app.include_router(process.router)

@app.get("/")
def read_root():
    return {"message": "API de Processamento de Planilhas Online"}