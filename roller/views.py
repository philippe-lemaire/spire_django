from signal import SIGKILL
from django.shortcuts import render
from django.http import HttpResponse
from .forms import RollForm
from .game_logic import roll

# Create your views here.


def index(request):
    # if it's a post request, process the form data
    if request.method == "POST":
        # create a form instance and populate it
        form = RollForm(request.POST)
        # check weather the form is valid
        if form.is_valid():
            # retrieve the values from it
            skill = form.cleaned_data["skill"]
            domain = form.cleaned_data["domain"]
            mastery = form.cleaned_data["mastery"]
            equipment = form.cleaned_data["equipment"]
            difficulty = form.cleaned_data["difficulty"]
            dice = 1 + sum((skill, domain, mastery, equipment))
            # call the game logic function
            pool, res = roll(dice, difficulty)
            # build the context
            context = {
                "form": form,
                "pool": pool,
                "res": res,
            }

    else:
        context = {"form": RollForm()}
    return render(request, "roller/roller.html", context)
