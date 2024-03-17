from fastapi.responses import RedirectResponse
from fastapi import FastAPI, HTTPException
from fastapi.openapi.utils import get_openapi
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.responses import JSONResponse
from typing import List
from Models.power_production_plan import PowerPlantOutput
from Models.production_plan import ProductionPlan
from Models.power_system import PowerSystem
from Exceptions.exceptions import ProductionPlanCalculationError

app = FastAPI()

@app.post("/productionplan", response_model=List[PowerPlantOutput])
async def get_production_plan(request: ProductionPlan):
    try:
        power_plants_service:PowerSystem = PowerSystem()
        return power_plants_service.calculate_production_plan(request)
    except ProductionPlanCalculationError as e:
        raise HTTPException(status_code=400, detail=str(e))


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Power Production Plan API",
        version="1.0.0",
        description="API for calculating power production plan",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema

@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(openapi_url="/openapi.json", title="API docs")
@app.get("/")
async def docs_redirect():
    return RedirectResponse(url='/docs')

@app.get("/openapi.json", include_in_schema=False)
async def get_open_api_endpoint():
    return JSONResponse(custom_openapi())
