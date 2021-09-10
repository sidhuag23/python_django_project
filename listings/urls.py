from django.urls import path

from . import views 
#/listings/id
urlpatterns=[

   path('',views.index,name='listings'),
   path('<int:listing_id>',views.listing,name='listing'),
   path('search.html',views.search,name='search'),

]