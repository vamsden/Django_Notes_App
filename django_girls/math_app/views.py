import json
import socket

from django.shortcuts import render
from django.http import HttpResponse
from models import InputForm, AdditionForm
from compute import compute, addition


# Create your views here.

"""
def index(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            return present_output(form)
    else:
        form = InputForm()
    return render(request, 'math_app/index.html', {'form': form})
def present_output(form):
    r = form.r
    s = compute(r)
    return HttpResponse('Hello, World! sin(%s)=%s' % (r, s))
"""


def index(request):
    s = None  # initial value of result
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            r = form.r
            s = compute(r)
    else:
        form = InputForm()

    return render(request, 'math_app/index.html',
                  {'form': form,
                   's': s if isinstance(s, float) else ''})


def add(request):
    t = None
    if request.method == 'POST':
        add_form = AdditionForm(request.POST)
        if add_form.is_valid():
            add_form = add_form.save(commit=False)
            a = add_form.a
            b = add_form.b
            t = addition(a, b)
    else:
        add_form = AdditionForm()

    context = {
        'add_form': add_form,
        't': t if isinstance(t, float) else '',
    }

    return render(request, 'math_app/add.html', context)


def main(request):
    return render(request, 'math_app/ajax.html', context={})


def ajaxexample(request):
    if request.POST.has_key('client_response'):
        x = request.POST['client_response']
        y = socket.gethostbyname(x)
        response_dict = {}
        response_dict.update({'server_response': y})
        return HttpResponse(json.dumps(response_dict),
                            content_type='application/javascript')
    else:
        return render(request, 'math_app/ajax.html', context={})
