from django.shortcuts import render
from django.views.generic import View


class UploadPhotoView(View):

    def get(self, request):
        return render(request, 'upload_photo.html')
