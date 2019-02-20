from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import GuessNumbers
from .models import getAllUser
from .form import PostForm

def test(request):
    return render(request, 'solution/test.html', {})


def index(request):
    solution = getAllUser()

    return render(request, "solution/default.html", {"solution":solution})


def post(request):
    form = PostForm()
    return render(request, 'solution/form.html', {"form":form})
