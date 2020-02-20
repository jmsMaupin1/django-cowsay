import subprocess

from django.shortcuts import render, reverse, HttpResponseRedirect

from cow_say.forms import CowEchoForm
from cow_say.models import CowText

def index(request):
    if request.method == "POST":
        form = CowEchoForm(request.POST)

        if form.is_valid():
            cow_text = form.cleaned_data['text']
            cmd  = subprocess.Popen(
                ['cowsay', cow_text],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT
            )
            out, err = cmd.communicate()
            text = out.decode().split('\n')

            form.save()

            return render(request, 'index.html', {
                'form': CowEchoForm(),
                'text': text
            })

    return render(request, 'index.html', {
        'form': CowEchoForm()
    })

def history(request):
    texts = CowText.objects.order_by('-date_submitted')[:10]
    return render(request, 'history.html', {
        "texts": texts
    })