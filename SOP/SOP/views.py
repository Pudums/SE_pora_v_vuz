from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from django.shortcuts import render
from django.views.generic import TemplateView
from SOP.models.models import User
from rest_framework.decorators import action


class ApiViewSet(ViewSet):
    def list(self, request=None):
        user = User.objects.all().filter(first_name=request.query_params.get('name')).first()
        if not user:
            return render(request, 'register.html')
        return render(request, 'index.html', {"name": user.first_name, "role": "Student" if user.is_student else "Teacher"})

    @action(url_path='register', methods=['get'], detail=False)
    def handler(self, request):
        print(request.query_params)
        user = User(first_name=request.query_params['name'],
                    last_name=request.query_params['last_name'],
                    is_student=request.query_params['student'] == '0', group_id=0)
        user.save()
        return render(request, 'index.html', {"name": user.first_name, "role": "Student" if user.is_student else "Teacher"})
