from django.shortcuts import render
from django.views import View
from .models import MyCv


class CvView(View):
    def get(self, request):
        cv = MyCv.objects.all()
        return render(request, 'cv/cv.html', {'cv': cv})
