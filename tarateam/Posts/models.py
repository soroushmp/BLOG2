from django.db import models
from ckeditor.fields import RichTextField
from django.core.validators import EmailValidator
from django_jalali.db import models as jmodels


class post(models.Model):
    objects = jmodels.jManager()
    title = models.CharField(max_length=150 , blank=False)
    poster_photo = models.ImageField(upload_to='post_images/' , blank=False)
    preview_text = models.CharField(max_length=130 , blank=False , default='متن پیش فرض خود را وارد کنید')
    body = RichTextField()
    created_at = jmodels.jDateTimeField(auto_now_add=True)
    published_at = jmodels.jDateTimeField(blank=True , auto_now=True)
    def __str__(self):
        return "%s, %s" % (self.title, self.published_at)
    
   

    
    
class Comment(models.Model):
    post = models.ForeignKey(post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    text = models.TextField()
    email = models.EmailField()

    

    
class CooperationRequest(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=12)
    email_address = models.EmailField()
    description = models.TextField(blank=False)
    date_brd = models.CharField(max_length=40 , blank=False)

  