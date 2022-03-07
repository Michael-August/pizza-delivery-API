from django.urls import path
from . import views

urlpatterns = [
    path('', views.OrderCreateListView.as_view(), name='orders'),
    path('<int:order_id>/', views.OrderDetailView.as_view(), name='order_detail'),
    path('update-status/<int:order_id>', views.UpdateOrderStatus.as_view(), name='order_status_update'),
    path('user/<int:user_id>', views.UserOrdersView.as_view(), name='user_orders'),
    path('user/<int:user_id>/<int:order_id>', views.UserOrderDetail.as_view(), name='user_order'),
]
