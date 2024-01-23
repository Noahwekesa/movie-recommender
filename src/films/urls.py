from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path("register/", views.RegisterView.as_view(), name="register"),
    path("film/", views.FilmList.as_view(), name='film-list'),
]

htmx_urlpatterns = [
    path('check_username/', views.check_username, name='check-username'),
    path('add-film', views.add_film, name='add-film'),
    path('delete-film/<int:pk>/', views.delete_film, name='delete-film'),
]
urlpatterns += htmx_urlpatterns
