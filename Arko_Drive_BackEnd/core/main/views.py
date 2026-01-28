from django.shortcuts import render, get_object_or_404, redirect
from .models import Test, TheoryGroup, SignGroup, Package, CarItem, ValueItem, HistoryItem

def index(request):
    return render(request, 'index.html')

def tests_list(request):
    tests = Test.objects.all()
    return render(request, 'tests.html', {'tests': tests})

def test_detail(request, pk):
    test = get_object_or_404(Test, pk=pk)
    return render(request, 'test_detail.html', {'test': test})

def theory_list(request):
    groups = TheoryGroup.objects.all()
    return render(request, 'theory.html', {'groups': groups})

def theory_detail(request, pk):
    group = get_object_or_404(TheoryGroup, pk=pk)
    return render(request, 'theory_detail.html', {'group': group})

def trafficsigns(request):
    groups = SignGroup.objects.all()
    return render(request, 'trafficsigns.html', {'sign_groups': groups})

def packages_view(request):
    packages_full = Package.objects.filter(category='full')
    packages_theory = Package.objects.filter(category='theory')
    packages_practical = Package.objects.filter(category='practical')
    return render(request, 'packages.html', {
        'packages_full': packages_full,
        'packages_theory': packages_theory,
        'packages_practical': packages_practical,
    })

def about_view(request):
    car_items = CarItem.objects.all()
    value_items = ValueItem.objects.all()
    history_items = HistoryItem.objects.all()
    return render(request, 'about.html', {
        'car_items': car_items,
        'value_items': value_items,
        'history_items': history_items,
    })

from .models import Question, Answer
import random

def random_question_view(request):
    questions = list(Question.objects.prefetch_related('answers').all())
    step = int(request.GET.get("step", 0))

    if not questions:
        return render(request, 'random_question.html', {'no_questions': True})

    if step < 0:
        step = 0
    if step >= len(questions):
        step = len(questions) - 1

    question = questions[step]
    selected_id = None
    answered = False

    if request.method == "POST":
        selected_id = int(request.POST.get("answer", -1))
        answered = True

    return render(request, 'random_question.html', {
        'question': question,
        'step': step,
        'answered': answered,
        'selected_id': selected_id,
    })

