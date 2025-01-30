from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=50, choices=[('admin', 'Admin'), ('regular', 'Regular')], default='regular')
    consent_given = models.BooleanField(default=False)
    consent_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.user.username