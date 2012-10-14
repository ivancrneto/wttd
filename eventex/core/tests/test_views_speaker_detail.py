# coding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse as r
from eventex.core.models import Speaker


class SpeakerDetailTest(TestCase):
    def setUp(self):
        self.speaker = Speaker(name='Ivan Rocha',
                slug='ivan-rocha',
                url='http://ivanneto.com.br',
                description='Passionate software developer!')
        self.speaker.save()
        url = r('core:speaker_detail', kwargs={'slug': 'ivan-rocha'})
        self.resp = self.client.get(url)

    def test_get(self):
        'Get should result in 200.'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'Homepage must use template speaker_detail.html.'
        self.assertTemplateUsed(self.resp, 'core/speaker_detail.html')

    def test_html(self):
        self.assertContains(self.resp, 'Ivan Rocha')
        self.assertContains(self.resp, 'Passionate software developer')
        self.assertContains(self.resp, 'http://ivanneto.com.br')

    def test_context(self):
        'Speaker must be in context.'
        speaker = self.resp.context['speaker']
        self.assertIsInstance(speaker, Speaker)


class SpeakerDetailNotFound(TestCase):
    def test_not_found(self):
        url = r('core:speaker_detail', kwargs={'slug': 'paula-rocha'})
        response = self.client.get(url)
        self.assertEqual(404, response.status_code)
