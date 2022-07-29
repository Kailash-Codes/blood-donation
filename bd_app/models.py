from django.db import models

# Create your models here.

class Donor(models.Model):
    first_name = models.CharField(max_length=40, null=False)
    last_name = models.CharField(max_length=40, null=False)
    age = models.CharField(max_length=2,null=False)
    address = models.CharField(max_length=20)
    phone = models.CharField(max_length=10,null=False)
    blood_group = models.CharField(max_length=4, null=False,default='A+')

    def __str__(self):
        return_str = self.first_name+" "+self.last_name
        return return_str
