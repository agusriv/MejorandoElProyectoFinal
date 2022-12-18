from django.urls import path
from appblog2.views import UserRegisterView, UserEditView, PasswordsCambiarView, ShowProfilePageView, EditProfilePageView, CreateProfilePgeView
from appblog2.views import password_succes


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edir_profile/', UserEditView.as_view(), name='edit_profile'),
    path('password/', PasswordsCambiarView.as_view(template_name='registration/change-password.html')),
    path('password_succes/', password_succes, name='password_success'),
    path('<pk>/perfil/', ShowProfilePageView.as_view(), name='show_profile'),
    path('<pk>/edit_perfil_page/', EditProfilePageView.as_view(), name='edit_profile_page'),
    path('create_perfil_page/', CreateProfilePgeView.as_view(), name='create_profile_page'),
]