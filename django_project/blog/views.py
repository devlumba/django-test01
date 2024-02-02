from django.shortcuts import render

# Create your views here.

posts = [
    {
        'author': 'God',
        'title': 'TOP 10 HOLY-C FRAMEWORKS',
        'content': '',
        'date_posted': 'December 29, 0000',
    },
    {
        'author': 'Isa',
        'title': 'C++ CRITIQUE',
        'content': "don't",
        'date_posted': 'December 29, 1989',
    }

]


def home(request):
    context = {
        'posts': posts,
        'title': "Home page",
    }
    return render(request, template_name="blog/home.html", context=context)


def about(request):
    return render(request, template_name="blog/about.html", context={'title': "About page"})