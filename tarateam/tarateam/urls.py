from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from Posts.views import post_def, home , blog , CooperationRequest_page ,save
urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , home , name='home'),
    path('blog/' , blog , name='blog'),
    path('blog/<int:post_id>/', post_def , name='post_def'),
    path('save/' ,save, name='save' ),
    path('Contact_us/' ,CooperationRequest_page , name='form' )
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
