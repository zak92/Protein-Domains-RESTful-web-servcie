from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect

# refactoring using django's generic views
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView

# Create your views here.

