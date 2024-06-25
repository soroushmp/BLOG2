from django.contrib import admin

from .models import Post, Comment, CooperationRequest


class CommentData(admin.TabularInline):
    model = Comment
    filter = '__all__'
    extra = 0


class PostData(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at', 'published_at']
    inlines = [CommentData]


class FormData(admin.ModelAdmin):
    list_display = ['id', 'name']


admin.site.register(Post, PostData)
admin.site.register(CooperationRequest, FormData)
