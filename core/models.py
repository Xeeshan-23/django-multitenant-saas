from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)
    status = models.CharField(
        max_length=20, 
        choices=[('Planning', 'Planning'), ('Active', 'Active'), ('Completed', 'Completed')],
        default='Active'
    )
    due_date = models.DateField()

    def __str__(self):
        return self.name

# notification model:
class Notification(models.Model):
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at'] # Shows newest notifications first

    def __str__(self):
        return self.message