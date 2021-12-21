from django.urls import path
from . import views

urlpatterns =[
    path('add/',views.LaptopCreateView.as_view(),name='lap_add'),
    path('list/',views.LaptopListView.as_view(),name='lap_list'),
    path('update/<int:pk>/',views.LaptopUpdateView.as_view(),name='update'),
    path('delete/<int:pk>',views.LaptopDeleteView.as_view(),name='delete'),
]