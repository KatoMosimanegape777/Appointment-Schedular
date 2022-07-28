from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.views.generic import TemplateView

def logout_view(request):
    logout(request)
    return redirect('http://127.0.0.1:8000/')


class register_teacher(TemplateView):
    template_name = "register_teacher.html"


class register_student(TemplateView):
    template_name = "register_student.html"