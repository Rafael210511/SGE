from django.urls import path
from . import views


urlpatterns = [
    path('inflow/list', views.InflowListView.as_view(), name='inflow_list'),
    path('inflow/create/', views.InflowCreateView.as_view(), name='inflow_create',),
    path('inflow/<int:pk>/detail/', views.InflowDetailView.as_view(), name='inflow_detail'),

    path('api/v1/inflows/', views.InflowCreateListAPIView.as_view(), name='inflow-create-list-api-view'),
    path('api/v1/inflows/<int:pk>/', views.InflowRetrieveAPIView.as_view(), name='inflow-detail-api-view'),
]
