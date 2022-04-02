from django.urls import path
from .views import home, delete, mark_complete, mark_incomplete
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


app_name = "todo"

urlpatterns = [
    path("", home, name="home"),
    path('delete/<int:todo_id>/', delete, name='delete'),
    path('mark_complete/<int:todo_id>/', mark_complete, name="mark_complete"),
    path('mark_incomplete/<int:todo_id>/', mark_incomplete, name="mark_incomplete"),
]

urlpatterns += staticfiles_urlpatterns()