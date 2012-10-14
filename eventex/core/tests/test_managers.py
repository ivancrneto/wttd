# coding: utf-8
from django.test import TestCase
from eventex.core.models import Contact, Speaker, Talk


class ContactManagerTest(TestCase):
    def setUp(self):
        s = Speaker.objects.create(name='Ivan Rocha',
            slug='ivan-rocha', url='http://ivanneto.com.br')
        s.contact_set.add(Contact(kind='E', value='ivan.cr.neto@gmail.com'),
            Contact(kind='P', value='84-87592558'),
            Contact(kind='F', value='84-32138475'))

    def test_emails(self):
        qs = Contact.emails.all()
        expected = ['<Contact: ivan.cr.neto@gmail.com>']
        self.assertQuerysetEqual(qs, expected)

    def test_phones(self):
        qs = Contact.phones.all()
        expected = ['<Contact: 84-87592558>']
        self.assertQuerysetEqual(qs, expected)

    def test_faxes(self):
        qs = Contact.faxes.all()
        expected = ['<Contact: 84-32138475>']
        self.assertQuerysetEqual(qs, expected)


class PeriodManagerTest(TestCase):
    def setUp(self):
        Talk.objects.create(title='Morning Talk', start_time='10:00')
        Talk.objects.create(title='Afternoon Talk', start_time='12:00')

    def test_morning(self):
        'Should return only talks before 12:00'
        self.assertQuerysetEqual(
            Talk.objects.at_morning(), ['Morning Talk'],
            lambda t: t.title)

    def test_afternoon(self):
        'Should return only talks after 12:00'
        self.assertQuerysetEqual(
            Talk.objects.at_afternoon(), ['Afternoon Talk'],
            lambda t: t.title)
