from django.shortcuts import render, redirect


def root_redirect(request):
    return redirect("/shows")


def index(request):
    return render(request, "table.html")


def add_new(request):
    return render(request, "form.html")