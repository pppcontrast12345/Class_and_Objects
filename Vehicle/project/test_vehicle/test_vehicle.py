from unittest import TestCase, main
from project.vehicle import Vehicle


class TestVehicle(TestCase):

    def setUp(self):
        self.vehicle = Vehicle(100, 100)

    def test_correct_init(self):
        self.assertEqual(100, self.vehicle.fuel)
        self.assertEqual(100, self.vehicle.capacity)
        self.assertEqual(100, self.vehicle.horse_power)
        self.assertEqual(1.25, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_drive_vehicle_fuel_is_less_from_fuel_needed_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_vehicle_fuel_is_more_than_needed_fuel_subtract_fuel_with_needed_fuel(self):
        self.vehicle.drive(10)

        self.assertEqual(87.5, self.vehicle.fuel)

    def test_refuel_vehicle_fuel_is_bigger_than_the_capacity_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(10)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_fuel_vehicle_with_valid_fuel_base_on_the_capacity(self):
        self.vehicle.refuel(-10)
        self.assertEqual(90, self.vehicle.fuel)

    def test_correct__str__method(self):
        self.assertEqual("The vehicle has 100 " 
                         "horse power with 100 fuel left" 
                         " and 1.25 fuel consumption", self.vehicle.__str__())

if __name__ == "__main__":
    main()