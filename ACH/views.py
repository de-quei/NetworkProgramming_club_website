from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from ACH.models import Board


def show_index_html(request):
    return render(request, 'ACH/index.html')

def show_ai_info_html(request):
    return render(request, 'ACH/ai_info.html')

class BoardListView(ListView):
    model = Board

class BoardCreateView(CreateView):
    model = Board
    fields = '__all__'
    template_name_suffix = '_create'
    success_url = reverse_lazy('ACH:board_list')