from unittest import TestCase, main

from project.student import Student


class TestStudent(TestCase):

    def setUp(self):
        self.student = Student("Ivan")
        self.student_with_courses = Student("Luke", {"math": ["x + y = z"]})

    def test_correct_init(self):
        self.assertEqual("Ivan", self.student.name)
        self.assertEqual("Luke", self.student_with_courses.name)


    def test_enroll_in_the_same_course_with_updated_notes(self):
        result = self.student_with_courses.enroll("math", ["2 + 2 = 4", "10 - 10 = 0"])
        string_message = "Course already added. Notes have been updated."
        self.assertEqual(string_message, result)

        self.assertEqual(["x + y = z", "2 + 2 = 4", "10 - 10 = 0"], self.student_with_courses.courses["math"])

    def test_enroll_in_new_courses_without_third_param_adds_notes_to_the_course(self):
        result = self.student.enroll("math", ["x + y = z"])

        self.assertEqual("Course and course notes have been added.", result)

        self.assertEqual({"math": ["x + y = z"]}, self.student.courses)

    def test_enroll_in_new_courses_with_third_param_Y_adds_to_the_notes(self):
        result = self.student.enroll("math", ["x + y = z"], "Y")

        self.assertEqual("Course and course notes have been added.", result)

        self.assertEqual({"math": ["x + y = z"]}, self.student.courses)

    def test_enroll_in_new_courses_with_THIRD_no_param_does_not_add_the_notes_to_the_course(self):
        result = self.student.enroll("math", ["x + y = z"], "n")

        self.assertEqual("Course has been added.", result)

        self.assertEqual({"math": []}, self.student.courses)

    def test_add_notes_to_non_existing_course_name_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student_with_courses.add_notes("history", ["History is repeating itself"])

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_add_notes_in_in_existing_courses(self):
        result = self.student_with_courses.add_notes("math", "1 + 2 = 3")

        self.assertEqual("Notes have been updated", result)

        self.assertEqual(["x + y = z", "1 + 2 = 3"], self.student_with_courses.courses["math"])

    def test_leave_course_cannot_remove_non_existing_course_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student_with_courses.leave_course("The Real World")

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

    def test_leave_course_removing_existing_course_name_from_courses(self):
        result = self.student_with_courses.leave_course("math")

        self.assertEqual("Course has been removed", result)

if __name__ == "__name__":
    main()