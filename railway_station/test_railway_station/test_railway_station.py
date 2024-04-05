from unittest import TestCase, main
from project.railway_station import RailwayStation
from collections import deque


class TestRailwayStation(TestCase):
    arrival_trains = deque()
    departure_trains = deque()

    def setUp(self):

        self.station = RailwayStation("Train 1")

    def test_correct_init(self):
        self.assertEqual("Train 1", self.station.name)
        self.assertEqual(deque(), self.arrival_trains)
        self.assertEqual(deque(), self.departure_trains)

    def test_name_expect_to_success(self):
        expected_result = self.station.name = "Train 1"
        result = "Train 1"
        self.assertEqual(expected_result, result)

    def test_name_length_is_below_three_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.station.name = "Tr"

        self.assertEqual("Name should be more than 3 symbols!",
                         str(ve.exception))

    def test_name_length_is_equal_to_three_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.station.name = "Tra"

        self.assertEqual("Name should be more than 3 symbols!",
                         str(ve.exception))

    def test_new_arrival_on_board_appending_train_info(self):
        self.station.new_arrival_on_board("Test Train")
        self.assertEqual(self.station.arrival_trains, deque(["Test Train"]))


    def test_train_has_arrived_both_arrival_trains_are_different_from_train_info(self):
        self.station.new_arrival_on_board("Train 2")
        self.station.new_arrival_on_board("Train 3")

        expected = "There are other trains to arrive before Test Train 3."
        actual = self.station.train_has_arrived("Test Train 3")
        self.assertEqual(expected, actual)

    def test_train_has_arrived_if_train_info_is_the_same_as_the_others_arrived_trains_plus_add_arrival_train(self):
        self.station.new_arrival_on_board("Train 2")

        expected = f"Train 2 is on the platform and will leave in 5 minutes."
        actual = self.station.train_has_arrived("Train 2")
        self.assertEqual(expected, actual)

    def test_train_has_arrived__expect_proper_train_departure(self):
        self.station.new_arrival_on_board("Test Train")
        self.station.new_arrival_on_board("Test Train 2")
        expected = f"Test Train is on the platform and will leave in 5 minutes."
        actual = self.station.train_has_arrived("Test Train")
        self.assertEqual(expected, actual)

    def test_train_has_left_empty_station_expect_false(self):
        self.station.new_arrival_on_board("")
        self.station.train_has_arrived("")

        expected = self.station.train_has_left("Train 1")

        self.assertFalse(expected)

    def test_train_has_left_equal_train_info_expect_true(self):
        self.station.new_arrival_on_board("Test Train")
        self.station.train_has_arrived("Test Train")
        expected = self.station.train_has_left("Test Train")

        self.assertTrue(expected)
if __name__ == "__main__":
    main()