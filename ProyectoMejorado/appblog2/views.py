from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import DetailView, CreateView
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from appblog2.forms import SignUpForm, EditProfileForm, PasswordChangingForm, PerfilPageForm
from appblog.models import Perfil


class ShowProfilePageView(DetailView):

    model = Perfil
    template_name = 'registration/user_profile.html'


    def get_context_data(self, *args, **kwargs):
        
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        
        page_user = get_object_or_404(Perfil, id=self.kwargs["pk"])

        context["page_user"] = page_user
        return context


class PasswordsCambiarView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('password_success')

def password_succes(request):
    return render(request, 'registration/password_succes.html', {})
    
class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('inicio')

    def get_object(self):
        return self.request.user

class EditProfilePageView(generic.UpdateView):

    model = Perfil
    form_class = PerfilPageForm
    template_name = 'registration/edit_profile_page.html'
    #fields = ['user', 'bio', 'perfil_imagen', 'Instagram_url', 'github_url', 'fb_url', 'web_url', 'Twitter_url']
    success_url = reverse_lazy('inicio')

class CreateProfilePgeView(CreateView):
    model = Perfil
    form_class = PerfilPageForm
    template_name = "registration/create_user_profile_page.html"
    #fields = '__all__'

    def form_invalid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
