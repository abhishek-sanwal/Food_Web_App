
from django.urls import path
from . import views

# Registering namespace for food app

app_name = "food"

'''
These are the url patterns. Django search urls from these patterns 
'''
urlpatterns = [
    
    path('',views.show,name = "show"),
    path('<int:item_id>/', views.display_item, name="display"),
    path('add',views.add_item,name ="add"),
    path('update/<int:item_id>/',views.update_item,name = "update"),
    path('delete<int:item_id>/',views.delete_item,name="delete")
]