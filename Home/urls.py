from django.urls import path
from .import views
urlpatterns =[
    path('',views.index,name='index'),
    path('mobile',views.mobile,name='mobile'),
    path('laptop',views.laptop,name='laptop'),
    path('television',views.television,name='television'),
    path('headphone',views.headphone,name='headphone'),
    path('camera',views.camera,name='camera'),
    path('washingmachine',views.washingmachine,name='washingmachine'),
    path('refrigerator',views.refrigerator,name='refrigerator'),
    path('tablet',views.tablet,name='tablet'),
    path('airconditioner',views.airconditioner,name='airconditioner'),
    path('fashion/<str:tp>',views.fashion,name='fashion'),
    path('books',views.books,name='books'),
    path('mobadvt',views.mobadvt,name='mobadvt'),
    path('fashadvt',views.fashadvt,name='fashadvt'),
    path('electronicadvt',views.electronicadvt,name='electronicadvt'),
    path('appadvt',views.appadvt,name='appadvt'),
]