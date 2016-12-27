from django.views.generic import View
from django.http import HttpResponse

class DefaultView(View):
    
    def get(self, request, *args, **kwargs):
        return HttpResponse('Sample Default View')