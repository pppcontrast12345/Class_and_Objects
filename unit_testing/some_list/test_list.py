from unittest import TestCase, main

#from some_list.original_list import IntegerList


class TestIntegerList(TestCase):

    def setUp(self):
        self.i_list = IntegerList(5.5, 1, 2, 3, "hello")

    def test_correct_init_ignore_not_int_values(self):
        self.assertEqual([1, 2, 3], self.i_list.get_data())

    def test_element_is_not_int_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.i_list.add(5.5)

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_element_that_is_integer_and_append_to_the_list(self):
        expected_list = self.i_list.get_data() + [7]
        self.i_list.add(7)

        self.assertEqual(expected_list, self.i_list.get_data())

    def test_remove_index_index_is_bigger_than_len_of_list_raise_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.i_list.remove_index(1000)
        self.assertEqual("Index is out of range", str(ie.exception))

    def test_remove_index_with_valid_index(self):
        self.i_list.remove_index(0)
        self.assertEqual([2, 3], self.i_list.get_data())

    def test_get_index_out_of_range_raise_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.i_list.get(1000)

        self.assertEqual("Index is out of range", str(ie.exception))


    def test_get_valid_index_returns_value_of_index(self):
        result = self.i_list.get(1)
        self.assertEqual(2, result)

    def test_insert_index_out_of_range_raise_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.i_list.insert(1000, 3)
        self.assertEqual("Index is out of range", str(ie.exception))

    def test_insert_element_is_not_integer_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.i_list.insert(1, 2.5)

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_insert_valid_index_and_valid_int_el(self):
        expected_list = self.i_list.get_data().copy()

        expected_list.insert(1, 5)
        self.i_list.insert(1, 5)

        self.assertEqual(expected_list, self.i_list.get_data())

    def test_get_biggest_element_and_returns_it(self):
        result = self.i_list.get_biggest()
        self.assertEqual(3, result)

    def test_get_index_and_returns_it(self):
        result = self.i_list.get_index(2)
        self.assertEqual(1, result)

if __name__ == "__main__":
    main()