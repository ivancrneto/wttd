# coding: utf-8
from django.test import TestCase
from eventex.core.models import Speaker, Talk
from django.core.urlresolvers import reverse as r


class TalkListTest(TestCase):
    def setUp(self):
        s = Speaker.objects.create(name='Ivan Rocha', slug='ivan-rocha',
            url='http://ivanneto.com.br', description='Passionate software developer!')
        t1 = Talk.objects.create(description=u'Descrição da palestra',
            title='Título da palestra', start_time='10:00')
        t2 = Talk.objects.create(description=u'Descrição da palestra',
            title='Título da palestra', start_time='13:00')
        t1.speakers.add(s)
        t2.speakers.add(s)
        self.resp = self.client.get(r('core:talk_list'))

    def test_get(self):
        'GET must result in 200.'
        self.assertEqual(200, self.resp.status_code)

    def test_html(self):
        'Html should list talks.'
        self.assertContains(self.resp, u'Título da palestra', 2)
        self.assertContains(self.resp, u'/palestras/1/')
        self.assertContains(self.resp, u'/palestras/2/')
        self.assertContains(self.resp, u'/palestrantes/ivan-rocha/', 2)
        self.assertContains(self.resp, u'Passionate software developer!', 2)
        self.assertContains(self.resp, u'Ivan Rocha', 2)
        self.assertContains(self.resp, u'Descrição da palestra', 2)

    def test_morning_talks_in_context(self):
        self.assertIn('morning_talks', self.resp.context)

    def test_afternoon_talks_in_context(self):
        self.assertIn('afternoon_talks', self.resp.context)
