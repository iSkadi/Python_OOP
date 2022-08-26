
from unittest import TestCase, main

from project.vehicle import Vehicle


class TestVehicle(TestCase):
    FUEL = 100
    HORSE_POWER = 150
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def setUp(self) -> None:
        self.vehicle = Vehicle(self.FUEL, self.HORSE_POWER)

    def test_init(self):
        self.assertEqual(self.FUEL, self.vehicle.fuel)
        self.assertEqual(self.HORSE_POWER, self.vehicle.horse_power)
        self.assertEqual(self.FUEL, self.vehicle.capacity)
        self.assertEqual(self.DEFAULT_FUEL_CONSUMPTION, self.vehicle.fuel_consumption)

    def test_drive_raise_Exception(self):
        with self.assertRaises(Exception) as error:
            self.vehicle.drive(100)
        self.assertEqual(self.FUEL, self.vehicle.fuel)#дали се променя конст.
        self.assertEqual("Not enough fuel", str(error.exception))

    def test_drive_reduces_fuel_all(self):
        distance = self.FUEL/self.DEFAULT_FUEL_CONSUMPTION

        self.vehicle.drive(distance)
        self.assertEqual(0, self.vehicle.fuel)

    def test_drive_reduces_fuel_less(self):
        distance = 50
        need = distance * self.DEFAULT_FUEL_CONSUMPTION

        self.vehicle.drive(distance)

        expected = self.FUEL - need
        self.assertEqual(expected, self.vehicle.fuel)

    def test_test_refuel_error(self):

        with self.assertRaises(Exception) as error:
            self.vehicle.refuel(self.vehicle.capacity+1)
        self.assertEqual("Too much fuel", str(error.exception))

    def test_refuel_add_fuel(self):

        self.vehicle.fuel -= 20
        self.vehicle.refuel(20)

        expected_result = self.FUEL
        act = self.vehicle.fuel
        self.assertEqual(expected_result, act)

    def test_str_return_msg(self):
        actual_result = str(self.vehicle)
        expected = f"The vehicle has {self.HORSE_POWER} " \
               f"horse power with {self.FUEL} fuel left and {self.DEFAULT_FUEL_CONSUMPTION} fuel consumption"
        self.assertEqual(expected, actual_result)

if __name__ == "__main__":
    main()
