from rest_framework import serializers
from songs.models import Songs, SongsFixed

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Songs
        fields = ['input_link', 'output_link', 'ranking', 'user_played', 'time_stamp']

class FixedSongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SongsFixed
        fields = ['song_path']