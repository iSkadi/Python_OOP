from unittest import TestCase,main

from project.student import Student


class TestStudent(TestCase):

    name = "Pesho"

    def setUp(self) -> None:

        self.student1 = Student(self.name)

    def test_init_None(self):
        self.assertEqual(self.name, self.student1.name)
        self.assertEqual({}, self.student1.courses)

    def test_init_not_None(self):

        course_1 = {"Python": ["none1", "none 2"]}

        student1 = Student(self.name, course_1)

        self.assertEqual(self.name, self.student1.name)
        self.assertEqual(course_1, student1.courses)

    def test_enroll_Course_already_added(self):
        course_name = 'Python'
        course_1 = {course_name: ["note 1", "note 2"]}

        student1 = Student(self.name, course_1)

        result = student1.enroll(course_name, ["note 3", "note 4"])

        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual(["note 1", "note 2", "note 3", "note 4"], student1.courses[course_name])

    def test_enroll_course_notes_have_been_added(self):
        course_name = 'Python'
        course_notes = ["note 1", "note 2"]

        expect = "Course and course notes have been added."
        actual = self.student1.enroll(course_name, course_notes)

        self.assertEqual(expect, actual)
        self.assertTrue(course_name in self.student1.courses)
        self.assertEqual(course_notes, self.student1.courses[course_name])

    def test_enroll_course_notes_have_been_added_Y(self):
        course_name = 'course_name1'
        course_notes = ["note 1", "note 2"]

        expect = "Course and course notes have been added."
        actual = self.student1.enroll(course_name, course_notes, "Y")

        self.assertEqual(expect, actual)
        self.assertTrue(course_name in self.student1.courses)
        self.assertEqual(course_notes, self.student1.courses[course_name])

    def test_enroll_course_notes_have_been_added_no_notes(self):
        course_name = 'Python'
        course_notes = ["note 1", "note 2"]

        expect = "Course has been added."
        actual = self.student1.enroll(course_name, course_notes, "N")

        self.assertEqual(expect, actual)
        self.assertTrue(course_name in self.student1.courses)
        self.assertEqual([], self.student1.courses[course_name])


    def test_add_notes_ex(self):
        with self.assertRaises(Exception) as ex:
            self.student1.add_notes("p1", "NOte 3")
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_add_notes_working(self):
        course_name = "Python"
        courses = {course_name: ["note 1", "note 2"]}
        student = Student(self.name, courses)

        act = student.add_notes(course_name, "note 3")
        exe = "Notes have been updated"
        self.assertEqual(exe, act)
        self.assertEqual(["note 1", "note 2", "note 3"], student.courses[course_name])

    def test_leave_course_ex(self):
        self.student1.enroll("Python", [])

        with self.assertRaises(Exception) as ex:
            self.student1.leave_course("course")
        act = str(ex.exception)
        exe = "Cannot remove course. Course not found."
        self.assertEqual(exe, act)

    def test_leave_course_if_student_is_enroll(self):
        course_name = "Python"
        student = Student(self.name, {course_name: []})

        act = student.leave_course(course_name)
        exe = "Course has been removed"

        self.assertEqual(exe, act)
        self.assertTrue(course_name not in student.courses)



if __name__ == "__main__":
    main()










