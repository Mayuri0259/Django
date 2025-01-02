
from django.urls import path

# The dot (.) represents the current package or module. 
# So, from . import views means "import the views module 
# from the current package or directory."
from . import views


urlpatterns = [
    #path("january", views.january),
    #path("february", views.february),
    path("", views.index, name="index"),  # /challenges/
    path("<int:month>", views.monthly_challenge_by_number),
    #<str:month> tells Django that the concrete value entered here should be treated as a string
    path("<str:month>", views.monthly_challenge, name="month-challenge") #<month> is used for dynamic path 
    
]

