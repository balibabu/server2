from django.urls import path
from . import views,viewsFolder
from .shared import viewShare

urlpatterns = [
    path('upload/',views.uploadFile,name='uploadFile'),
    path('delete/<int:id>/',views.deleteFile,name='deleteFile'),
    path('download/<int:id>/',views.downloadFile,name='downloadFile'),
    path('file/<int:pk>/',views.UpdateFileView.as_view(),name='file-update'),

    path('filesAndFolders/',viewsFolder.getFilesAndFolders,name='user-info'),
    path('folder/',viewsFolder.FolderListCreateView.as_view(),name='folder-create-list'),
    path('folder/<int:pk>/',viewsFolder.FolderUpdateDeleteView.as_view(),name='folder-update-delete'),

    path('share/',viewShare.shareFile,name='shareFile'),
    path('revoke/<int:id>/',viewShare.removePermission,name='removePermission'),
    path('dsf/<str:id>/',viewShare.downloadSharedFile,name='downloadSharedFile'),
]
