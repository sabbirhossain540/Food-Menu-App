from . import views
from django.urls import path

app_name = 'food'
urlpatterns = [
    path('', views.index, name='index'),
    #path('<int:item_id>/', views.details, name='details'),
    path('<int:pk>/',views.FoodDetail.as_view(),name='details'),
    path('item/', views.item, name='item'),
    #add
    path('add',views.CreateItem.as_view(),name='create_item'),
    #path('add', views.create_item, name='create_item'),
    #edit
    path('update/<int:id>/', views.update_item, name='update_item'),
    path('delete/<int:id>/', views.delete_item, name='delete_item'),
]
