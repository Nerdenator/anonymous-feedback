from django.conf.urls import url
import views


urlpatterns = [
    url('', views.record_feedback, name='feedback'),
    url('thanks', views.thanks, name='thanks'),
]
