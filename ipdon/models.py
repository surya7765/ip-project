from django.db import models

# Create your models here.
class Event(models.Model):
    img_url = models.CharField(max_length = 200)
    event_name = models.CharField(max_length = 20)
    event_desc = models.CharField(max_length = 500)

    def __str__(self):
        return str(self.event_name)


class Contest(models.Model):
    venue = models.CharField(max_length = 100)
    date = models.DateTimeField()
    prize = models.IntegerField()
    contest_url = models.CharField(max_length = 500)
    title = models.CharField(max_length = 20)
    image = models.CharField(max_length = 500)
    running = models.BooleanField(default = False)
    upcoming = models.BooleanField(default = False)
    past = models.BooleanField(default = False)

    def __str__(self):
        return str(self.title)
