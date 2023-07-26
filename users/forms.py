from django import forms


class LoginForm(forms.Form):
    """
    用户登录表单检查
    """
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=5)
