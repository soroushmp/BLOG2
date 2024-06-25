from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

# Wrong Name For Application
from Posts import views as Posts

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Posts.homepage_render, name='homepage'),
    path('blogs/', Posts.blogs_render, name='blogs'),
    path('blog/<int:pk>', Posts.blog_render, name='blog'),
    path('contact-us/', Posts.cooperation_request_page, name='cooperation_request')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
