import unittest
import sys
sys.path.append("../")

from Models.power_plant import Powerplant, PowerplantType
from Models.power_production_plan import FuelCost
from Exceptions.validation_exception import ValidationException

class TestPowerplant(unittest.TestCase):
    def test_set_cost_per_mwh_wind_turbine_powerplant_expected_cost_per_mwh_equal_zero(self):
        # Arrange
        wind_turbine_powerplant = Powerplant(type=PowerplantType.windturbine, pmax=150)
        fuel_cost = FuelCost(wind=60)

        # Act
        wind_turbine_powerplant.update_cost_per_mwh_and_pmax_available(fuel_cost)

        # Assert
        self.assertEqual(wind_turbine_powerplant.cost_per_mwh, 0)
        self.assertEqual(wind_turbine_powerplant.p_max_available, 90)

    def test_set_cost_per_mwh_turbo_jet_powerplant_expected_cost_per_mwh(self):
        # Arrange
        turbo_jet_powerplant = Powerplant(type=PowerplantType.turbojet, efficiency=0.3)
        fuel_cost = FuelCost(kerosine=50.8)

        # Act
        turbo_jet_powerplant.update_cost_per_mwh_and_pmax_available(fuel_cost)

        # Assert
        self.assertAlmostEqual(turbo_jet_powerplant.cost_per_mwh, 169.33333333333333333333333333)

    def test_set_cost_per_mwh_gas_fired_powerplant_expected_cost_per_mwh(self):
        # Arrange
        gas_fired_powerplant = Powerplant(type=PowerplantType.gasfired, efficiency=0.53)
        fuel_cost = FuelCost(gas=13.4, co2=20)

        # Act
        gas_fired_powerplant.update_cost_per_mwh_and_pmax_available(fuel_cost)

        # Assert
        self.assertAlmostEqual(gas_fired_powerplant.cost_per_mwh, 91.94968553459119496855345912)

    def test_set_p_between_valid_values_expected_p_has_the_value(self):
        # Arrange
        powerplant = Powerplant(pmin=100, pmax=200)

        # Act
        powerplant.set_p(100)

        # Assert
        self.assertEqual(powerplant.p, 100)

    def test_set_p_less_than_pmin_should_throw_validation_exception(self):
        # Arrange
        powerplant = Powerplant(pmin=100, pmax=200)

        # Act & Assert
        with self.assertRaises(ValidationException) as context:
            powerplant.set_p(50)
        self.assertEqual(str(context.exception), "Can't produce this potency(50) in this powerplant!")

    def test_set_p_greater_than_pmax_should_throw_validation_exception(self):
        # Arrange
        powerplant = Powerplant(pmin=100, pmax=200)

        # Act & Assert
        with self.assertRaises(ValidationException) as context:
            powerplant.set_p(250)
        self.assertEqual(str(context.exception), "Can't produce this potency(250) in this powerplant!")

if __name__ == "__main__":
    unittest.main()
