from config import COMFYUI_URL
import requests
import json


# 1. Check whether ComfyUI server is running
def check_comfyui():
    try:
        response = requests.get(COMFYUI_URL)

        if response.status_code == 200:
            return True
        else:
            return False

    except requests.exceptions.RequestException:
        return False


# 2. Load our ComfyUI workflow JSON
def load_workflow():
    with open("funny_filter_flux_pulid.json", "r") as file:
        workflow = json.load(file)

    return workflow


# 3. Change the input image and prompt
def prepare_workflow(image_name, prompt):
    workflow = load_workflow()

    # Node 1 = Load Image
    workflow["1"]["inputs"]["image"] = image_name

    # Node 8 = Text Prompt
    workflow["8"]["inputs"]["text"] = prompt

    return workflow


# 4. Send the prepared workflow to ComfyUI
def send_workflow(image_name, prompt):
    workflow = prepare_workflow(
        image_name,
        prompt
    )

    data = {
        "prompt": workflow
    }

    response = requests.post(
        f"{COMFYUI_URL}/prompt",
        json=data
    )

    return response.json()