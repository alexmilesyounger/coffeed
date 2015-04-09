from django.conf.urls import patterns, include, url
import core.views as coreviews

urlpatterns = patterns('', 
    # Examples:
    # url(r'^$', 'coffeed.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', coreviews.LandingView.as_view()),
    url(r'location/$', coreviews.LocationListView.as_view()),
    url(r'location/(?P<pk>\d+)/detail/$', coreviews.LocationDetailView.as_view(), name='location_list'),
   	
   	# This is the video code for urls.py
    # url(r'location/create/$', coreviews.LocationCreateView.as_view()), 
	
	# Lesson note code for urls.py
    # url(r'location/(?P<pk>\d+)/update/$', coreviews.LocationUpdateView.as_view(), name='location_update'),

    # Lesson note code for urls.py ADAPTED BY ALEX TO MATCH NOTE CLASS NAME 
    # PLUST the video code for urls.py UPDATED TO MATCH NOTE CLASS NAME
    url(r'location/create/$', coreviews.ReviewCreateView.as_view()), 
    url(r'location/(?P<pk>\d+)/update/$', coreviews.ReviewCreateView.as_view(), name='location_update'),


)



