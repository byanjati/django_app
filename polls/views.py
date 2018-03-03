from django.shortcuts import render, get_object_or_404
from .models import Question


def index(request):
    questions = Question.objects.all()
    context = { 'questions': questions }
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    return render(request, 'polls/detail.html', {'question': question})
