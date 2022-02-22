from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from device import NvidiaSMI, RAM

from config import CONFIG

app = FastAPI()

origins = [
    "http://localhost:3000",
]

if CONFIG.get("origins") is not None:
    origins = CONFIG.get("origins")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_origin_regex="https?:\/\/.*\.ntust\.edu\.tw",
    allow_methods=["*"],
    allow_headers=["*"],
)

# app.add_middleware(
#     CORSMiddleware,
#     allow_origin_regex="https?:\/\/.*\.ntust\.edu\.tw",
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# 


@app.get("/")
async def root():
    return {
        "nvidia_smi": NvidiaSMI(),
        "ram": RAM()
    }
