from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth import logout as auth_logout
# Create your views here.



def register(request):

    if request.method == 'POST':

        form = UserCreationForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            return redirect('home')
    else:

        form = UserCreationForm()

    context = {'form': form}

    return render(request, 'Blog/register.html', context=context)

def login_view(request):
        
        if request.user.is_authenticated:
            return redirect('home')
    
        if request.method == 'POST':
    
            form = AuthenticationForm(data=request.POST)
    
            if form.is_valid():
    
                user = form.get_user()
    
                login(request, user)
    
                return redirect('home')
        else:
    
            form = AuthenticationForm()
    
        context = {'form': form}
    
        return render(request, 'Blog/login.html', context=context)

@login_required(login_url='/login/')
def logout_view(request):

    auth_logout(request)

    return redirect('home')
    
@login_required(login_url='/login/')
def home(request):

    postear = Post.objects.order_by('-created_at')
    context = {'postear': postear}
    return render(request, 'Blog/home.html', context=context)

@login_required(login_url='/login/')
def create(request):
    
        if request.method == 'POST':
    
            form = PostForm(request.POST)
    
            if form.is_valid():
    
                form.save()
    
                return redirect('home')
        else:
    
            form = PostForm()
    
        context = {'form': form}
    
        return render(request, 'Blog/create.html', context=context)
