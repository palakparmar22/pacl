from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from . models import Users, Users_M


def index(request):
    users = Users.objects.all()
    context = {
        'users': users,
    }
    return render(request, "index.html", context)

def index_m(request):
    users = Users_M.objects.all()
    context = {
        'users': users,
        'completed_count': users.filter(is_completed=1, is_editable=0).count(),
        'editable_count':  users.filter(is_editable=1, is_completed=None or 0).count(),
        'pending_count':    users.filter(is_editable=1, is_completed=None or 0).count() -  users.filter(is_completed=1, is_editable=0).count()
    }
    return render(request, "index_m.html", context)



