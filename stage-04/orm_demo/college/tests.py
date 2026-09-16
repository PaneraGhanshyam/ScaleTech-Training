from django.test import TestCase

from .models import Course, Student, StudentProfile


class CollegeModelTests(TestCase):

    def setUp(self):
        self.course = Course.objects.create(
            name="Computer Science",
            duration=4
        )

        self.python_course = Course.objects.create(
            name="Python",
            duration=1
        )

        self.student = Student.objects.create(
            name="Ghanshyam",
            email="ghanshyam@example.com",
            age=22,
            course=self.course
        )

    # -------------------------
    # Model creation
    # -------------------------
    def test_student_creation(self):
        self.assertEqual(self.student.name, "Ghanshyam")
        self.assertEqual(self.student.age, 22)

    # -------------------------
    # Model method
    # -------------------------
    def test_is_adult(self):
        self.assertTrue(self.student.is_adult())

    def test_greeting(self):
        self.assertEqual(
            self.student.greeting(),
            "Hello, I am Ghanshyam"
        )

    # -------------------------
    # Custom Manager
    # -------------------------
    def test_adults_manager(self):
        adult_students = Student.objects.adults()

        self.assertIn(
            self.student,
            adult_students
        )

    # -------------------------
    # Many-to-One
    # -------------------------
    def test_many_to_one_relationship(self):
        self.assertEqual(
            self.student.course,
            self.course
        )

        self.assertIn(
            self.student,
            self.course.students.all()
        )

    # -------------------------
    # One-to-One
    # -------------------------
    def test_one_to_one_relationship(self):
        profile = StudentProfile.objects.create(
            student=self.student,
            phone="9876543210",
            city="Rajkot"
        )

        self.assertEqual(
            self.student.profile,
            profile
        )

        self.assertEqual(
            profile.student,
            self.student
        )

    # -------------------------
    # Many-to-Many
    # -------------------------
    def test_many_to_many_relationship(self):
        self.student.enrolled_courses.add(
            self.course,
            self.python_course
        )

        self.assertEqual(
            self.student.enrolled_courses.count(),
            2
        )

        self.assertIn(
            self.python_course,
            self.student.enrolled_courses.all()
        )

        self.assertIn(
            self.student,
            self.python_course.enrolled_students.all()
        )