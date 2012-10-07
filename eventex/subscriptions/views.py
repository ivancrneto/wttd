# coding: utf-8
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.views.generic.simple import direct_to_template
from django.shortcuts import get_object_or_404
from forms import SubscriptionForm
from models import Subscription


def subscribe(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)


def new(request):
    return direct_to_template(request,
            'subscriptions/subscription_form.html',
            {'form': SubscriptionForm()})


def create(request):
    form = SubscriptionForm(request.POST)
    if not form.is_valid():
        return direct_to_template(request,
            'subscriptions/subscription_form.html', {'form': form})
    # obj = Subscription(**form.cleaned_data)
    # obj.save()
    obj = form.save()
    return HttpResponseRedirect('/inscricao/%d/' % obj.pk)


def success(request, pk):
    subscription = get_object_or_404(Subscription, pk=pk)
    return direct_to_template(request,
         'subscriptions/subscription_detail.html',
         {'subscription': subscription})
