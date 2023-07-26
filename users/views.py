from django.shortcuts import render, redirect
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.db.models import Q
from django.views.generic import View
from users.models import UsersModel
from users.forms import LoginForm


class CustomBackend(ModelBackend):
    """
    auth模块 表单自定义验证逻辑
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UsersModel.objects.get(Q(username=username) | Q(email=username))
            # 检查加密密码
            if user.check_password(password):
                return user
        except Exception as e:
            print(e)
            return None


class UserLoginView(View):
    """
    用户登录逻辑
    """

    def get(self, request):
        return render(request, 'login.html', {})

    def post(self, request):
        # 交给Form检查表单 -> authenticate验证身份 -> 登录(调用login)
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            email = request.POST.get("email", "")
            password = request.POST.get("password", "")
            # 验证记录
            user = authenticate(username=email, password=password)
            if user is not None:
                # 登录成功
                login(request, user)
                return JsonResponse({"status": "success"})
            else:
                return JsonResponse({"status": "failed"})
        else:
            return JsonResponse({"status": "form"})


class UserLogoutView(View):
    """
    用户注销逻辑
    """

    def get(self, request):
        logout(request)
        return redirect("users:login")
