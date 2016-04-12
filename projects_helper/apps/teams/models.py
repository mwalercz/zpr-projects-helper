from django.core.urlresolvers import reverse
from django.db import models


class Team(models.Model):
    project_preference = models.ForeignKey(
        'projects.Project',
        on_delete=models.SET_NULL,
        null=True
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('teams:detail', args=[str(self.id)])
