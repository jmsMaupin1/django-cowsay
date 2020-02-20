import subprocess

from django.db import models
from django.utils import timezone

def get_cowsay_templates():
    cmd = subprocess.Popen(
        ['cowsay', '-l'],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT
    )

    out, err = cmd.communicate()

    if err:
        raise err
    else:
        return out.decode().replace("\n", " ").split(" ")[4:]

class CowText(models.Model):
    template_choices = [(None, 'cow')]
    template_choices.extend((template, template) for template in get_cowsay_templates())
    text = models.CharField(max_length=250)
    template = models.CharField(max_length=26, choices=template_choices, null=True, blank=True)
    date_submitted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text