from django.db import models

class Profile(models.Model):
  name = models.CharField(max_length=100)
  permalink = models.CharField(max_length=30)
  
  def __unicode__(self):
    return self.name
  
class Testimonial(models.Model):
  profile = models.ForeignKey(Profile)
  name = models.CharField(max_length = 100)
  email = models.EmailField(max_length = 200)
  website = models.URLField()
  city = models.CharField(max_length=100)
  country = models.CharField(max_length=100)
  date = models.DateTimeField('date published')
  content = models.TextField()

  def __unicode__(self):
    return self.name

