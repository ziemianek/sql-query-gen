from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import PromptForm
from utils import generate_sql_query


@login_required  # (login_url='/signup/')
def generate_view(request):
    prompt = ""
    response = ""

    if request.method == "POST":
        form = PromptForm(request.POST)
        if form.is_valid():
            prompt = form.cleaned_data['prompt']
            response = generate_sql_query.generate_sql_query(prompt)
    else:
        form = PromptForm()

    context = {
        'form' : form,
        'prompt' : prompt,
        'response' : response,
    }

    return render(request, "generate/generate.html", context=context)
