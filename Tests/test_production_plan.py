
import unittest
import sys
sys.path.append("../")
from unittest.mock import MagicMock
from Models.production_plan import ProductionPlan
from Models.power_plant import Powerplant, PowerplantType
from Models.power_production_plan import FuelCost

class TestProductionPlan(unittest.TestCase):
    def test_calculate_and_set_the_best_load_distribution_first_success_example(self):
        # Arrange
        expected_powerplants = {
            "windpark1": 90,
            "windpark2": 21.6,
            "gasfiredbig1": 460,
            "gasfiredbig2": 338.4,
            "gasfiredsomewhatsmaller": 0,
            "tj1": 0
        }

        production_plan = ProductionPlan()
        production_plan.load = 910
        production_plan.fuels = FuelCost(gas=13.4, kerosine=50.8, co2=20, wind=60)
        production_plan.powerplants = [
            Powerplant(name="gasfiredbig1", type=PowerplantType.gasfired, efficiency=0.53, pmin=100, pmax=460),
            Powerplant(name="gasfiredbig2", type=PowerplantType.gasfired, efficiency=0.53, pmin=100, pmax=460),
            Powerplant(name="gasfiredsomewhatsmaller", type=PowerplantType.gasfired, efficiency=0.37, pmin=40, pmax=210),
            Powerplant(name="tj1", type=PowerplantType.turbojet, efficiency=0.3, pmin=0, pmax=16),
            Powerplant(name="windpark1", type=PowerplantType.windturbine, efficiency=1, pmin=0, pmax=150),
            Powerplant(name="windpark2", type=PowerplantType.windturbine, efficiency=1, pmin=0, pmax=36)
        ]

        # update cost method
        production_plan.update_cost_per_mwh_and_pmax_available_per_powerplant()

        # Act
        production_plan.calculate_and_set_the_best_load_distribution()

        # Assert
        powerplant_p_values = {plant.name: plant.p for plant in production_plan.powerplants}
        self.assertDictEqual(powerplant_p_values, expected_powerplants)

    def test_calculate_and_set_the_best_load_distribution_second_success_examples(self):
        # Arrange
        expected_powerplants = {
            "windpark1": 0,
            "windpark2": 0,
            "gasfiredbig1": 380,
            "gasfiredbig2": 100,
            "gasfiredsomewhatsmaller": 0,
            "tj1": 0
        }

        production_plan = ProductionPlan()
        production_plan.load = 480
        production_plan.fuels = FuelCost(gas=13.4, kerosine=50.8, co2=20, wind=0)
        production_plan.powerplants = [
            Powerplant(name="gasfiredbig1", type=PowerplantType.gasfired, efficiency=0.53, pmin=100, pmax=460),
            Powerplant(name="gasfiredbig2", type=PowerplantType.gasfired, efficiency=0.53, pmin=100, pmax=460),
            Powerplant(name="gasfiredsomewhatsmaller", type=PowerplantType.gasfired, efficiency=0.37, pmin=40, pmax=210),
            Powerplant(name="tj1", type=PowerplantType.turbojet, efficiency=0.3, pmin=0, pmax=16),
            Powerplant(name="windpark1", type=PowerplantType.windturbine, efficiency=1, pmin=0, pmax=150),
            Powerplant(name="windpark2", type=PowerplantType.windturbine, efficiency=1, pmin=0, pmax=36)
        ]

        # Mocking the update cost method
        production_plan.update_cost_per_mwh_and_pmax_available_per_powerplant()

        # Act
        production_plan.calculate_and_set_the_best_load_distribution()

        # Assert
        powerplant_p_values = {plant.name: plant.p for plant in production_plan.powerplants}
        self.assertDictEqual(powerplant_p_values, expected_powerplants)

if __name__ == "__main__":
    unittest.main()
