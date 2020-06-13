from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


from dataapp.models import File
from django.shortcuts import render
from django.views import View


class ViewProfile(View):
    def get(self, request):
        html = 'index.html'
        data = File.objects.all()
        return render(
            request,
            html,
            {'data': data}
        )

