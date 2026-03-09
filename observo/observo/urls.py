from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),

    path("animals/", views.animal_list, name="animal_list"),
    path("animals/<int:pk>/", views.animal_detail, name="animal_detail"),
    path("new_animal/", views.new_animal, name="new_animal"),
    path("delete_animal/<int:pk>/", views.delete_animal, name="delete_animal"),
    path("change_animal/<int:pk>/", views.change_animal, name="change_animal"),

    path("observs/", views.observ_list, name="observ_list"),
    path("observs/<int:pk>/", views.observ_detail, name="observ_detail"),
    path("new_observ/", views.observ_create, name="observ_create"),
    path("delete_observ/<int:n>/", views.observ_delete, name="observ_delete"),
    path("change_observ/<int:pk>/", views.change_observ, name="change_observ"),
     path("favorites/", views.favorite_list, name="favorite_list"),

    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("signup/", views.signup, name="signup"),
]
