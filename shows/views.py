from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Show


def root_redirect(request):
    return redirect("/shows")


def index(request):
    context = {"all_shows": Show.objects.all()}
    return render(request, "table.html", context)


def add_new(request):
    return render(request, "form.html")


def valid(request):
    errors = Show.objects.validate(request.POST)
    if len(errors) > 0:
        for msg in errors.values():
            messages.error(request, msg)
        return False
    else:
        return True


def create(request):
    if request.method == "POST":
        if not valid(request):
            return redirect("./new")
        else:
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


def destroy(request, show_id):
    Show.objects.get(id=show_id).delete()
    return redirect("/shows")


def update(request, show_id):
    if request.method == "POST":
        if not valid(request):
            return redirect(f"/shows/{show_id}/edit")
        else:
            update_show = Show.objects.get(id=show_id)
            fields = ["title", "network", "release_date", "desc"]
            for field in fields:
                if request.POST[field] != getattr(update_show, field):
                    update_show.__dict__[field] = request.POST[field]
            update_show.save()
            return redirect("../" + str(update_show.id))
    else:
        return redirect("/shows")


def edit(request, show_id):
    edit_show = Show.objects.get(id=show_id)
    context = {"this_show": edit_show}
    return render(request, "edit.html", context)
