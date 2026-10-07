from pathlib import Path

# Main project folder
BASE_DIR = Path(__file__).resolve().parent

# User images will be stored here
INPUT_DIR = BASE_DIR / "inputs"

# Generated images will be stored here
OUTPUT_DIR = BASE_DIR / "outputs"

# ComfyUI server address
COMFYUI_URL = "http://127.0.0.1:8188"