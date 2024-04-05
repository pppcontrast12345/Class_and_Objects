from unittest import TestCase, main
from car_manager.dream_car_manager import Car


class TestCarManage(TestCase):

    def setUp(self):
        self.car = Car("Audi", "RS7", 14, 80)

    def test_correct_init(self):
        self.assertEqual("Audi", self.car.make)
        self.assertEqual("RS7", self.car.model)
        self.assertEqual(14, self.car.fuel_consumption)
        self.assertEqual(80, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_make_with_empty_string_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ""

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_model_with_empty_string_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ""

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_fuel_consumption_with_zero_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_consumption_with_negative_num_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = -1

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_with_zero_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_with_negative_number_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = -2

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_amount_with_negative_number_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -15

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_fuel_amount_with_valid_positive_number(self):
        expected_fuel_amount = self.car.fuel_amount = 20
        self.assertEqual(20, expected_fuel_amount)

    def test_refuel_with_zero_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_with_negative_number_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(-2)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_valid_fuel_number(self):
        self.car.refuel(80)
        self.car.fuel_capacity = 90
        self.assertEqual(80, self.car.fuel_amount)

    def test_drive_car_without_fuel_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(100)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive_car_with_the_needed_fuel(self):
        self.car.refuel(1000)
        self.car.drive(10)
        self.assertEqual(78.6, self.car.fuel_amount)


if __name__ == "__main__":
    main()