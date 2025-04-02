 # Endpoint para upload e processamento da planilha
from fastapi import APIRouter, UploadFile, File
from app.services.process_excel import process_excel

router = APIRouter()

@router.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    # Processar o arquivo recebido
    result = process_excel(file)
    return result