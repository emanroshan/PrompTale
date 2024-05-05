from django.db import models
from account.models import Account

class Image(models.Model):
	image = models.ImageField(upload_to='images/')
	def __str__(self):
		return self.image.name
	
class TextEntry(models.Model):
	text = models.TextField()
	color = models.TextField(default='#ffffff')  # Default color is white
	font = models.TextField(default='Chalkduster')  # Default font is Arial

class StoryBook(models.Model):
	id = models.AutoField(primary_key=True)
	username = models.CharField(max_length=100)
	title = models.CharField(max_length=100)
	description = models.TextField()
	text = models.ManyToManyField(TextEntry, blank=True)
	images = models.ManyToManyField(Image, blank=True)
	is_public = models.BooleanField(default=False)
	rating = models.FloatField(default=0.0)
	no_of_ratings = models.IntegerField(default=0)

	def __str__(self):
		return self.title
	
	def delete_book(self):
		self.delete()

	def set_public_status(self, is_public):
		self.is_public = is_public
		self.save()

	def add_rating(self, rating):
		current_rating = self.rating
		total = self.no_of_ratings
		current_rating *= total
		current_rating += rating
		current_rating /= (total + 1)
		self.rating = current_rating
		self.no_of_ratings = total + 1
		self.save()

