from django.urls import path
from . import views

urlpatterns = [
    path('users/new', views.new_user, name='new_user'),
    path('users/<int:user_id>', views.user_detail, name='user_detail'),
    path('users/<int:user_id>/add-points', views.add_points, name='add_points'),
    path('users/<int:user_id>/deduct-points', views.deduct_points, name='deduct_points'),
]