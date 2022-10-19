from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from django.shortcuts import render
from django.views.generic import TemplateView

class MyView(TemplateView):
    pass
class ApiViewSet(ViewSet):
    def list(self, request=None):
        return render(request, 'SOP/templates/index.templates')
