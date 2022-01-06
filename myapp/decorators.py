from django.shortcuts import redirect, HttpResponse
from django.http.response import HttpResponse

def unauthenticated_user(view_func):
    def wrapper_func(request,*args, **kwargs):
            if request.user.is_anonymous:
                return redirect("/login")
            else:

                return view_func(request,*args, **kwargs)

    return wrapper_func


def allowed_user(allowed_rules = []):
    def decorator(view_func):
        def wrapper_func(request,*args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_rules:
                return view_func(request,*args, **kwargs)
            else:
                return HttpResponse("You are not authorised to view this page")


        return wrapper_func
    return decorator


def admin_only(view_func):
        def wrapper_func(request,*args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group == 'customer':
                return redirect('/user')
            elif group == 'admin':
                return view_func(request,*args, **kwargs)
            else:
                return redirect("/login")

                
        return wrapper_func
