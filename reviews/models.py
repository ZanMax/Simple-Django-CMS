from django.db import models

# Create your models here.


class ReviewsStatuses(models.Model):
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.status

    class Meta:
        verbose_name_plural = "ReviewsStatuses"


class Reviews(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField()
    rating = models.IntegerField(default=5)
    text = models.TextField()
    status = models.ForeignKey(
        ReviewsStatuses, default=1, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'self.name - self.rating'

    class Meta:
        verbose_name_plural = "Reviews"
