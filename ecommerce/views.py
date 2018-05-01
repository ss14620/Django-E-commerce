from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .forms import ContactForm
from django.contrib.auth import login,authenticate,get_user_model,logout



def home_page(request):
    # print(request.session.get("first_name","Unknown"))
    #request.session['first_name']
    context = {'title': 'Hello World!'}
    if request.user.is_authenticated:
        context["premium_content"]='Congo!!!!'
    return render(request,'home_page.html',context)


def about_page(request):
    return render(request,'about_page.html',{})


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context ={ "form":contact_form }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    #if request.method == "POST":
        # print(request.POST.get('Full Name'))
        # print(request.POST.get('email'))
        # print(request.POST.get('content'))
    return render(request,'contact_page.html',context)
