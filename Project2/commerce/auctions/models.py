from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Bid(models.Model):
    current_bid = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    total_bids = models.PositiveSmallIntegerField(name='total_bids')
    duration = models.DateTimeField(name='end_date')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'${self.current_bid}'


class Comment(models.Model):
    text = models.TextField(name='comment_text')
    likes = models.PositiveIntegerField(name='comment_likes')
    posted = models.DateTimeField(name='time_posted')
    thread = models.BooleanField(name='is_thread', default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.text


class Listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    image = models.URLField(name='image_url')
    category = models.CharField(max_length=24)
    condition = models.CharField(max_length=5)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bid = models.ForeignKey(Bid, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'Listing: {self.title}'


class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)