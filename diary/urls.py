from django.urls import path
from . import views

app_name = 'diary'

urlpatterns = [
    # 汎用的な呼び出しの場合は、クラス名.as_view()となる
    path('', views.IndexView.as_view(), name='index'),
    path('add/', views.AddView.as_view(), name='add'),
    path('update/<int:pk>/', views.UpdateView.as_view(), name='update'),
    path('delete/<int:pk>', views.DeleteView.as_view(), name='delete'),
    path('detail/<int:pk>', views.DetailView.as_view(), name='detail'),
]
