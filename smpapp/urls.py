from .views import *
from django.urls import path

urlpatterns = [
    # path('', home),
    # path('student/',student_post),
    # path('student/<id>', update_post),
    # path('student-delete/<id>/', delete_post)
    path('student/',Facebookapi.as_view()),
    path('register/',Register_user.as_view()),
]