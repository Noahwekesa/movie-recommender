from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path("register/", views.RegisterView.as_view(), name="register"),
    path("film/", views.AddFilms, name='add-film'),
]

htmx_urlpatterns = [
    path('check_username/', views.check_username, name='check-username'),
]
urlpatterns += htmx_urlpatterns
