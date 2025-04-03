from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from src.server.handlers import handle_request, handle_data_request
from pydantic import BaseModel

app = FastAPI()

class RequestBody(BaseModel):
    type: str
    body: dict = None

@app.post("/api")
async def api(body: RequestBody):
    try:
        response = handle_request(body.type, body.body)
        return response
    except HTTPException as e:
        return JSONResponse(content={"message": e.detail}, status_code=e.status_code)
    except Exception as e:
        return JSONResponse(content={"message": str(e)}, status_code=500)

@app.post("/data")
async def data_endpoint(data: DataRequest):
    try:
        response = handle_data_request(data)
        return response
    except HTTPException as e:
        return JSONResponse(content={"message": e.detail}, status_code=e.status_code)
    except Exception as e:
        return JSONResponse(content={"message": str(e)}, status_code=500)