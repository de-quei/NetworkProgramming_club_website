from django.shortcuts import render
from django.views.generic import ListView

from ACH.models import Board


def show_index_html(request):
    return render(request, 'ACH/index.html')

def show_ai_info_html(request):
    return render(request, 'ACH/ai_info.html')

class BoardListView(ListView):
    model = Board