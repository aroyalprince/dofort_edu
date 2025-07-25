from django.db import models


class Enquiry(models.Model):

    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    course = models.CharField(max_length=122)
    semester = models.CharField(max_length=122)
    complaint = models.CharField(max_length=200)
    date = models.DateField()

    def __str__(self):
        return f"Enquiry from {self.name}"

   
class Admission(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    contact = models.CharField(max_length=15)
    mail = models.EmailField()
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    occupation = models.CharField(max_length=100)
    guardian_name = models.CharField(max_length=100)
    guardian_occupation = models.CharField(max_length=100)
    guardian_contact = models.CharField(max_length=15)

    # Educational qualifications (3 rows)
    institute1 = models.CharField(max_length=200, blank=True, null=True)
    class_sem1 = models.CharField(max_length=100, blank=True, null=True)
    stream1 = models.CharField(max_length=100, blank=True, null=True)
    passing_year1 = models.CharField(max_length=10, blank=True, null=True)
    percentage1 = models.CharField(max_length=10, blank=True, null=True)

    institute2 = models.CharField(max_length=200, blank=True, null=True)
    class_sem2 = models.CharField(max_length=100, blank=True, null=True)
    stream2 = models.CharField(max_length=100, blank=True, null=True)
    passing_year2 = models.CharField(max_length=10, blank=True, null=True)
    percentage2 = models.CharField(max_length=10, blank=True, null=True)

    institute3 = models.CharField(max_length=200, blank=True, null=True)
    class_sem3 = models.CharField(max_length=100, blank=True, null=True)
    stream3 = models.CharField(max_length=100, blank=True, null=True)
    passing_year3 = models.CharField(max_length=10, blank=True, null=True)
    percentage3 = models.CharField(max_length=10, blank=True, null=True)

    subjects = models.CharField(max_length=200)
    references = models.CharField(max_length=200)
    refname = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name





class ContactMessage(models.Model):
    name = models.CharField(max_length=122)
    email = models.EmailField()
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"
