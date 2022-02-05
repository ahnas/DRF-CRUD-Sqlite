from pyexpat import model
from django.db import models

# Create your models here.


class Employee(models.Model):
    checked = models.BooleanField(default=True)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    age = models.IntegerField()
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.name)



# Create / Insert / Add = POST
# Retreive / Fetch = GET
# Update / Edit = PUT
# Delete / Remove = DELETE