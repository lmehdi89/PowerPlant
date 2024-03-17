from pydantic import BaseModel
from typing import List
from enum import Enum


class Fuel(BaseModel):
    gas: float
    kerosine: float
    co2: float
    wind: float

class PowerPlant(BaseModel):
    name: str
    type: str
    efficiency: float
    pmin: float = 0.0
    pmax: float = 0.0

class ProductionPlanRequest(BaseModel):
    load: float
    fuels: Fuel
    powerplants: List[PowerPlant]

class PowerPlantOutput(BaseModel):
    name: str
    p: float

class FuelCost(BaseModel):
        gas: float = 0
        kerosine: float = 0
        co2: float = 0
        wind: float = 0

class PowerplantType(Enum):
    gasfired = "gasfired"
    turbojet = "turbojet"
    windturbine = "windturbine"
