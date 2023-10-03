from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path("blog/", views.index, name="main"),
    path("blog/post<int:id>", views.post, name="post"),
    path("about", views.about, name="about"),
    path("contacts", views.contacts, name="contacts"),
    path("services", views.services, name="services"),
    path('blog/category/<int:id>', views.category, name='category'),
    # path("<dynamic_url>", views.pro_url, name="test"),
    path('blog/search/', views.search, name="search"),
    path('blog/create/', views.create, name="create"),
    path('blog/comment/', views.comment, name="comment"),
    path('blog/login/', LoginView.as_view(),name = "blog_login"),
    path('blog/logout/', LogoutView.as_view(),name="blog_logout"),
    path('blog/profile/', views.profile, name="profile")
]
