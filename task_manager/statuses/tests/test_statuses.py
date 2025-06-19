from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from task_manager.statuses.models import Status

class StatusCreateTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='admin', password='admin123')
        self.client.login(username='admin', password='admin123')

    def test_create_status(self):
        url = reverse('status_create')
        data = {'name': 'In Progress'}
        response = self.client.post(url, data)

        self.assertRedirects(response, reverse('status_list'))
        self.assertTrue(Status.objects.filter(name='In Progress').exists())


class StatusReadTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.status = Status.objects.create(name='Test Status')
        self.client.login(username='testuser', password='testpass')

    def test_status_list_view(self):
        response = self.client.get(reverse('status_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Status')


class StatusUpdateTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='editor', password='pass123')
        self.status = Status.objects.create(name='Initial Status')
        self.client.login(username='editor', password='pass123')

    def test_status_update_view(self):
        url = reverse('status_update', args=[self.status.pk])
        response = self.client.post(url, {'name': 'Updated Status'})
        self.assertRedirects(response, reverse('status_list'))
        self.status.refresh_from_db()
        self.assertEqual(self.status.name, 'Updated Status')


class StatusDeleteTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='deleter', password='pass123')
        self.status = Status.objects.create(name='To be deleted')
        self.client.login(username='deleter', password='pass123')

    def test_status_delete_view(self):
        url = reverse('status_delete', args=[self.status.pk])
        response = self.client.post(url)
        self.assertRedirects(response, reverse('status_list'))
        self.assertFalse(Status.objects.filter(pk=self.status.pk).exists())
