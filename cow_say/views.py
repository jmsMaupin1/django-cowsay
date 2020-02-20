import subprocess

from django.shortcuts import render, reverse, HttpResponseRedirect

from cow_say.forms import CowEchoForm
from cow_say.models import CowText

def cowsay_helper(text, template=None):
    cmd_arr = ['cowsay']
    if template:
        cmd_arr.extend(['-f', template])
    cmd_arr.extend([text])

    cmd  = subprocess.Popen(
        cmd_arr,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT
    )

    out, err = cmd.communicate()

    if err:
        raise err
    else:
        return out.decode().split("\n")
        

def index(request):
    if request.method == "POST":
        form = CowEchoForm(request.POST)

        if form.is_valid():
            cow_text = form.cleaned_data['text']
            template = form.cleaned_data['template']
            form.save()

            return render(request, 'index.html', {
                'form': CowEchoForm(),
                'text': cowsay_helper(cow_text, template=template)
            })

    return render(request, 'index.html', {
        'form': CowEchoForm()
    })


def history(request):
    texts = CowText.objects.order_by('-date_submitted')[:10]
    return render(request, 'history.html', {
        "texts": texts
    })


def text_view(request, text_id):
    cow_text = CowText.objects.get(id=text_id)
    return render(request, 'index.html', {
        'text': cowsay_helper(cow_text.text, cow_text.template)
    })