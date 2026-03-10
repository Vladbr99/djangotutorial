from django.test import TestCase
from polls.models import Question
from django.utils import timezone
from datetime import timedelta

class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        future_time = timezone.now() + timedelta(days=30)
        future_question = Question(pub_date=future_time)
        self.assertFalse(future_question.was_published_recently())

    def test_was_published_recently_with_recent_question(self):
        recent_time = timezone.now() - timedelta(hours=1)
        recent_question = Question(pub_date=recent_time)
        self.assertTrue(recent_question.was_published_recently())
    
