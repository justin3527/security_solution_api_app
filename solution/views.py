from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from . models import GuessNumbers
from .forms import PostForm

def test(request):
    return render(request, 'solution/test.html', {})


def index(request):
    solution = GuessNumbers.objects.all()

    return render(request, "solution/default.html", {"solutions":solutions})


def post(request):
    form = PostForm()
    return render(request, 'solution/form.html', {"form":form})
