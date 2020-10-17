from django.urls import path
from blogapp import views

urlpatterns = [
    path('aboutus/', views.aboutus, name='aboutus'),
    path('contactus/', views.contactus, name='contactus'),
    path('', views.PostList.as_view(), name='home'),
    path('search/', views.SearchResultsView.as_view(), name='search_results'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
] 