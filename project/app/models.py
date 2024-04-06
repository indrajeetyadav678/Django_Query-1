from django.db import models

# Create your models here.
class StudentModel(models.Model):
    stu_name=models.CharField(max_length=500)
    stu_address=models.CharField(max_length=500)
    

    class Meta:
        db_table="Student"
        verbose_name_plural="Student"

    def __str__(self):                     
        return self.stu_name
