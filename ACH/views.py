from django.shortcuts import render

def show_index_html(request):
    return render(request, 'ACH/index.html')

def show_ai_info_html(request):
    return render(request, 'ACH/ai_info.html')