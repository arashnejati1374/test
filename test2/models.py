from django.db import models

class test1(models.Model):
    name=models.CharField(max_length=500)
    l_name=models.CharField(max_length=500)
    age=models.IntegerField()

    def __str__(self):
        return self.name

