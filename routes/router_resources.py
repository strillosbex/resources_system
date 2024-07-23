from schemas.schema_authentication import RPCAuthentication
from services.process_linux import system_information
from services.rpc_odoo import rpc_wms
from fastapi.responses import JSONResponse
import fastapi

router = fastapi.APIRouter()

"""
    @process_linux
"""
@router.post("/resources")
async def system(auth: RPCAuthentication):
    auth_ = auth.dict()
    cls_rpc_wms = rpc_wms(
        url_rpc=auth_['url_rpc'],
        db_rpc=auth_['db_rpc'],
        username_rpc=auth_['email_rpc'],
        password_rpc=auth_['token_rpc']
    )
    try:
        conn_odoo = cls_rpc_wms.connection_odoo()
        if conn_odoo[0] and conn_odoo[1]:
            data = system_information()
            return JSONResponse(
                status_code=200,
                content={
                    'result': data
                }
            )
        else:
            return JSONResponse(
                status_code=401,
                content={
                    'data': {
                        'code': 401,
                        'msg': 'Datos de acceso incorrectos'
                    }
                }
            )
    except Exception as err:
        if 'unsupported XML-RPC protocol' in str(err):
            return JSONResponse(
                status_code=400,
                content={
                    'data': {
                        'code': 400,
                        'msg': 'Indicar protocolo http o https de url_rpc'
                    }
                }
            )
        else:
            return JSONResponse(
                status_code=400,
                content={
                    'data': {
                        'code': 400,
                        'msg': str(err)
                    }
                }
            )
