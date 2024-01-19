from django.db import models


class Feedback(models.Model):
    student_number = models.CharField(max_length=25)
    registration_number = models.CharField(max_length=25)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length = 256)
    dob = models.DateField()
    address = models.CharField(max_length=10)
    message = models.TextField()

    def _str_(self):
        return f"Student: {self.name} \n Message: {self.message}"

    def _repr_(self):
        return f"Student: {self.name} \n Message: {self.message}"


# class Users(models.Model):
    
#     email = models.CharField(max_length=255, unique=True)
#     password = models.CharField(max_length=255)
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)

#     def __str__(self):
#         return self.email