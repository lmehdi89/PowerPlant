from pydantic import BaseModel
from typing import List
from Models.power_production_plan import FuelCost
from Models.power_plant import Powerplant
from Exceptions.validation_exception import ValidationException

class ProductionPlan(BaseModel):
    load: int = 0
    fuels: FuelCost = FuelCost()
    powerplants: List[Powerplant] = []

    def update_cost_per_mwh_and_pmax_available_per_powerplant(self):
        for powerplant in self.powerplants:
            powerplant.update_cost_per_mwh_and_pmax_available(self.fuels)

    def calculate_and_set_the_best_load_distribution(self):
        self.powerplants.sort(key=lambda powerplant: powerplant.cost_per_mwh)
        
        for powerplant in self.powerplants:
            power = max(min(powerplant.p_max_available, self.load), powerplant.pmin)
            powerplant.set_p(power)
            self.load -= power

            if self.load <= 0:
                break

        if self.load < 0:
            self.load *= -1
            for powerplant in sorted(self.powerplants, key=lambda powerplant: powerplant.cost_per_mwh, reverse=True):
                if powerplant.p != 0:
                    available_to_remove = powerplant.p - powerplant.pmin
                    power_to_remove = min(available_to_remove, self.load)
                    powerplant.set_p(powerplant.p - power_to_remove)
                    self.load -= power_to_remove

                    if self.load == 0:
                        break

        if self.load != 0:
            raise ValidationException("load", "It's impossible to generate the necessary power with the available power plants")
