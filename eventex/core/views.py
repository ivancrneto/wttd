# coding: utf-8
from django.views.generic.simple import direct_to_template
from django.shortcuts import get_object_or_404
from eventex.core.models import Speaker, Talk


def homepage(request):
    return direct_to_template(request, 'index.html')


def speaker_detail(request, slug):
    speaker = get_object_or_404(Speaker, slug=slug)
    context = {'speaker': speaker}
    return direct_to_template(request, 'core/speaker_detail.html', context)


def talk_list(request):
    context = {
        'morning_talks': Talk.objects.at_morning(),
        'afternoon_talks': Talk.objects.at_afternoon()
    }
    return direct_to_template(request, 'core/talk_list.html', context)


def talk_detail(request, pk):
    talk = get_object_or_404(Talk, pk=pk)
    context = {
        'talk': talk,
    }
    return direct_to_template(request, 'core/talk_detail.html', context)
