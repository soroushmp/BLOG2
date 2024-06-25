from django.contrib import admin
from .models import post , Comment ,  CooperationRequest


class CommentData(admin.TabularInline):
    model = Comment
    filter = '__all__'
    extra=0

class postdata(admin.ModelAdmin):
    list_display = ['id', 'title' , 'created_at' , 'published_at']
    inlines = [CommentData]
   
class form_data(admin.ModelAdmin) :
    list_display = ['id' , 'name']
    
admin.site.register(post , postdata)
admin.site.register(CooperationRequest , form_data)
