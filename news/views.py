
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
import datetime as dt
from .models import Article
# Create your views here.

def welcome(request):
    return render(request, 'welcome.html')

def news_of_day(request):
    date = dt.date.today()
    news = Article.today_news()
    
    #function to convert date object to find exact day

    return render(request, 'all-news/today-news.html', {"date": date, "news":news})

# def convert_dates(dates):
#     #function that gets the weekday number for the date.
#     day_number = dt.date.weekday(dates)

#     days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

#     #returnnig the actual day of the week

#     day = days[day_number]

#     return day

def past_days_news(request, past_date):
    #Converts a date from the string url
    try:
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()

    except ValueError:
        #raise 404 error when valueError is thronw
        raise Http404()
        assert False

    if date==dt.date.today():
        return redirect(news_of_day)
     
    news = Article.days_news(date)

   
    return render (request, 'all-news/past-news.html', {"date": date,"news":news})

def search_results(request):
    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_articles = Article.search_by_title(search_term)
        message = f"{search_term}"

        return render (request, 'all-news/search.html', {"messge":message, "articles":searched_articles})

    else:
        message = "you haven't searhed for any term"
        return render (request, 'all-news/search.html', {"message":message})

def article(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
    except Article.DoesNotExist:
        raise Http404()
    return render(request,"all-news/article.html", {"article":article})

