from django.urls import path, include
# from .views import article_list, article_detail, ArticleAPIView, ArticleDetails
# from .views import ArticleAPIView, ArticleDetails, GenericAPIView, ArticleViewSet
from .views import ArticleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('articles', ArticleViewSet, basename='article')

urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>', include(router.urls)),
    # path('articles', article_list),
    # path('articles/<int:pk>', article_detail),
    # path('articles', ArticleAPIView.as_view()),
    # path('articles/<int:article_id>', ArticleDetails.as_view()),
    # path('generic/articles', GenericAPIView.as_view()),
    # path('generic/articles/<int:id>', GenericAPIView.as_view()),
]
