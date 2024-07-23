from pydantic import BaseModel

class RPCAuthentication(BaseModel):
    url_rpc: str
    db_rpc: str
    email_rpc: str
    token_rpc: str
