from django.contrib import admin
from django.urls import path

from blog.views import frontpage, post_detail, about, contact, privacy, games

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('admin/', admin.site.urls),
    path('about/',about, name='about'), 
    path('contact/',contact, name='contact'), 
    path('privacy/',privacy, name='privacy'),  
    path('games/',games, name='games'),    
    path('<slug:slug>/', post_detail, name='post_detail'),
  
]
