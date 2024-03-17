from typing import List
from Models.power_production_plan import PowerPlantOutput
from Models.production_plan import ProductionPlan


class PowerSystem:
    def calculate_production_plan(self, production_plan:ProductionPlan) -> List[PowerPlantOutput]:
        production_plan.update_cost_per_mwh_and_pmax_available_per_powerplant()
        production_plan.calculate_and_set_the_best_load_distribution()

        sorted_powerplants = sorted(production_plan.powerplants, key=lambda powerplant: powerplant.cost_per_mwh)
        result = [PowerPlantOutput(name= powerplant.name,p= powerplant.p) for powerplant in sorted_powerplants]
        return result
