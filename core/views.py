from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
import core.models as coremodels

# Create your views here. 

class LandingView(TemplateView):
	template_name = 'base/index.html'

class LocationListView(ListView):
	model = coremodels.Location
	template_name = 'location/list.html'

class SearchListView(LocationListView):
	
	def get_queryset(self):
		incoming_query_string = self.request.GET.get('query', '')
		return coremodels.Location.objects.filter(title__icontains=incoming_query_string)

# class SearchListView(LocationListView):

# 	def get_queryset(self):
# 		incoming_query_string = self.request.GET.get('query','')
# 		return coremodels.Location.objects.filter(title__icontains=incoming_query_string)

class LocationDetailView(DetailView):
	model = coremodels.Location
	template_name = 'location/detail.html'
	context_object_name = 'location'

# WORKING REVIEW FORM
# class ReviewCreateView(CreateView):
#     model = coremodels.Review
#     template_name = 'base/form.html'
#     fields = "__all__"

class LocationCreateView(CreateView):
	model = coremodels.Location
	template_name = 'base/form.html'
	fields = "__all__"

class LocationUpdateView(UpdateView):
	model = coremodels.Location
	template_name = 'base/form.html'
	fields = "__all__"

class ReviewCreateView(CreateView):
	model = coremodels.Review
	template_name = 'base/form.html'
	fields = ['description', 'rating']

	def form_valid(self, form):
		form.instance.user = self.request.user
		form.instance.location = coremodels.Location.objects.get(id=self.kwargs['pk'])
		return super(ReviewCreateView, self).form_valid(form)

	def get_success_url(self):
		return self.object.location.get_absolute_url()









