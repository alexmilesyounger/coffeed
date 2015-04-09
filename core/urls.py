from django.conf.urls import patterns, include, url
import core.views as coreviews

urlpatterns = patterns('', 
    # Examples:
    # url(r'^$', 'coffeed.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', coreviews.LandingView.as_view()),
    url(r'location/$', coreviews.LocationListView.as_view()),
    url(r'search/$', coreviews.SearchListView.as_view()),
    url(r'location/(?P<pk>\d+)/detail/$', coreviews.LocationDetailView.as_view(), name='location_list'),
    # REVIEW FORM
    # url(r'location/create/$', coreviews.ReviewCreateView.as_view()), 
    # url(r'location/(?P<pk>\d+)/update/$', coreviews.ReviewCreateView.as_view(), name='location_update'),
    # LOCATION FORM
    url(r'location/create/$', coreviews.LocationCreateView.as_view()), 
    # NOT YET NEEDED
    # url(r'location/(?P<pk>\d+)/update/$', coreviews.LocationCreateView.as_view(), name='location_update'),
    url(r'location/(?P<pk>\d+)/update/$', coreviews.LocationUpdateView.as_view(), name='location_update'),
)



