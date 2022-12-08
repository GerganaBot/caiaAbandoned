from django.urls import path, include
from caiaAbandoned.accounts import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.SignInView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('profile/<int:pk>/', include([
        path('', views.UserDetailsView.as_view(), name='profile-details'),
        path('edit/', views.UserEditView.as_view(), name='profile-edit'),
        path('delete/', views.UserDeleteView.as_view(), name='profile-delete'),
    ]))
]
