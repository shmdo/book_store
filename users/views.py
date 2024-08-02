from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from .forms import UserRegistrationForm, UserLoginForm
from .models import CustomUser


class UserRegistrationView(FormView):
    template_name = 'auth/register.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.email = form.cleaned_data.get('email')
        user.user_type = form.cleaned_data.get('user_type')
        if user.user_type == 'author':
            user.is_staff = True
        user.save()
        login(self.request, user)
        return super().form_valid(form)


class UserLoginView(LoginView):
    template_name = 'auth/login.html'
    form_class = UserLoginForm

    def get_success_url(self):
        return reverse_lazy('index')


class UserLogoutView(LogoutView):
    template_name = 'auth/logout.html'

    def get_success_url(self):
        return reverse_lazy('index')

# from django.shortcuts import render, redirect
# from django.views import View
# from django.contrib.auth.models import User
# from .forms import UserRegistrationForm, UserLoginForm
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth import login, logout
#
#
# class RegisterView(View):
#     def get(self, request):
#         return render(request, 'auth/register.html')
#
#     def post(self, request):
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         email = request.POST['email']
#         username = request.POST['username']
#         password_1 = request.POST['password_1']
#         password_2 = request.POST['password_2']
#         if password_1 == password_2:
#             user = User(first_name=first_name, last_name=last_name, email=email, username=username)
#             user.set_password(password_1)
#             user.save()
#             return redirect('login')
#         else:
#             return render(request, 'auth/register.html')
#
#
# class LoginView(View):
#     def get(self, request):
#         form = UserLoginForm()
#         context = {'form': form}
#         return render(request, 'auth/login.html', context)
#
#     def post(self, request):
#         username = request.POST['username']
#         password_1 = request.POST['password_1']
#
#         data = {
#             'username': username,
#             'password': password_1
#         }
#
#         login_form = AuthenticationForm(data=data)
#         if login_form.is_valid():
#             user = login_form.get_user()
#             login(request, user)
#             return redirect('index')
#
#         else:
#             form = UserLoginForm()
#             context = {'form': form}
#             return render(request, 'auth/login.html', context)
#
#
# class LogoutView(View):
#     def get(self, request):
#         logout(request)
#         return redirect('index')
#

