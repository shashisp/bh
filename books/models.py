from django.db import models
from django.contrib.auth.models import User


from django.db.models import Count

class BookVoteCountManager(models.Manager):
    
    def get_query_set(self):
        return super(BookVoteCountManager, self).get_query_set().annotate(
            votes=Count('vote')).order_by('-votes')


class Book(models.Model):
    title = models.CharField("Book Title", max_length=100)
    submitter = models.ForeignKey(User)
    submitted_on = models.DateTimeField(auto_now_add=True)
    rank_score = models.FloatField(default=0.0)
    isbn = models.CharField("ISBN", max_length=250, blank=True)
    description = models.TextField(blank=True)
    with_votes = BookVoteCountManager()
    objects = models.Manager()

    def __unicode__(self):
        return self.title

class Vote(models.Model):
    voter = models.ForeignKey(User)
    link = models.ForeignKey(Book)

    def __unicode__(self):
        return "%s upvoted %s" % (self.voter.username, self.link.title)


class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True, null=True)
    bio = models.CharField(max_length=150)

    def __unicode__(self):
        return self.user.first_name


class Collection(models.Model):
    title = models.CharField(max_length=150)
    created_by = models.ForeignKey(UserProfile)
    books = models.ManyToManyField(Book)

    def __uniocode__(self):
        return self.title