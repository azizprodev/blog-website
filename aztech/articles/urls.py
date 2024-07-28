from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name="index"),
    path('<int:id>/', views.article, name='article'),
]
