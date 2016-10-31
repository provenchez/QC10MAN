from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
import urllib2


from .models import Choice, Question

def index(request):
    return render(request, 'matchfetcher/index.html')

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'matchfetcher/detail.html', {'question': question})

def results(request):
    return render(request, 'matchfetcher/detail.html')

def getMatch(request):
    match_page = request.GET['matchPage']
    response = urllib2.urlopen('https://play.esea.net/index.php?s=stats&d=match&id=8177329')
    html = response.read()
    return HttpResponseRedirect(reverse('matchfetcher:index'))