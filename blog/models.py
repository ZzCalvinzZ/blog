from django.db import models

class Article(models.Model):
  """Article Model"""
  title = models.CharField(max_length=255, unique=True)
  slug = models.SlugField(max_length=100, unique=True)
  date = models.DateField(db_index=True, auto_now_add=True)
  author = models.CharField(max_length=100)
  post = models.TextField()
  category = models.ForeignKey('blog.Category')

class Category(models.Model):
  """Category Model"""
  title = models.CharField(max_length=100, db_index=True)
  slug = models.SlugField(max_length=100, db_index=True)