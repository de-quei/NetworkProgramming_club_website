from django.shortcuts import render

def show_index_html(request):
    return render(request, 'ACH/index.html')