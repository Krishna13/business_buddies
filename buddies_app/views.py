from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib import messages

# Create your views here.
def render_login(request):
    return render(request, "login.html")

def perform_login(request):
    if request.method != "POST":
        return HttpResponse("Method not Allowed")
    else:
        user = authenticate(username=request.POST.get("username"), password=request.POST.get("password"))
        if user is not None:
            login(request, user)
            if user.user_type == "1":
                return HttpResponseRedirect('/admin_home')
            else:
                return HttpResponseRedirect(reverse("employee_home"))
        else:
            messages.error(request, "Invalid Credentials")
            return HttpResponseRedirect("/")

def logout_it(request):
    logout(request)
    return HttpResponseRedirect("/")

def admin_home(request):
    if request.user.is_anonymous:
        return redirect("/")
    return render(request, "admin_home.html")

def render_create_orders(request):
    if request.user.is_anonymous:
        return redirect("/")
    return render(request, "create_orders.html")

def render_create_products(request):
    if request.user.is_anonymous:
        return redirect("/")
    return render(request, "create_products.html")