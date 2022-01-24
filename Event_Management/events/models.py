from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class events(models.Model):
    event_id = models.AutoField
    event_name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    venue = models.CharField(max_length=120)
    from_Date = models.DateTimeField()
    to_Date = models.DateTimeField()
    Deadline = models.DateTimeField()
    host_email = models.CharField(max_length=50)
    host_password = models.CharField(max_length=50)

    def __str__(self):
        return self.event_name

class participate(models.Model):
    class reg_type(models.TextChoices):
        Individual = 'INDIVIDUAL',_('Individual') 
        Group = 'GROUP',_('Group')

    name = models.CharField(max_length=50)
    contact_no = models.CharField(max_length=18)
    email_id = models.CharField(max_length=50)
    registeration_type = models.CharField(max_length=10,choices=reg_type.choices)
    event = models.ForeignKey(events,on_delete=models.CASCADE)
    no_of_people = models.IntegerField()

    def __str__(self) -> str:
        return self.name


