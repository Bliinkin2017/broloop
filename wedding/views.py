from django.shortcuts import render_to_response

def news(request):
    articles = [ {'content': 'First Article', 'author': 'Aaron', 'date': '2/23/2008'}, {'content': 'Second Article', 'author': 'Maria', 'date': '2/24/2008'} ]
    return render_to_response('news.html', {'article_list': articles, 'news': True})
