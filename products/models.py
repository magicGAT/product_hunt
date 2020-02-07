from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# PRODUCT CLASS

# COMPONENTS

# title
# url
# date published
# total votes
# image
# icon
# body

# hunter

class Product(models.Model):
	name = models.CharField(max_length=200)
	url = models.CharField(max_length=150)
	pub_date = models.DateField(null=True)
	vote_quant = models.IntegerField(default=1)
	image = models.ImageField(upload_to="images/")
	icon = models.ImageField(upload_to="images/")
	description = models.TextField()
	hunter = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

	def summary(self):
		return self.description[:100 + "..."]

	def pub_date_pretty(self):
		return self.date.strftime('%b %e %Y')
