from django.db import models

# Create your models here.
class UserQuerries(models.Model):
    user_query = models.CharField(max_length=200)

    def __str__(self):
        return(UserQuerries.user_query)
