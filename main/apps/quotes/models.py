from django.db import models
from ..users.models import User

# Create your quotes models here.

class QuoteManager(models.Manager):
    def validate(self, quotes_form):
        errors = []
        if len(quotes_form['author']) < 3 :
            errors.append('Author name must be longer than 3 characters.')
        if len(quotes_form['quote']) < 10:
            errors.append('Quote must be longer than 10 characters. Try again.')
        return errors

        print(quotes_form)

    def create_quote(self, new_quote):
        posted_by = User.objects.get(id=new_quote['posted_by'])
        return self.create(
            author = new_quote['author'],
            quote = new_quote['quote'],
            posted_by = posted_by
        )

    def delete_quote(self, quote_id):
        quote = Quote.objects.get(id=quote_id)
        quote.delete()




class Quote(models.Model):
    author = models.CharField(max_length=255)
    quote = models.CharField(max_length=500)
    posted_by = models.ForeignKey(User, related_name= 'posted_by')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = QuoteManager()

    def __str__(self):
        return self.author
