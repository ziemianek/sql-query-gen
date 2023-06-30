from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from generate.models import History


def home_view(request):
    return render(request, "home_view.html")


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class HistoryView(LoginRequiredMixin, ListView):
    model = History
    template_name = 'history.html'
    paginate_by = 15

    def get_queryset(self):
        return History.objects.filter(
            user = self.request.user
        ).all()
