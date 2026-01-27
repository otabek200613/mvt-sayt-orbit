from django.shortcuts import render, redirect
from .models import *
from .forms import ContactForm, ChangeProfileForm,PasswordChangeForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def home(request):
    home = Home.objects.filter(is_active=True).first()  # <-- bitta obyekt
    about = About.objects.filter(is_published=True)
    categories = Categories.objects.all()
    portfolio = Portfolio.objects.all()
    cat = request.GET.get('cat')
    services = Services.objects.all()
    experience = Experience.objects.all()
    education = Education.objects.all()
    clients = Clients.objects.all()
    blog = Blog_posts.objects.all()
    resume_photo = Resume_photo.objects.filter(is_active=True)
    footer = Footer.objects.filter(is_published=True).first()

    form = ContactForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('.')

    if cat:
        portfolio = Portfolio.objects.filter(category__title__iexact=cat)

    context = {
        'home': home,  # <-- endi obyekt
        'abouts': about,
        'portfolio': portfolio,
        'categories': categories,
        'services': services,
        'experience': experience,
        'education': education,
        'clients': clients,
        'resume_photo': resume_photo,
        'blog': blog,
        'form': form,
        'footer': footer,
    }
    return render(request, 'index.html', context)


def login_view(request):
    home = Home.objects.filter(is_active=True).first()
    if request.user.is_authenticated:
        return redirect('home')
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_url = request.GET.get('next')
            return redirect(next_url or 'home')
    context = {
        'form': form,
        'home': home,
    }

    return render(request, 'login.html', context)


def logout_view(request):
    home = Home.objects.filter(is_active=True).first()
    if not request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    context = {
        'home': home,
    }

    return render(request, 'logout.html',context)


def register(request):
    home = Home.objects.filter(is_active=True).first()
    if request.user.is_authenticated:
        return redirect('/')
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/login')
    context = {
        'form': form,
        'home': home,
    }
    return render(request, 'register.html', context)


@login_required
def profile(request):
    home = Home.objects.filter(is_active=True).first()
    if request.method == "POST":
        form = ChangeProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profil yangilandi ✅")
            return redirect(".")  # yoki redirect('.')
    else:
        form = ChangeProfileForm(instance=request.user)
        context = {
            'form': form,
            'home': home,
        }

    return render(request, "profile.html", context)


def reset_password(request):
    return render(request, 'reset-password.html')


@login_required
def change_password(request):
    home = Home.objects.filter(is_active=True).first()
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('profile')
    else:
        form = PasswordChangeForm(user=request.user)
    context = {
        'form': form,
        'home': home,
    }
    return render(request, 'change-password.html', context)
