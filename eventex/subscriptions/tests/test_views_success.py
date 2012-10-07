# coding: utf-8
from django.test import TestCase
from eventex.subscriptions.models import Subscription
from django.core.urlresolvers import reverse as r


class SuccessTest(TestCase):
    def setUp(self):
        s = Subscription.objects.create(name='Ivan Rocha', cpf='12345678901',
            email='ivan.cr.neto@gmail.com', phone='8487598888')
        self.resp = self.client.get(r('subscriptions:success', args=[s.pk]))

    def test_get(self):
        'GET /inscricao/1/ should return 200.'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'Uses template'
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_detail.html')

    def test_context(self):
        'Context must have a subscription instance.'
        subscription = self.resp.context['subscription']
        self.assertIsInstance(subscription, Subscription)

    def test_html(self):
        'Check if subscription data was rendered.'
        self.assertContains(self.resp, 'Ivan Rocha')


class SuccessViewNotFound(TestCase):
    def test_not_found(self):
        response = self.client.get(r('subscriptions:success', args=[0]))
        self.assertEqual(404, response.status_code)
