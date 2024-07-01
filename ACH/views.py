from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from ACH.models import Board, CreativeAI


def show_index_html(request):
    return render(request, 'ACH/index.html')

def show_ai_info_html(request):
    ai_list = CreativeAI.objects.all()  # CreativeAI 모델의 모든 객체를 가져옴
    return render(request, 'ACH/ai_info.html', {'ai_list': ai_list})

class BoardListView(ListView):
    model = Board

class BoardCreateView(CreateView):
    model = Board
    fields = '__all__'
    template_name_suffix = '_create'
    success_url = reverse_lazy('ACH:board_list')