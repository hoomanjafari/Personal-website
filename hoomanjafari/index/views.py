from django.shortcuts import render
from django.views import View


class Home(View):
    def get(self, request):
        return render(request, 'index/index.html')


class SearchView(View):
    def get(self, request):
        return render(request, 'index/search_page.html')
