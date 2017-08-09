from django.conf.urls import url
import views

urlpatterns = [
    url('your-feedback', views.record_feedback, name='feedback')
]