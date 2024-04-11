from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15)
   

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task_detail = models.TextField()
    TASK_CHOICES = (
        ('Pending', 'Pending'),
        ('Done', 'Done')
    )
    task_type = models.CharField(max_length=10, choices=TASK_CHOICES)


