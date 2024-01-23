from django.views.decorators.http import require_http_methods
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView, login_required
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView, TemplateView
from django.contrib.auth import get_user_model, logout
from .models import Film


from .forms import RegisterForm


class IndexView(TemplateView):
    template_name = 'index.html'


class Login(LoginView):
    template_name = 'registration/login.html'


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()  # save the user
        return super().form_valid(form)


def logout_view(request):
    logout(request)
    return redirect('login')


def check_username(request):
    username = request.POST.get('username')
    if get_user_model().objects.filter(username=username).exists():
        return HttpResponse("<div id='username-error' class='text-danger'>This username already exists</div>")
    else:
        return HttpResponse("<div id='username-error' class='text-success'>This username is available </div>")


class FilmList(LoginRequiredMixin, ListView):
    template_name = 'AddFilms.html'
    model = Film
    context_object_name = 'films'

    def get_queryset(self):
        user = self.request.user
        return user.films.all()


def add_film(request):
    name = request.POST.get('filmname')
    # create an isinstance of the film
    film = Film.objects.create(name=name)
    # add the film to the users list
    request.user.films.add(film)
    # return template with all users films
    films = request.user.films.all()
    context = {
        'films': films
    }
    return render(request, 'partials/film-list.html', context)


@login_required
@require_http_methods(["DELETE"])
def delete_film(request, pk):
    """
function to delete film from user's list
    """
    request.user.films.remove(pk)
    # return the template
    films = request.user.films.all()

    context = {
        'films': films
    }
    return render(request, 'partials/film-list.html', context)
