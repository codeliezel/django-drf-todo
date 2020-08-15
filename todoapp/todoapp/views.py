from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import NoteModel
from .serializers import NoteSerializer

class NoteView(APIView):

    """
    Create a new note
    """
    
    def post(self, request):
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    """
    Get all notes
    """

    def get(self, request):
        notes = NoteModel.objects.all()
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class NoteDetailView(APIView):

    """
    Get a note
    """
    
    def get_object(self, pk):
        try:
            return NoteModel.objects.get(pk=pk)
        except NoteModel.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        note = self.get_object(pk)
        serializer = NoteSerializer(note)
        return Response(serializer.data)
     
    """
    Update a note
    """

    def put(self, request, pk, format=None):
        note = self.get_object(pk)
        serializer = NoteSerializer(note, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
    
    """
    Delete a note
    """

    def delete(self, request, pk, format=None):
        note = self.get_object(pk)
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)        