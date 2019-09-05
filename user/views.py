from django.shortcuts import render

# Create your views here.
from django.views import View


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        error_msg = '用户名或口令出错'
        return render(request, 'login.html', locals())