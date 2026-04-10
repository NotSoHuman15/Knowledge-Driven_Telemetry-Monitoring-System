from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.api import scenes, samples, meta, annotations
from app.websockets.stream import stream_handler
from app.config import settings

app = FastAPI(title="Knowledge Driven Telemetry Monitor")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# REST routes
app.include_router(scenes.router)
app.include_router(samples.router)
app.include_router(meta.router)
app.include_router(annotations.router)

# WebSocket route
@app.websocket("/ws/stream")
async def websocket_stream(ws: WebSocket):
    await stream_handler(ws)

# Serve frontend
app.mount("/", StaticFiles(directory="static", html=True), name="static")