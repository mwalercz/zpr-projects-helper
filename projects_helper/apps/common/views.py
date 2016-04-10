from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters

from projects_helper.apps import students
from projects_helper.apps import lecturers


@sensitive_post_parameters()
@csrf_protect
@never_cache
def user_login(request):
    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'GET':
        return render(request, 'index/login.html', {})
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            if students.email_check(user):
                return redirect('students:profile')
            elif lecturers.email_check(user):
                return redirect('lecturers:profile')
            else:
                return HttpResponse("Invalid login details supplied.")
        else:
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, '404.html')





