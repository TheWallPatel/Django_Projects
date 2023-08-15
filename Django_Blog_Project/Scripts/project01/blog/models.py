# for creat models
from django.db import models
# adding curr time zone from running system.
from django.utils import timezone
# for allowing dictinct user to create posts
from django.contrib.auth.models import User

# Create your models here.
# each class is table in database
class Posts(models.Model):
    # creating Attributes ot feilds in table in DB.
    # creatinf title feild in table of char type with length 100.
    title = models.CharField(max_length=100)
    content = models.TextField()
    # creating Datetime field with curr time feature with default=timezone.now
    # now is function but we dont want to run it so remove () from timezone.now()
    date_posted = models.DateTimeField(default=timezone.now)
    # allowing user to create multiple posts from one user id
    # we need to include auth.models
    # here we tell django when user is deleted their post also get deleted
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title