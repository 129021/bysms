from django.urls import path
from sales.views import listorders,listorders1,listorders2,listorders3,listorders4


urlpatterns = [


    path('orders/',listorders),
    path('orders1/',listorders1),
    path('orders2/',listorders2),
    path('orders3/',listorders3),
    path('orders4/',listorders4),

]