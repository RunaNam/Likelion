from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/detail/<int:blog_id>', views.detail, name="detail"),
    path('blog/create', views.create, name='create'),

]
