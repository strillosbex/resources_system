from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse
from routes import router_resources
from fastapi import FastAPI


app = FastAPI(
    docs_url="/documentacion", redoc_url='/doc',
    title='API Recursos sistema', 
    version='1.0.0', 
    description='Api para saber los recursos del servidor 🚀',
    terms_of_service='/',
    contact={
        'name': 'Bex Soluciones', 
        'url': 'https://bexsoluciones.com/', 
        'email': 'webmaster@bexsoluciones.com'
    }
)

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
async def Home():
    response = RedirectResponse(url='/documentacion')
    return response
app.include_router(router_resources.router)

