from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts

# Create your views here.
# creating Home: this page will handle traffic at HOME route
# it takes request arg.

#rendering on text while respose
# def home(request):
#     return HttpResponse("<h1>Bolg Home Page</h1>")
# def about(request):
#     return HttpResponse("<h1>this is ABout Page</h1>")

# data to send to template to render on webpage
# this data can recieve from database or file,
posts=[
    {
        'author': "Dhawal",
        'title': "Blog post 01",
        'content': "First post content",
        'date_posted': "august 27, 2022"
    },
    {
        'author': "kshitya",
        'title': "Blog post 02",
        'content': "second post content",
        'date_posted': "august 28, 2022"
    }
]

# rendering the templates
def home (request):
    # adding this variable to send data to render over page
    # print(Posts.objects.all())
    context = {
        # 'posts' : posts,
        'posts' : Posts.objects.all(),
        'title': "Home"
    }
    return render(request,'blog/home.html',context)

def about(request):
    context = {
        # 'posts': posts,
        'title': "About"
    }
    return render (request,'blog/about.html',context)

