from django.urls import path
from children import views

urlpatterns = [
    path('children/', views.ChildrenList.as_view()),
    path('children/<int:pk>/', views.ChildrenDetail.as_view()),
]
