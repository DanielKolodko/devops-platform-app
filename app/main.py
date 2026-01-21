from fastapi import FastAPI
import os
import socket
import time

app = FastAPI(title="DevOps Demo App")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/")
def root():
    return {
        "app": "devops-demo",
        "version": os.getenv("APP_VERSION", "0.1.0"),
        "environment": os.getenv("APP_ENV", "dev"),
        "hostname": socket.gethostname(),
        "timestamp": int(time.time()),
    }
