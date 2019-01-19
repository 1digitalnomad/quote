from django.db import models
from ..quotes.models import Quote

# Create your models here.
class LikeManager(models.Manager):
    def add_like(self, form):
        quotes = Quote.objects.get(id=form['likes']).fav_quote.likes
        post_like = self.get(id=id)
        for likes in quotes:
            if likes < 0:
                post_like.likes += 1
                post_like.save()
            else: 
                if likes == 1:
                    break



#add like to count. if user has liked it once  they can not like it again


class Like(models.Model):
    likes = models.IntegerField()
    quote = models.ForeignKey(Quote, related_name='fav_quote')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = LikeManager()
