from django.core.exceptions import FieldDoesNotExist
from django.test import TestCase
from .models import Editor, Article, tags
import datetime as dt

class EditorTestClass(TestCase):
    #SETUP METHOD
    def setUp(self):
        self.josephat = Editor(first_name = 'Josephat', last_name='Otieno', email='josephatotieno92@gmail.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.josephat, Editor))


    #testing the save method
    def test_save_method(self):
        self.josephat.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors)>0)

class ArticleTestCase(TestCase):
    def setUp(self):
        self.josephat=Editor(first_name="josephat",last_name="otieno", email="josephatotieno92@gmail.com")
        self.josephat.save_editor()

        #creatig a new tag and saving it
        self.new_tag = tags(name = 'testing')
        self.new_tag.save()

        self.new_article = Article(title = "Test case", post="This is a random post", editor= self.josephat)
        self.new_article.save()
        self.new_article.tags.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Article.objects.all().delete()
    
    def test_get_news_today(self):
        today_news = Article.today_news()
        self.assertTrue(len(today_news)>0)

    def get_news_by_date(self):
        test_date = '2020-04-20'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        news_by_date = Article.days_news(date)
        self.assertTrue(len(news_by_date)==0)