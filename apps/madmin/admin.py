from django.contrib import admin

# Register your models here.
from django.views import generic
from django.http import HttpResponse
from django.shortcuts import render


class Admin(generic.View):
    def get(self, request):
        return render(request,'madmin/admin.html')
