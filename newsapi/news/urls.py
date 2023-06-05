from django.urls import path
from news.api.views import article_list_create_api_view, JournalistListCreateApiView, ArticleDetailApiView

urlpatterns = [
    path("articles/",article_list_create_api_view,name = "articles-list"),
    path("articles/<int:pk>/",ArticleDetailApiView.as_view(),name="article-detail"),
    path("journalists/",JournalistListCreateApiView.as_view(),name="journalist-list")
]