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
    path('myorders/<int:pk>', views.UzsakymasByUserDetailView.as_view(), name='mano_uzsakymas'),
    path('myorders/new', views.OrderByUserCreateView.as_view(), name='mano_uzsakymas_naujas'),
    path('myorders/<int:pk>/update', views.OrderByUserUpdateView.as_view(), name='my_order_update'),
    path('myorders/<int:pk>/delete', views.OrderByUserDeleteView.as_view(), name='my_order_delete'),
    path('register/', views.register, name='register'),
    path('profilis/', views.profilis, name='profilis'),

]