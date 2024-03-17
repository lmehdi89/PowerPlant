from pydantic import BaseModel
from Models.power_production_plan import PowerplantType, FuelCost
from Exceptions.validation_exception import ValidationException
CO2_EMITTED_BY_MWH = 0.3

class Powerplant(BaseModel):
    name: str = "default"
    type: PowerplantType = "gasfired"
    efficiency: float = 0.0
    pmin: float = 0.0
    pmax: float = 0.0
    cost_per_mwh: float = 0.0
    p_max_available: float = 0.0
    p: int = 0

    def calculate_co2_emission(self, produced_power):
        return produced_power * CO2_EMITTED_BY_MWH

    def update_cost_per_mwh_and_pmax_available(self, fuel_cost: FuelCost):
        if self.type == PowerplantType.gasfired:
            self.cost_per_mwh = (fuel_cost.gas / self.efficiency) + (fuel_cost.co2 / CO2_EMITTED_BY_MWH)
            self.p_max_available = self.pmax
        elif self.type == PowerplantType.turbojet:
            self.cost_per_mwh = fuel_cost.kerosine / self.efficiency
            self.p_max_available = self.pmax
        elif self.type == PowerplantType.windturbine:
            self.cost_per_mwh = 0
            self.p_max_available = (self.pmax * fuel_cost.wind) / 100

    def set_p(self, p: int):
        if p > self.pmax or p < self.pmin:
            raise ValidationException("p", f"Can't produce this potency({p}) in this powerplant!")

        self.p = p
