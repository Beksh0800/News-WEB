from django.shortcuts import render, get_object_or_404, redirect
from .models import News
from .forms import NewsUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def home_page(request):
    posts = News.objects.all().order_by('-pub_date')[:4]
    context = {'posts': posts}
    return render(request, './index.html', context)

def all_news_page(request):
    posts = News.objects.all().order_by('-pub_date')
    context = {'posts': posts}
    return render(request, './news-list.html', context)

def news_detail_page(request, pk):
    post = get_object_or_404(News, pk=pk)
    context = {'post': post}
    return render(request, './news_detail.html', context)

def signup_page(request):
    if request.method == 'POST':
        form = NewsUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login_page")

    else:
        form = NewsUserForm()

    context = {'form': form}

    return render(request, './signup.html', context)

def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home_page")

    else:
        form = AuthenticationForm()

    context = {'form': form}
    return render(request, './login.html', context)


def logout_request(request):
    logout(request)
    return redirect("home_page")
