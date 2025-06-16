from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from task_manager.task_manager_app.tasks.models import Task
from task_manager.task_manager_app.statuses.models import Status


class TaskCreateTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='creator', password='pass123')
        self.status = Status.objects.create(name='Open')
        self.client.login(username='creator', password='pass123')

    def test_create_task(self):
        url = reverse('task_create')
        data = {
            'name': 'New Task',
            'description': 'Task description',
            'status': self.status.id,
            'executor': ''
        }
        response = self.client.post(url, data)
        self.assertRedirects(response, reverse('task_list'))
        self.assertTrue(Task.objects.filter(name='New Task').exists())


class TaskReadTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='reader', password='pass123')
        self.status = Status.objects.create(name='In progress')
        self.task = Task.objects.create(
            name='Read Task',
            description='Some desc',
            author=self.user,
            status=self.status
        )
        self.client.login(username='reader', password='pass123')

    def test_task_list_view(self):
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Read Task')

    def test_task_detail_view(self):
        url = reverse('task_detail', args=[self.task.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Some desc')


class TaskUpdateTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='editor', password='pass123')
        self.status = Status.objects.create(name='To edit')
        self.task = Task.objects.create(
            name='Old Task',
            description='Old desc',
            author=self.user,
            status=self.status
        )
        self.client.login(username='editor', password='pass123')

    def test_task_update_view(self):
        url = reverse('task_update', args=[self.task.pk])
        data = {
            'name': 'Updated Task',
            'description': 'New description',
            'status': self.status.id,
            'executor': ''
        }
        response = self.client.post(url, data)
        self.assertRedirects(response, reverse('task_list'))
        self.task.refresh_from_db()
        self.assertEqual(self.task.name, 'Updated Task')


class TaskDeleteTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='deleter', password='pass123')
        self.other_user = User.objects.create_user(username='other', password='pass456')
        self.status = Status.objects.create(name='Delete Test')
        self.own_task = Task.objects.create(
            name='My Task',
            description='desc',
            author=self.user,
            status=self.status
        )
        self.client.login(username='deleter', password='pass123')

    def test_task_delete_own(self):
        url = reverse('task_delete', args=[self.own_task.pk])
        response = self.client.post(url)
        self.assertRedirects(response, reverse('task_list'))
        self.assertFalse(Task.objects.filter(pk=self.own_task.pk).exists())

    def test_task_delete_not_owner(self):
        foreign_task = Task.objects.create(
            name='Not mine',
            description='desc',
            author=self.other_user,
            status=self.status
        )
        url = reverse('task_delete', args=[foreign_task.pk])
        response = self.client.post(url)
        self.assertRedirects(response, reverse('task_list'))
        self.assertTrue(Task.objects.filter(pk=foreign_task.pk).exists())
