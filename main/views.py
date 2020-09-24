from django.http import Http404
from .models import FormFile
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class FormFileList(APIView):
    def get(self, request):
        form_files = FormFile.objects.all()
        serializer = FormFileSerializer(form_files, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FormFileSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            response_data = {
                "id": serializer.data["id"],
                "file": "http://147.139.7.242" + serializer.data["file"]
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FormFileDetail(APIView):
    def get_object(self, pk):
        try:
            return FormFile.objects.get(pk=pk)
        except:
            return Http404

    def get(self, request, pk):
        form_file = self.get_object(pk)
        serializer = FormFileSerializer(form_file)
        response_data = {
            "id": serializer.data["id"],
            "file": "http://147.139.7.242" + serializer.data["file"]
        }
        return Response(response_data)

    def delete(self, request, pk):
        form_file = get_object(pk)
        form_file.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)