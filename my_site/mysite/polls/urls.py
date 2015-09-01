from django.conf.urls import url

from . import views

urlpatterns = [
	#this will process and route any url requets sent to the polls app. 
	#by the time a request gets here, the pattern that sent it here has been removed
	#it will then route the processing of that request to a function in the views.py file for this app
    
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]