from django.contrib import admin
from django.urls import path
from crud_app import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path("", views.crud_list, name="crud-list",),
    path("crud-delete/<int:id>/", views.crud_delete, name="crud-delete",),
    path("crud-create", views.crud_create, name="crud-create",),
    path("crud-update/<int:id>/", views.crud_update, name="crud-update",),
]