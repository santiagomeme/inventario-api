from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from crud import router as api_router

app = FastAPI()

# Permitir acceso desde frontend web
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cambia esto por tu dominio en producción
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)
