from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    #path("<slug:slug>", views.book_detail, name="book-detail"), here slug is giving me an error
    path("<int:id>", views.book_detail, name="book-detail")
]

