from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from appblog.models import Post
from django.urls import reverse_lazy, reverse
from appblog.models import Comment
from appblog.forms import CommentForm, PostForm, EditForm
from django.http import HttpResponseRedirect

def about(request):
   return render(request, "appblog/about.html")


class PostList(ListView):
    model = Post
    template_name = 'appblog/inicio.html'

class PostDetail(DetailView):
   model = Post
   template_name = 'appblog/detail_post.html'

   def get_context_data(self, *args, **kwargs):
       context = super(PostDetail, self).get_context_data()
       stuff = get_object_or_404(Post, id=self.kwargs['pk'])
       total_likes = stuff.TotalLikes()
       
       liked = False
       if stuff.likes.filter(id=self.request.user.id).exists():
        liked = True
       context["total_likes"] = total_likes
       context["liked"] = liked
       return context

class PostCreate( CreateView):
    model = Post
    form_class = PostForm
    #success_url = ""
    #fields = "__all__"
    template_name = "appblog/Post_form.html"


class PostUpdate( UpdateView):
    model = Post
    form_class = EditForm
    success_url = ""
    #fields = "__all__"

class PostDelate( DeleteView):  
    model = Post
    template_name = "appblog/Post_confirm_delete.html"
    success_url = reverse_lazy("inicio")
    
   
class CommentCreate( CreateView):

    model = Comment
    form_class = CommentForm
    template_name = "appblog/add_comment.html"

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    success_url = reverse_lazy("inicio")

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('detalle-post', args=[str(pk)]))
