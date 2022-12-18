from django.test import TestCase
from django.test import Client
#用来写测试
# Create your tests here.
from django.utils import timezone
from polls.models import Question
from polls.models import Choice

class IndexTestCase(TestCase):
    def setUp(self):
        Question.objects.create(id=1,question_text="what is new?",pub_date=timezone.now())
        Choice.objects.create(id=1,choice_text="Not much",votes=0,question_id=1)
        Choice.objects.create(id=2,choice_text="The SKY",votes=888,question_id=1)

    def test_index_page(self):
        c=Client()
        response = c.get("/polls/")
        print(response.status_code)
        # self.assertEqual(response.status_code,200)
        # self.assertIn(b"what is new?" ,response.content)
        self.assertTemplateUsed(response,'polls/index.html')

    def test_detail_page(self):
        c=Client()
        response = c.get("/polls/1/")
        self.assertEqual(response.status_code,200)
        self.assertIn(b"what is new?" ,response.content)
        self.assertIn(b"Not much" ,response.content)
        self.assertIn(b"The SKY" ,response.content)
        self.assertTemplateUsed(response,'polls/detail.html')

    def test_result_page(self):
        c=Client()
        response = c.get("/polls/1/results/")
        self.assertEqual(response.status_code,200)
        self.assertIn(b"what is new?" ,response.content)
        self.assertIn(b"Not much" ,response.content)
        self.assertIn(b"The SKY" ,response.content)
        self.assertIn(b"888" ,response.content)
        self.assertTemplateUsed(response,'polls/results.html')
    def test_vote_page(self):
        c=Client()
        response = c.post("/polls/1/vote/",data={"choice":2})
        self.assertEqual(response.status_code,302)
        response = c.get("/polls/1/results/")
        self.assertEqual(response.status_code,200)
        self.assertIn(b"889" ,response.content)
