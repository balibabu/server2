from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import PhotoSerializer
from .models import Photo
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import status
from git.extra.fileManager import FileManager
from .utility.thumbnail import Thumbnail


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def getPhotos(request):
    user=request.user
    photos=Photo.objects.filter(user=user).order_by('id')
    serializer=PhotoSerializer(photos,many=True)
    return Response(serializer.data)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def upload(request):
    user=request.user
    file = request.FILES.get('file')
    fileContent=file.read()
    fm=FileManager(user.username)
    original=fm.upload(fileContent,file.name)
    img=Thumbnail(fileContent)
    thumnail=fm.upload(img.thumbnail(),file.name)
    width,height=img.resolution()
    serializer=PhotoSerializer(data={'width':width,'height':height})
    if serializer.is_valid():
        serializer.save(user=user,original=original,thumnail=thumnail)
        return Response(serializer.data)
    else:
        return Response(serializer.errors)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def download(request,id,typ):
    user=request.user
    photo=Photo.objects.get(id=id)
    if typ==1:
        fileInfo=photo.original
    else:
        fileInfo=photo.thumbnail
    fm=FileManager(user.username)
    file_content=fm.download(fileInfo)
    response = HttpResponse(file_content, content_type='application/octet-stream')
    return response


@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def deletePhoto(request,id): 
    user=request.user
    photo=Photo.objects.get(id=id)
    fm=FileManager(user.username)
    fm.delete(photo.original) # photo cascade w.r.t original/thumbnail
    fm.delete(photo.thumbnail)
    return Response(status=status.HTTP_204_NO_CONTENT)
