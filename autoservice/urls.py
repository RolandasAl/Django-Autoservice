from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('automobiliai/', views.automobiliai, name='automobiliai'),
    path('automobiliai/<int:masina_id>', views.automobilis, name='automobilis'),
    path('uzsakymai/', views.Uzsakymai.as_view(), name='uzsakymai'),
    path('uzsakymai/<int:pk>', views.Uzsakymo_info.as_view(), name='uzsakymo_info'),
    path('search/', views.search, name='search'),
    path('myorders/', views.User_uzsakymas.as_view(), name='mano_uzsakymai'),
    path('register/', views.register, name='register')

]