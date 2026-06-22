from django.db import models

# Create your models here.

class Users(models.Model):
    sr_no = models.IntegerField()
    name = models.CharField(max_length=100)
    certificate_no = models.CharField(max_length=20)
    is_editable = models.IntegerField(null=True, blank=True)
    is_completed = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    
class Users_M(models.Model):
    sr_no = models.IntegerField()
    name = models.CharField(max_length=100)
    certificate_no = models.CharField(max_length=20)
    is_editable = models.IntegerField(null=True, blank=True)
    is_completed = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.name