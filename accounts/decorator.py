from django.shortcuts import redirect
from functools import wraps


def unauthenticated(view_func):
    @wraps(view_func)
    def __wrapper_func(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request,*args,**kwargs)
    return __wrapper_func


