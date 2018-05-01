from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .forms import LoginForm,RegisterForm,GuestForm
from django.contrib.auth import login,authenticate,get_user_model,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.http import is_safe_url
from .models import GuestEmail

# Create your views here.
@login_required
def user_logout(request):
    logout(request)
    return redirect("/")

def guest_register_view(request):
    form =GuestForm(request.POST or None)
    context ={"form": form }
    next_ =request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None
    if form.is_valid():
        email =form.cleaned_data.get("email")
        new_guest_email = GuestEmail.objects.create(email=email)
        request.session['guest_email_id'] = new_guest_email.id
        if is_safe_url(redirect_path,request.get_host()):
            return redirect(redirect_path)
        else:
            return redirect("/register/")
    return render(request,"/register/")


def login_page(request):
    form =LoginForm(request.POST or None)
    context ={"form": form }
    next_ =request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None
    print(request.user.is_authenticated)
    if form.is_valid():
        print(form.cleaned_data)
        username =form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request,username =username,password=password)
        if user is not None:
            login(request,user)
            try:
                del request.session['guest_email_id']
            except:
                pass  
            if is_safe_url(redirect_path,request.get_host()):
                context['form'] = LoginForm()
                return redirect(redirect_path)
            else:
                return redirect("/")
        else:
            print("Error")
    return render(request,"accounts/login.html",context)

User =get_user_model()
def register_page(request):
    form = RegisterForm(request.POST or None)
    context ={"form":form}
    if form.is_valid():
        print(form.cleaned_data)
        username =form.cleaned_data.get("username")
        email =form.cleaned_data.get("email")
        password =form.cleaned_data.get("password")
        new_user =User.objects.create_user(username,email,password)
        print(new_user)

    return render(request,"accounts/register.html",context)
