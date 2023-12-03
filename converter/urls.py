from django.urls import path
from .views import UploadDataView

urlpatterns = [
    path('upload/', UploadDataView.as_view(), name='upload_data_view'),
    # other paths...
]
