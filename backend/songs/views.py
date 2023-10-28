from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .spotify_helper import search_track
from .serializers import SongSerializer

class SongSearchView(APIView):
    def get(self, request):
        query = request.GET.get('query')
        if not query:
            return Response({'error': 'Query parameter is missing'}, status=status.HTTP_400_BAD_REQUEST)

        songs = search_track(query)
        if songs:
            song = songs[0]
            serializer = SongSerializer(song)
            return Response(serializer.data)
        else:
            return Response([])
