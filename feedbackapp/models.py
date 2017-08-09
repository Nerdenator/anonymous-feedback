from django.db import models


class Feedback (models.Model):
    submitted = models.DateTimeField(auto_now=True)
    feedback_text = models.TextField(null=False)
    submitter_ip = models.GenericIPAddressField()

    def __str__(self):
        return str(self.id)
