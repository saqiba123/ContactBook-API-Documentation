from django.db import models

# Create your models here.
class Contacts(models.Model):
    contact_id  = models.IntegerField(primary_key=True)
    contact_name = models.CharField(max_length=40)
    contact_email = models.EmailField()
    contact_address = models.CharField(max_length=200)
    contact_phone = models.IntegerField(default=0)  # Set default value here

    def __str__(self) -> str:
        return self.contact_name
