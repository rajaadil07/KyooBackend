from .models import Song
from .serializers import SongSerializer
from .spotify import get_access_token

from rest_framework import views, status
from rest_framework.response import Response

import requests

class SongAPIView(views.APIView):
    def get(self, request):
        query = request.GET.get('q')
        songs = Song.objects.all()
        if not query:
            serializer = SongSerializer(songs, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        url = 'https://api.spotify.com/v1/search'
        access_token = get_access_token()
        headers = {'Authorization': f'Bearer {access_token}'}
        params = {'q': query, 'type': 'track'}
        response = requests.get(url, headers=headers, params=params)

        if response.ok:
            results = response.json().get('tracks', {}).get('items', [])
            if not results:
                return Response({'error': 'No results found'}, status=status.HTTP_404_NOT_FOUND)

            song_data = results[0]  # Grabs the first match
            song = Song.objects.create(
                title=song_data.get('name', ''),
                artist=song_data.get('artists', [{}])[0].get('name', ''),
                album=song_data.get('album', {}).get('name', ''),
                release_year=song_data.get('album', {}).get('release_date', '')[:4],
                album_art=song_data.get('album', {}).get('images', [{}])[0].get('url', '')
            )
            serializer = SongSerializer(song)
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response({'error': 'Failed to retrieve results from the Spotify API'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)