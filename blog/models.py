from django.db import models
import datetime
# Create your models here.


class PostStatuses(models.Model):
    status = models.CharField(max_length=32, unique=True, default='draft')


class PostTypes(models.Model):
    type = models.CharField(max_length=32, unique=True, default='post')


class Post(models.Model):
    title = models.CharField(max_length=250)
    date = models.DateTimeField()
    post_modified = models.DateTimeField()
    author = models.CharField(max_length=100)
    text = models.TextField()
    url = models.CharField(max_length=250, unique=True,
                           null=False, db_index=True)
    post_type = models.ForeignKey(
        PostTypes, default=1, on_delete=models.DO_NOTHING)
    status = models.ForeignKey(
        PostStatuses, default=1, on_delete=models.DO_NOTHING)

    def save(self, *args, **kwargs):
        now = datetime.datetime.now()
        self.post_modified = now.strftime("%Y-%m-%d %H:%M:%S")
        super().save(*args, **kwargs)
