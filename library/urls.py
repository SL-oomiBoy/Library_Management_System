
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('books/', views.book_list, name='book_list'),
    path('books/<int:pk>/', views.book_detail, name='book_detail'),
    path('books/new/', views.book_create, name='book_create'),
    path('books/<int:pk>/edit/', views.book_update, name='book_update'),
    path('books/<int:pk>/delete/', views.book_delete, name='book_delete'),

    path('members/', views.member_list, name='member_list'),
    path('members/<int:pk>/', views.member_detail, name='member_detail'),
    path('members/new/', views.member_create, name='member_create'),
    path('members/<int:pk>/edit/', views.member_update, name='member_update'),
    path('members/<int:pk>/delete/', views.member_delete, name='member_delete'),

    path('borrow_records/', views.borrow_record_list, name='borrow_record_list'),
    path('borrow_records/<int:pk>/', views.borrow_record_detail, name='borrow_record_detail'),
    path('borrow_records/new/', views.borrow_record_create, name='borrow_record_create'),
    path('borrow_records/<int:pk>/edit/', views.borrow_record_update, name='borrow_record_update'),
    path('borrow_records/<int:pk>/delete/', views.borrow_record_delete, name='borrow_record_delete'),
]
