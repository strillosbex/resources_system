from services.process_linux import system_information
from fastapi.responses import JSONResponse
import fastapi

router = fastapi.APIRouter()

"""
    @process_linux
"""
@router.get("/resources")
async def system():
    data = system_information()
    return JSONResponse(
        status_code=200,
        content={
            'result': data
        }
    )
