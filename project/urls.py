
from django.contrib import admin
from django.urls import path
from home.views import home, delete, todo_edit

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home),
    path("delete/<int:id>/", delete),
    path("edit/<int:id>/", todo_edit)
]
