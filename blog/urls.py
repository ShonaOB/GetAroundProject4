from django.urls import path
from . import views


urlpatterns = [
    path('', views.ReviewList.as_view(), name='home'),
    path('search/', views.SearchList.as_view(), name='search_results'),
    path('views/', views.PostCreateView.as_view(), name='post_form'),
    path('views/edit/<slug:slug>', views.UpdatePostView.as_view(), name='update_post'),
    path('views/delete/<slug:slug>', views.DeletePostView.as_view(), name='delete_post'),
    path('<slug:slug>/', views.ReviewDetail.as_view(), name='review_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),

]
