from djongo import models
from bson import ObjectId
# Create your models here.

class Contacts(models.Model):
    _id = models.ObjectIdField(auto_created=True, primary_key=True, default=ObjectId)
    name = models.CharField(max_length=400)
    email = models.EmailField(max_length=400, unique=True)
    message = models.TextField(default=None)
    created_at = models.DateTimeField(auto_now_add=True)

class Projects(models.Model):
    _id = models.ObjectIdField(auto_created=True, primary_key=True, default=ObjectId)
    title = models.CharField(max_length=200)
    content = models.TextField(default=None)
    imageUrl = models.TextField(default='https://images.unsplash.com/photo-1632831291403-dbe6cb9df2d3?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D')
    created_at = models.DateTimeField(auto_now_add=True)

class Posts(models.Model):
    _id = models.ObjectIdField(auto_created=True, primary_key=True, default=ObjectId)
    title = models.CharField(max_length=200)
    logoClass = models.TextField(default=None)
    description = models.TextField(default=None)
    githubLink = models.TextField(default=None)


class Hobbies(models.Model):
    _id = models.ObjectIdField(auto_created=True, primary_key=True, default=ObjectId)
    title = models.CharField(max_length=200)
    description = models.TextField(default=None)
    headLine = models.CharField(max_length=200)
    imageUrl = models.TextField(default='https://images.unsplash.com/photo-1632831291403-dbe6cb9df2d3?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D')