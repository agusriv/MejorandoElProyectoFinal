from django.urls import path
from appblog.views import PostList, PostDetail, PostCreate, PostUpdate, PostDelate, CommentCreate, LikeView, contact



urlpatterns = [
    path('', PostList.as_view(), name="inicio"),
    path('contact/', contact, name="contact"),
    path('post/<pk>/', PostDetail.as_view(), name="detalle-post"),
    path('add_post/', PostCreate.as_view(), name="agregar-post"),
    path('editar/post/<pk>',PostUpdate.as_view(), name="actualizar-post" ),
    path("borrar/post/<pk>/", PostDelate.as_view(), name="borrar-post"),
    path('post/<pk>/comment/', CommentCreate.as_view(), name="agregar-comentario"),
    path('like/<pk>', LikeView, name="like_post"),
]