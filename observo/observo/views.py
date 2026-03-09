from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseForbidden

from .models import Animal, Observ
from .forms import AnimalForm, ObservForm, SignUpForm

def staff_required(view_func):
    return user_passes_test(lambda u: u.is_authenticated and u.is_staff)(view_func)


def home(request):
    return render(request, "observo/home.html")


def about(request):
    return render(request, "observo/about.html")


def animal_list(request):
    animals = Animal.objects.all()
    return render(request, "observo/animal_list.html", {"animals": animals})


def animal_detail(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    return render(request, "observo/animal_detail.html", {"animal": animal})


@staff_required
def new_animal(request):
    if request.method == "POST":
        form = AnimalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("animal_list")
    else:
        form = AnimalForm()

    return render(request, "observo/new_animal.html", {"form": form})


@staff_required
def change_animal(request, pk):
    animal = get_object_or_404(Animal, pk=pk)

    if request.method == "POST":
        form = AnimalForm(request.POST, instance=animal)
        if form.is_valid():
            form.save()
            return redirect("animal_detail", pk=animal.pk)
    else:
        form = AnimalForm(instance=animal)

    return render(request, "observo/change_animal.html", {"form": form, "animal": animal})


@staff_required
def delete_animal(request, pk):
    animal = get_object_or_404(Animal, pk=pk)

    if request.method == "POST":
        animal.delete()
        return redirect("animal_list")

    return render(request, "observo/delete_animal.html", {"animal": animal})

@login_required
def observ_list(request):
    if request.user.is_staff:
        observs = Observ.objects.all()
    else:
        observs = Observ.objects.filter(user=request.user)

    return render(request, "observo/observ_list.html", {"observs": observs})


@login_required
def observ_detail(request, pk):
    if request.user.is_staff:
        observ = get_object_or_404(Observ, pk=pk)
    else:
        observ = get_object_or_404(Observ, pk=pk, user=request.user)

    return render(request, "observo/observ_detail.html", {"observ": observ})


@login_required
def observ_create(request):
    if request.method == "POST":
        form = ObservForm(request.POST)
        if form.is_valid():
            obs = form.save(commit=False)
            obs.user = request.user
            obs.save()
            return redirect("observ_detail", pk=obs.pk)
    else:
        form = ObservForm()

    return render(request, "observo/new_observ.html", {"form": form})


@login_required
def change_observ(request, pk):
    if request.user.is_staff:
        observ = get_object_or_404(Observ, pk=pk)
    else:
        observ = get_object_or_404(Observ, pk=pk, user=request.user)

    if request.method == "POST":
        form = ObservForm(request.POST, instance=observ)
        if form.is_valid():
            form.save()
            return redirect("observ_detail", pk=observ.pk)
    else:
        form = ObservForm(instance=observ)

    return render(request, "observo/change_observ.html", {"form": form, "observ": observ})


@login_required
def observ_delete(request, n):
    if request.user.is_staff:
        observ = get_object_or_404(Observ, pk=n)
    else:
        observ = get_object_or_404(Observ, pk=n, user=request.user)

    if request.method == "POST":
        observ.delete()
        return redirect("observ_list")

    return render(request, "observo/delete_observ.html", {"observ": observ})

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            role = form.cleaned_data["role"]

            if role == "admin":
                user.is_staff = True
                user.is_superuser = True
                user.save()

            login(request, user)
            return redirect("home")
    else:
        form = SignUpForm()

    return render(request, "registration/signup.html", {"form": form})

def favorite_list(request):
    return render(request, "observo/favorite_list.html")