from django.db import models


# -------------------------
# Custom Manager
# -------------------------
class StudentManager(models.Manager):

    def adults(self):
        return self.filter(age__gte=18)


# -------------------------
# Course Model
# -------------------------
class Course(models.Model):
    name = models.CharField(max_length=100)
    duration = models.IntegerField()

    def __str__(self):
        return self.name


# -------------------------
# Student Model
# -------------------------
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()

    # Many-to-One
    # Many students can belong to one course
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="students"
    )

    # Many-to-Many
    # A student can take multiple courses
    enrolled_courses = models.ManyToManyField(
        Course,
        related_name="enrolled_students",
        blank=True
    )

    # Custom manager
    objects = StudentManager()

    # Model method
    def is_adult(self):
        return self.age >= 18

    # Model method
    def greeting(self):
        return f"Hello, I am {self.name}"

    def __str__(self):
        return self.name


# -------------------------
# Student Profile
# -------------------------
class StudentProfile(models.Model):

    # One-to-One
    # One student has one profile
    student = models.OneToOneField(
        Student,
        on_delete=models.CASCADE,
        related_name="profile"
    )

    phone = models.CharField(max_length=15)
    city = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.student.name} Profile"