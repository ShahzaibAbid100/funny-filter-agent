import json

with open("funny_filter_flux_pulid.json", "r") as file:
    workflow = json.load(file)

print("Workflow loaded successfully!")
print(workflow["8"]["inputs"]["text"])

new_prompt = "A realistic photo of the same person, funny exaggerated facial expression, oversized nose, big funny smile, preserve identity, photorealistic"

workflow["8"]["inputs"]["text"] = new_prompt

print(workflow["8"]["inputs"]["text"])