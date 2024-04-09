from django.urls import path

from . import views


app_name = "users"
urlpatterns = [
    path("", views.index, name ="index"),
    path("login", views.login_view, name="login"),
    path("signup", views.signup_view, name="signup"),
    path("logout", views.logout_view, name="logout"),
    path("reviews", views.reviews, name="reviews"),
    path('profile/', views.user_profile, name='user-profile'),
    # Add URL patterns for editing and deleting pets
    path('edit-pet/<int:pet_id>/', views.user_profile, name='edit-pet'),
    path('delete-pet/<int:pet_id>/', views.user_profile, name='delete-pet'),
]

