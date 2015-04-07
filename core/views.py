from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
import core.models as coremodels

# Create your views here. 

class LandingView(TemplateView):
	template_name = 'base/index.html'

class LocationListView(ListView):
	model = coremodels.Location
	template_name = 'location/list.html'
	# template_name = 'base/theme.html'

# class LocationDetailView(DetailView):
# 	model = coremodels.location
# 	template_name = 'location/detail.html'
# 	context_object_name = 'location'