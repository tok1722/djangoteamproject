from django.urls import path
from . import views

urlpatterns = [
    path('board/<int:pk>/', views.BoardDetail.as_view(), name='board_detail'),
    path('board/edit/<int:pk>/', views.board_edit, name='board_edit'),
    path('create/', views.create_board, name='create_board'),
    path('list/', views.board_list, name='board_list'),
]