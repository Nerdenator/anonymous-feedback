from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import FeedbackForm
from .models import Feedback


def record_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            # do stuff
            feedback = Feedback()
            feedback.submitter_ip = get_client_ip(request)
            feedback.feedback_text = form.cleaned_data['feedback']
            feedback.save()
            return HttpResponseRedirect('/thanks/')
    else:
        form = FeedbackForm()

    return render(request, 'feedbackapp/feedback_form.html', {'form': form})


# https://stackoverflow.com/questions/4581789/how-do-i-get-user-ip-address-in-django
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1] # needs to be the last element in array for Heroku
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
