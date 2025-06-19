from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from task_manager.labels.models import Label
from task_manager.tasks.models import Task
from task_manager.statuses.models import Status

class LabelCRUDTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='pass123')
        self.client.login(username='testuser', password='pass123')
        self.label = Label.objects.create(name='Bug')

    def test_label_list_view(self):
        response = self.client.get(reverse('label_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Bug')

    def test_label_create_view(self):
        response = self.client.post(reverse('label_create'), {'name': 'Feature'})
        self.assertRedirects(response, reverse('label_list'))
        self.assertTrue(Label.objects.filter(name='Feature').exists())

    def test_label_update_view(self):
        response = self.client.post(reverse('label_update', args=[self.label.pk]), {'name': 'Fix'})
        self.assertRedirects(response, reverse('label_list'))
        self.label.refresh_from_db()
        self.assertEqual(self.label.name, 'Fix')

    def test_label_delete_view(self):
        response = self.client.post(reverse('label_delete', args=[self.label.pk]))
        self.assertRedirects(response, reverse('label_list'))
        self.assertFalse(Label.objects.filter(pk=self.label.pk).exists())

    def test_label_delete_protected(self):
        status = Status.objects.create(name='In progress')
        task = Task.objects.create(
            name='Task with label',
            author=self.user,
            status=status
        )
        task.labels.add(self.label)

        response = self.client.post(reverse('label_delete', args=[self.label.pk]))
        self.assertRedirects(response, reverse('label_list'))
        self.assertTrue(Label.objects.filter(pk=self.label.pk).exists())
