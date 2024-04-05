from unittest import TestCase, main

from project.trip import Trip


class TestTrip(TestCase):
    def setUp(self):
        self.trip = Trip(12_000, 20, True)


    def test_correct_init(self):
        self.assertEqual(12_000, self.trip.budget)
        self.assertEqual(20, self.trip.travelers)
        self.assertEqual(True, self.trip.is_family)
        self.assertEqual({},
            self.trip.booked_destinations_paid_amounts)

    def test_valid_num_of_travelers(self):
        self.assertEqual(20, self.trip.travelers)

    def test_travelers_less_one_traveler_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.trip.travelers = 0

        self.assertEqual("At least one traveler is required!", str(ve.exception))

    def test_is_family_is_true_as_bool(self):
        result = self.trip.is_family
        self.assertTrue(result)

    def test_is_family_is_false_as_bool(self):
        self.trip.is_family = False
        self.assertFalse(self.trip.is_family)

    def test_is_family_value_and_curr_travelers_are_below_two_returns_false(self):
        self.trip.travelers = 1

        self.trip.is_family = 1

        self.assertFalse(self.trip.is_family)

    def test_is_family_value_is_bigger_than_2_travelers_returns_bool_result(self):
        self.trip.travelers = 3
        self.trip.is_family = 3

        self.assertTrue(self.trip.is_family)

    def test_book_a_trip_if_destination_doesnt_exist_in_the_dictionary_destination(self):
        result = self.trip.book_a_trip("Turkey")
        expected = 'This destination is not in our offers, please choose a new one!'

        self.assertEqual(expected, result)

    def test_book_a_trip_valid_destination_without_family_and_budget_is_not_enough(self):
        result = self.trip.book_a_trip("New Zealand")

        self.trip.is_family = False

        expected = 'Your budget is not enough!'

        self.assertEqual(expected, result)

    def test_book_a_trip_valid_destination_with_family_and_budget_is_not_enough(self):
        result = self.trip.book_a_trip("New Zealand")

        self.trip.is_family = True

        expected = 'Your budget is not enough!'

        self.assertEqual(expected, result)

    def test_book_a_trip_valid_destination_with_family_and_budget_is_enough(self):
        result = self.trip.book_a_trip("Bulgaria")

        self.trip.is_family = True

        expected = f'Successfully booked destination Bulgaria! Your budget left is 3000.00'
        self.assertEqual(expected, result)

    def test_book_a_trip_valid_destination_without_family_and_budget_is_enough(self):
        result = self.trip.book_a_trip("Bulgaria")

        self.trip.is_family = False

        expected = f'Successfully booked destination Bulgaria! Your budget left is 3000.00'
        self.assertEqual(expected, result)

    def test_booking_status_if_not_booked_destinations_returns_string_message(self):
        expected = f'No bookings yet. Budget: 12000.00'
        result = self.trip.booking_status()

        self.assertEqual(expected, result)

    def test_booking_status_if_there_is_booking_destinations_returns_string(self):
        self.booked_destinations_paid_amounts = {"Bulgaria": 500}
        self.trip.book_a_trip("Bulgaria")
        self.assertEqual(self.booked_destinations_paid_amounts, {'Bulgaria': 500.0})
        result = self.trip.booking_status()
        expected = """Booked Destination: Bulgaria\nPaid Amount: 9000.00\nNumber of Travelers: 20\nBudget Left: 3000.00"""

        self.assertEqual(expected, result)

if __name__ == "__main__":
    main()