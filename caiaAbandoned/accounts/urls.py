from django.urls import path, include
from caiaAbandoned.accounts import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.SignInView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('profile/<int:pk>/', include([
        path('', views.show_profile_details, name='profile-details'),
        path('edit/', views.edit_profile, name='profile-edit'),
        path('delete/', views.delete_profile, name='profile-delete'),
    ]))
]
