from django.shortcuts import render, redirect
from .models import *
from .forms import ContactForm

def home(request):
    home = Home.objects.first()   # <-- bitta obyekt
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
        'home': home,          # <-- endi obyekt
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
