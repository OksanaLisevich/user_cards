from .forms import CardSumForm, CardForm
from django.shortcuts import render, redirect
from .models import Card, CardSum
from django.db.models import Sum
from django.views.decorators.csrf import csrf_exempt


def index(request):
    all_cards = Card.objects.all().annotate(card_total_sum=Sum('cardsum__sum'))
    card_form = CardForm()
    context = {
        'all_cards': all_cards,
        'card_form': card_form
    }
    return render(request, 'index.html', context)


@csrf_exempt
def add_sum(request):
    if request.POST:
        card_sum_form = CardSumForm(request.POST)
        if card_sum_form.is_valid:
            card_sum_form.save()
            return redirect("/user_cards")

    return redirect("/user_cards")


@csrf_exempt
def add_card(request):
    if request.POST:
        card_form = CardForm(request.POST)
        if card_form.is_valid:
            card_form.save()
    return redirect("/user_cards")
