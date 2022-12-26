from django.urls import path
from .views import  (CreateItem, ListDisplay, AboutUs, AirdropView, 
                     CreateAirdrop, MyDetailView, UpdateViewAirDrop, DeleteAirDrop)
urlpatterns = [
    path('', ListDisplay.as_view(), name='home' ),
    
    path('contact/', CreateItem.as_view(), name='contact' ),
    path('about/', AboutUs.as_view(), name='about' ),
    path('airdrop/', AirdropView.as_view(), name='airdrop'),
    path('airdrop/<int:pk>/', MyDetailView.as_view(), name='airdrop_details'),
    path('update/<int:pk>/', UpdateViewAirDrop.as_view(), name='airdrop_update'),
    path('delete/<int:pk>/', DeleteAirDrop.as_view(), name='airdrop_delete'),
    path('create/', CreateAirdrop.as_view(), name='create_new'),
    
    
        
        
    
    ]