from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Wing(models.Model):
  name = models.CharField(max_length=200)

class UserProfile(models.Model):
  user = models.OneToOneField(User)

  #wing = models.ForeignKey(Wing)
  wing = models.TextField() # wing name
  zs = models.TextField() # sleep data

  def __unicode__(self):
    return self.user.username
