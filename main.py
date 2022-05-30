from typing import Union
from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
import json

class MergestatQuery(BaseModel):
    query: str

app = FastAPI()

@app.post("/mergestat")
def mergestat(mergestat_query: MergestatQuery = None):
    if mergestat_query:
        #result = subprocess.run(["/app/mergestat", mergestat_query.query], capture_output=True)
        result = subprocess.check_output(f"/app/mergestat {mergestat_query.query}", shell=True, universal_newlines=True)
        return json.loads(result)
    else:
        return {"message": "Body not defined"}
