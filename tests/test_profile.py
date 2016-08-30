import os
from datetime import date

from django.conf import settings
from django_webtest import WebTest
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile

from twitter.models import Tweet

User = get_user_model()


class ProfileTestCase(WebTest):
    def setUp(self):
        self.user = User.objects.create_user(
            username='larrypage', first_name='Larry', last_name='Page', 
            email='larrypage@twitter.com', birth_date=date(1992, 7, 6), 
            password='coffee')

    def test_update_user_profile(self):
        """Should update user profile when given data is valid"""
        # Preconditions
        self.assertEqual(self.user.username, 'larrypage')
        self.assertEqual(self.user.first_name, 'Larry')
        self.assertEqual(self.user.last_name, 'Page')
        self.assertEqual(self.user.birth_date, date(1992, 7, 6))
        self.assertEqual(self.user.avatar, None)
        with self.assertRaises(User.DoesNotExist):
            User.objects.get(username='sergeybrin')
            
        profile = self.app.get('/profile', user=self.user)
        form = profile.form
        form['username'] = 'sergeybrin'
        form['first_name'] = 'Sergey'
        form['last_name'] = 'Brin'
        form['birth_date'] = '1988-4-25'
        avatar_url = os.path.join(
            settings.BASE_DIR, 'twitter/static/img/sample.jpg')
        form.submit(
            upload_files=[('avatar', avatar_url)]
        )
        
        # Postconditions
        updated_user = User.objects.get(username='sergeybrin')
        self.assertEqual(updated_user.username, 'sergeybrin')
        self.assertEqual(updated_user.first_name, 'Sergey')
        self.assertEqual(updated_user.last_name, 'Brin')
        self.assertEqual(updated_user.birth_date, date(1988, 4, 25))
        self.assertEqual(updated_user.avatar.url, '/media/avatars/sample.jpg')
        with self.assertRaises(User.DoesNotExist):
            User.objects.get(username='larrypage')

        os.remove(
            os.path.join(settings.BASE_DIR, 'twitter/media/avatars/sample.jpg'))            
            
    def test_update_user_profile_invalid_data(self):
        """Should not update user profile when given data is invalid"""
        # Preconditions
        self.assertEqual(self.user.username, 'larrypage')
            
        profile = self.app.get('/profile', user=self.user)
        form = profile.form
        form['username'] = 123
        with self.assertRaises(TypeError) as e:
            form.submit()
        self.assertTrue('expected string, int found' in e.exception.message)
        User.objects.get(username='larrypage')
        