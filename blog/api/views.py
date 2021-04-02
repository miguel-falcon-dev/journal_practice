from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
import blog.models as b_mdls
from blog.api.serializers import EntrySerializer

class EntriesListApiView(APIView):
    def get(self, request, *args, **kwargs):
        entries = b_mdls.Entry.objects
        serializer = EntrySerializer(entries, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        data = {
            'creation_date': request.data.get('creation_date'),
            'updated_date': request.data.get('updated_date'),
            'feeling': request.data.get('feeling'),
            'description': request.data.get('description'),
            'photo': request.data.get('photo'),
        }
        serializer = EntrySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EntryDetailApiView(APIView):
    def get_object(self, entry_id):
        try:
            return b_mdls.Entry.objects.get(id=entry_id)
        except b_mdls.Entry.DoesNotExist:
                return None

    def get(self, request, entry_id, *args, **kwargs):
        entry_instance = self.get_object(entry_id)
        if not entry_instance:
            return Response(
                {"res": "Object with entry id does not exists"},status=status.HTTP_400_BAD_REQUEST
            )
        
        serializer = EntrySerializer(entry_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, entry_id, *args, **kwargs):
        entry_instance = self.get_object(entry_id)
        if not entry_instance:
            return Response(
                {"res": "Object with entry id does not exists"},status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'creation_date': request.data.get('creation_date'),
            'updated_date': request.data.get('updated_date'),
            'feeling': request.data.get('feeling'),
            'description': request.data.get('description'),
            'photo': request.data.get('photo'),
        }
        serializer = EntrySerializer(instance = entry_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, entry_id, *args, **kwargs):
        entry_instance = self.get_object(entry_id)
        if not entry_instance:
            return Response(
                {"res": "Object with entry id does not exists"},status=status.HTTP_400_BAD_REQUEST
            )
        entry_instance.delete()
        return Response ({"res": "Object deleted!"}, status=status.HTTP_200_OK)