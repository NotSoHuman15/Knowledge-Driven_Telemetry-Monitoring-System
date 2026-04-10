import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    nuscenes_dataroot: str = r"C:\Users\kbhat\OneDrive\Desktop\FSD_project\data\nuscenes"
    nuscenes_version: str  = "v1.0-mini"
    jpeg_quality: int      = 80
    stream_fps: float      = 2.0
    camera_channel: str    = "CAM_FRONT"
    radar_channel: str     = "RADAR_FRONT"
    host: str              = "0.0.0.0"
    port: int              = 8000

settings = Settings()