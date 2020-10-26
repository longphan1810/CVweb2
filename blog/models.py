from django.db import models
from django.conf import settings
from django.utils.text import slugify
from six import python_2_unicode_compatible
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
# Create your models here.
class topic(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    showname = models.CharField(max_length=255, null= True)

    def __str__(self):
        return self.name

class article(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique= True, blank=True, editable=True, null = True)
    topic = models.ForeignKey(topic, on_delete=models.CASCADE)
    author = models.CharField(max_length=255)
    opening = models.TextField()
    body = RichTextUploadingField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null = True)
    view = models.IntegerField(default=0, null=True)
    

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(article, self).save(*args, **kwargs)
    

class Comment(models.Model):
    post = models.ForeignKey(article, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)



    