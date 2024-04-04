from django.urls import path, include

from . import views

app_name = "quotes"

urlpatterns = [
    path("", views.main, name="root"),
    path("<int:page>", views.main, name="root_paginate"),
    path('users/', include('users.urls')),
    path('author/<str:author>', views.author, name='author'), 
    path('tag/<str:tag>', views.tag, name='tag'),  
    path('tag/<str:tag>/<int:page>', views.tag, name='tag_paginate'),
]
