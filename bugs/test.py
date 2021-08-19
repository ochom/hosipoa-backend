from .models import Bug, Replies
from django.test import TestCase


class BugTestCase(TestCase):
    def setUp(self):
        bug = Bug.objects.create(
            title="Bug test",
            description="test desc",
            is_resolved=True
        )

        reply = Replies.objects.create(bug=bug, reply="Test reply")

    def test_Bug_created(self):
        bug = Bug.objects.get(title="Bug test")
        self.assertEqual(bug.is_resolved, True)

    def test_replies(self):
        reply = Replies.objects.get(reply="Test reply")
        self.assertEqual(reply.bug.title, "Bug test")
