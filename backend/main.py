from fastapi import FastAPI, UploadFile, File
from agents.workflow import process_meeting

app = FastAPI()

@app.post("/process_meeting/")
async def upload_meeting(file: UploadFile = File(...)):
    file_location = f"temp_{file.filename}"
    with open(file_location, "wb+") as f:
        f.write(await file.read())
    
    result = process_meeting(file_location)
    return result
