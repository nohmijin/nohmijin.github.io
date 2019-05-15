from django.db import models

# Create your models here.
class Post(models.Model):

    address2 = models.CharField(max_length=50)
    
    title = models.CharField(max_length=200)
    content = models.TextField()
    file = models.FileField(null=True)
    bill = models.IntegerField(default=0)
    pet = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True) #만든시간
    updated_at = models.DateTimeField(auto_now=True) #수정시간

    def __str__(self):
        return self.title

    def summary(self):
        return self.content[:10]