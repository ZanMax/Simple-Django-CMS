from shutil import unregister_unpack_format
from tabnanny import verbose
from django.db import models
import datetime
from ckeditor.fields import RichTextField
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.


class PostStatuses(models.Model):
    status = models.CharField(max_length=32, unique=True, default='draft')

    def __str__(self):
        return self.status

    class Meta:
        verbose_name_plural = "Statuses"


class PostTypes(models.Model):
    type = models.CharField(max_length=32, unique=True, default='post')

    def __str__(self):
        return self.type

    class Meta:
        verbose_name_plural = "Types"


class Tags(models.Model):
    tag = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.tag

    class Meta:
        verbose_name_plural = "Tags"


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    articles_count = models.IntegerField(validators=[MinValueValidator(1)])
    experience = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(50)])
    age = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(90)])
    education = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    expertise = models.CharField(max_length=255)
    about = RichTextField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Post(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateTimeField()
    post_modified = models.DateTimeField()
    author = models.ForeignKey(
        Author, on_delete=models.DO_NOTHING, null=True, related_name="posts")
    text = RichTextField()
    url = models.SlugField(max_length=255, unique=True,
                           null=False, db_index=True)
    post_type = models.ForeignKey(
        PostTypes, default=1, on_delete=models.DO_NOTHING)
    status = models.ForeignKey(
        PostStatuses, default=1, on_delete=models.DO_NOTHING)
    likes = models.IntegerField(default=0)
    read_time = models.IntegerField(default=0)
    tags = models.ManyToManyField(Tags)
    comment_allowed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        now = datetime.datetime.now()
        self.post_modified = now.strftime("%Y-%m-%d %H:%M:%S")
        self.read_time = int(round((len(self.text) / 200), 0))
        super().save(*args, **kwargs)

    class Meta:
        get_latest_by = ['date']
        ordering = ['-date']


class Comment(models.Model):
    user_name = models.CharField(max_length=80)
    user_email = models.CharField(max_length=120)
    user_ip = models.CharField(max_length=120)
    comment = models.TextField()
    post = models.ForeignKey(
        Post, on_delete=models.DO_NOTHING, null=True, related_name="comments")
    date = models.DateTimeField()
    approved = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.user_ip = "0.0.0.0"
        now = datetime.datetime.now()
        self.date = now.strftime("%Y-%m-%d %H:%M:%S")
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.user_name} - {self.user_email}'
