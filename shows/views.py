from django.shortcuts import render, redirect
from .models import Show


def root_redirect(request):
    return redirect("/shows")


def index(request):
    context = {"all_shows": Show.objects.all()}
    return render(request, "table.html", context)


def add_new(request):
    return render(request, "form.html")


def create(request):
    if request.method == "POST":
        new_show = Show.objects.create(
            title=request.POST["title"],
            network=request.POST["network"],
            release_date=request.POST["release_date"],
            desc=request.POST["desc"],
        )
        return redirect("./" + str(new_show.id))
    else:
        return redirect("/shows")


def this_show(request, show_id):
    context = {"this_show": Show.objects.get(id=show_id)}
    return render(request, "details.html", context)
