"""from django.urls import path
from .views import ReturnTrue, ReturnFalse

urlpatterns = [
    path('return-true/', ReturnTrue.as_view(), name='return_true'),
    path('return-false/', ReturnFalse.as_view(), name='return_false'),
]"""



"""from django.urls import path
from .views import GetExample, PostExample, PutExample, DeleteExample

urlpatterns = [
    path('get/', GetExample.as_view(), name='get-example'),
    path('post/', PostExample.as_view(), name='post-example'),
    path('put/', PutExample.as_view(), name='put-example'),
    path('delete/', DeleteExample.as_view(), name='delete-example'),
]
"""

from django.urls import path
from .views import Example

urlpatterns = [
    path('get/', Example.as_view(), name='get-example'),
    path('post/', Example.as_view(), name='post-example'),
    path('put/', Example.as_view(), name='put-example'),
    path('delete/', Example.as_view(), name='delete-example'),
]
