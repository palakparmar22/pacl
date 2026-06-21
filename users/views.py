from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
import pandas as pd
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

def insert_data_using_csv(csv_file_path):
    name_list = pd.read_csv(csv_file_path)
    for idx, row in name_list.iterrows():
        sr_no = row["No"]
        if int(sr_no) != 1:
            continue
        name = row["Name"]
        certificate_no = row["ID Number"]
        password = row["Password"]
        
        new_user = Users_M.objects.create(sr_no=sr_no, name=name, certificate_no=certificate_no, password=password)
        new_user.save()
        

