from django import forms


class FeedbackForm(forms.Form):
    feedback = forms.CharField(label='Feedback', max_length=5000)
