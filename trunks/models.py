from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Trunk_OTN(models.Model):
	Author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	Trunk = models.CharField(max_length=20)
	Detail = models.TextField()
	Created_date = models.DateTimeField(default=timezone.now)
	Published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.Published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.Trunk

class Trunk_DWDM(models.Model):
	Author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	Trunk = models.CharField(max_length=20)
	Detail = models.TextField()
	Created_date = models.DateTimeField(default=timezone.now)
	Published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.Published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.Trunk

class Trunk_SDH(models.Model):
	Author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	Trunk = models.CharField(max_length=20)
	Detail = models.TextField()
	Created_date = models.DateTimeField(default=timezone.now)
	Published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.Published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.Trunk