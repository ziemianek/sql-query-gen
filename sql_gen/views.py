from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.urls import reverse_lazy
from generate.models import History


def home_view(request):
    return render(request, "home_view.html")


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        return response

    def get_success_url(self):
        # Get the 'next' URL parameter from the request's GET data
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        else:
            return reverse_lazy('home-view')  # Default URL if 'next' parameter is not provided




class HistoryView(LoginRequiredMixin, ListView):
    model = History
    template_name = 'history.html'

    def get_queryset(self):
        return History.objects.filter(
            user = self.request.user
        ).all()
