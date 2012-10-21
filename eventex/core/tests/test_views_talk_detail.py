# coding: utf-8
from django.test import TestCase
from eventex.core.models import Talk
from django.core.urlresolvers import reverse as r


class TalkListTest(TestCase):
    def setUp(self):
        t = Talk.objects.create(description=u'Descrição da palestra',
            title='Título da palestra', start_time='10:00')
        t.speakers.create(name='Ivan Rocha', slug='ivan-rocha',
            url='http://ivanneto.com.br', description='Passionate software developer!')
        self.resp = self.client.get(r('core:talk_detail', args=[1]))

    def test_get(self):
        'GET must result in 200.'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'core/talk_detail.html')

    def test_talk_in_context(self):
        talk = self.resp.context['talk']
        self.assertIsInstance(talk, Talk)

    def test_not_found(self):
        response = self.client.get(r('core:talk_detail', args=[0]))
        self.assertEqual(404, response.status_code)
