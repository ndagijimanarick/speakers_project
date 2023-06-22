from django.urls import path,include
from . import views

urlpatterns = [
    path('speak',views.speak),
    path('show',views.show),
    path('edit/<int:id>',views.edit),
    path('update/<int:id>',views.update),
    path('delete/<int:id',views.delet)
]