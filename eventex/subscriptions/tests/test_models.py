# coding utf-8
from django.test import TestCase
from django.db import IntegrityError
from eventex.subscriptions.models import Subscription
from datetime import datetime


class SubscriptionTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Ivan Rocha',
            cpf='012345678901',
            email='ivan.cr.neto@gmail.com',
            phone='84-87598888',
        )

    def test_create(self):
        'Subscription must have name, cpf, email, phone'
        self.obj.save()
        self.assertEqual(self.obj.id, 1)

    def test_has_created_at(self):
        'Subscription must have automatic created_at'
        self.obj.save()
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_unicode(self):
        self.assertEqual(u'Ivan Rocha', unicode(self.obj))

    # def test_paid_default_value_is_false(self):
    #     self.assertEqual


class SubscriptionUniqueTest(TestCase):
    def setUp(self):
        # Create a first entry to force the collision
        Subscription.objects.create(name='Ivan Rocha', cpf='012345678901',
            email='ivan.cr.neto@gmail.com', phone='8487598888')

    def test_cpf_unique(self):
        'CPF must be unique'
        s = Subscription(name='Ivan Rocha', cpf='012345678901',
            email='ivancrneto@gmail.com', phone='8487598888')
        self.assertRaises(IntegrityError, s.save)

    def test_email_unique(self):
        'Email must be unique'
        s = Subscription(name='Ivan Rocha', cpf='109876543210',
            email='ivan.cr.neto@gmail.com', phone='8487598888')
        self.assertRaises(IntegrityError, s.save)
