from django.db import models
import datetime
from ckeditor.fields import RichTextField
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class PostStatuses(models.Model):
    status = models.CharField(max_length=32, unique=True, default='draft')

    def __str__(self):
        return self.status


class PostTypes(models.Model):
    type = models.CharField(max_length=32, unique=True, default='post')

    def __str__(self):
        return self.type


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    articles_count = models.IntegerField(validators=[MinValueValidator(1)])
    experience = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(50)])
    age = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(90)])
    education = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    expertise = models.CharField(max_length=255)
    about = RichTextField()

    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    def __str__(self):
        return self.full_name

class Post(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateTimeField()
    post_modified = models.DateTimeField()
    author = models.CharField(max_length=100)
    text = RichTextField()
    url = models.SlugField(max_length=255, unique=True,
                           null=False, db_index=True)
    post_type = models.ForeignKey(
        PostTypes, default=1, on_delete=models.DO_NOTHING)
    status = models.ForeignKey(
        PostStatuses, default=1, on_delete=models.DO_NOTHING)

    def save(self, *args, **kwargs):
        now = datetime.datetime.now()
        self.post_modified = now.strftime("%Y-%m-%d %H:%M:%S")
        super().save(*args, **kwargs)
