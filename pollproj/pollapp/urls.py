from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('index',views.home,name='home'),
    path('detail/<int:id>',views.detail,name='detail'),
    path('result/<int:id>',views.result,name='result'),
    path('<int:question_id>/vote/', views.vote, name ='vote'),

]