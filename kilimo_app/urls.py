from . import views
from django.urls  import path, include

urlpatterns = [
    path('', views.index, name='index'),
    path('students/', views.students, name='students'),
    path('single_class/<id>', views.single_class, name='single_class'),
    

]