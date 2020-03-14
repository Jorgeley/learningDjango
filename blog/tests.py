from django.test            import TestCase
from django.utils           import timezone
from django.core.exceptions import ValidationError
from calendar               import datetime
from blog.models            import Post

class PostTests(TestCase):

    #test case for publishing post in future date should raise an exception
    def test_future_publishing(self):
        next_month = timezone.now() + datetime.timedelta(days=30) #+30 days from now
        with self.assertRaises(ValidationError):
            Post(title='test', author='test', text='test invalid date', publishing=next_month)