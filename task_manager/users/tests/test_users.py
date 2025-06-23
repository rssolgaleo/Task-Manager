from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


User = get_user_model()


class UserTests(TestCase):
    def test_user_creation(self):
        response = self.client.post(reverse('user_create'), {
            'first_name': 'Test',
            'last_name': 'User',
            'username': 'testuser',
            'password1': 'StrongPass123',
            'password2': 'StrongPass123',
        })

        self.assertRedirects(response, reverse('login'))
        self.assertTrue(User.objects.filter(username='testuser').exists())


class UserReadTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='reader',
            password='testpass'
        )

    def test_user_list_accessible(self):
        response = self.client.get(reverse('user_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.user.username)


class UserUpdateTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='editor',
            password='pass123'
        )
        self.other_user = User.objects.create_user(
            username='someone',
            password='pass123'
        )

    def test_user_can_update_self(self):
        self.client.login(username='editor', password='pass123')
        response = self.client.post(
            reverse('user_update', args=[self.user.id]),
            {
                'first_name': 'Updated',
                'last_name': 'Name',
                'username': 'editor',
                'password1': 'newpass123',
                'password2': 'newpass123',
            }
        )
        self.assertRedirects(response, reverse('user_list'))
        self.user.refresh_from_db()
        self.assertEqual(self.user.first_name, 'Updated')

    def test_user_cannot_update_other(self):
        self.client.login(username='editor', password='pass123')
        response = self.client.post(
            reverse('user_update', args=[self.other_user.id]),
            {
                'first_name': 'Hacker',
                'last_name': 'someone',
                'username': 'someone',
                'password1': 'newpass123',
                'password2': 'newpass123',
            },
            follow=True
        )
        self.assertRedirects(response, reverse('user_list'))


class UserDeleteTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='deleter', password='pass123'
        )
        self.other_user = User.objects.create_user(
            username='other', password='pass123'
        )

    def test_user_can_delete_self(self):
        self.client.login(username='deleter', password='pass123')
        response = self.client.post(
            reverse('user_delete', args=[self.user.id])
        )
        self.assertRedirects(response, reverse('user_list'))
        self.assertFalse(User.objects.filter(username='deleter').exists())

    def test_user_cannot_delete_other(self):
        self.client.login(username='deleter', password='pass123')
        response = self.client.post(
            reverse('user_delete', args=[self.other_user.id])
        )
        self.assertRedirects(response, reverse('user_list'))
        self.assertTrue(User.objects.filter(username='other').exists())
