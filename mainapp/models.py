from django.db import models

# Create your models here.

gender_choice = (('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other'))

class School(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    def __str__(self):
        return self.name

class College(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)


class SchoolData(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True, blank=True)
    student = models.CharField(max_length=255, blank=True, null=True)
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=255, blank=True, null=True, choices=gender_choice)
    aadhar = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    residential_address = models.CharField(max_length=255, blank=True, null=True)
    father_name = models.CharField(max_length=255, blank=True, null=True)
    mother_name = models.CharField(max_length=255, blank=True, null=True)
    father_occupation = models.CharField(max_length=255, blank=True, null=True)
    mother_occupation = models.CharField(max_length=255, blank=True, null=True)
    family_annual_income = models.CharField(max_length=255, blank=True, null=True)
    contact = models.CharField(max_length=255, blank=True, null=True)
    high_school_percentage = models.CharField(max_length=255, blank=True, null=True)
    intermidiate_percentage = models.CharField(max_length=255, blank=True, null=True)

    

    

    
class CollegeData(models.Model):
    college = models.ForeignKey(College, on_delete=models.CASCADE, null=True, blank=True)
    student = models.CharField(max_length=255, blank=True, null=True)
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=255, blank=True, null=True)
    aadhar = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
