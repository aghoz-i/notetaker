from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Note
from .serializers import NoteSerializer
from .schemas import (
    note_list_get_schema,
    note_list_post_schema,
    note_detail_get_schema,
    note_detail_put_schema,
    note_detail_delete_schema
)

class NoteListView(APIView):

    @note_list_get_schema
    def get(self, request):
        notes = Note.objects.all()
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)
    
    @note_list_post_schema
    def post(self, request):
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class NoteDetailView(APIView):
    @note_detail_get_schema
    def get(self, request, pk):
        try:
            note = Note.objects.get(pk=pk)
            serializer = NoteSerializer(note)
            return Response(serializer.data)
        except Note.DoesNotExist:
            return Response({"detail": "Note not found"}, status=404)
    
    @note_detail_put_schema
    def put(self, request, pk):
        try:
            note = Note.objects.get(pk=pk)
            serializer = NoteSerializer(note, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        except Note.DoesNotExist:
            return Response({"detail": "Note not found"}, status=404)
    
    @note_detail_delete_schema
    def delete(self, request, pk):
        try:
            note = Note.objects.get(pk=pk)
            note.delete()
            return Response(status=204)
        except Note.DoesNotExist:
            return Response({"detail": "Note not found"}, status=404)