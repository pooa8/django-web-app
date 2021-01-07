from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader
from datetime import datetime

import random


def index(request):
    now = datetime.now()
    context = {
        'current_date': now
    }
    return render(request, 'first/index.html', context)


def select(request):
    context = {}
    return render(request, 'first/select.html', context)


def result(request):
    chosen = int(request.GET['number']) # int 형변환 필요

    results = []
    if chosen >= 1 and chosen <= 45:
        results.append(chosen)
    
    box = []
    for i in range(0, 45):
        if chosen != i+1:
            box.append(i+1)

    random.shuffle(box)

    while len(results) < 6: # 로또 번호 6개
        results.append(box.pop())

    context = {
        'number': results
    }
    return render(request, 'first/result.html', context)