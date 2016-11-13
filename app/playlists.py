import sys, os
import spotipy
import spotipy.util as util

from random import randint

#User ID
username = 'spotify'

#Playlist IDs
anger = "4qstWgP2KMRSiTY3a1fF2R"
disgust = "4dgsG6S4O8ZaTFk1gQWCk0"
fear = "1t9mj3y3HVmTf8QMfk4s2W"
joy = "65V6djkcVRyOStLd8nza8E"
sadness = "6ejgjp55cJWGzcDOp4HpGC"

# tracks = 

def get_playlist_tracks(emotion):
	token = util.prompt_for_user_token(username)
	if token:
		sp = spotipy.Spotify(auth=token)
		if emotion == "Anger":
			tracks = sp.user_playlist_tracks(username, playlist_id=anger)
		elif emotion == "Disgust":
			tracks = sp.user_playlist_tracks(username, playlist_id=disgust)
		elif emotion == "Fear":
			tracks = sp.user_playlist_tracks(username, playlist_id=fear)
		elif emotion == "Joy":
			tracks = sp.user_playlist_tracks(username, playlist_id=joy)
		elif emotion == "Sadness":
			tracks = sp.user_playlist_tracks(username, playlist_id=sadness)
		else:
			print("Playlist for " + emotion + " not found for " + username)
		return(tracks)

# Returns random 30s preview from tracks
def get_random_preview(tracks):
	# Array of 30s preview URLs from tracks
	urls = get_preview_urls(tracks)
	# Randomly chooses index of track
	size = get_size(playlist)
	index = randint(0, size - 1)
	# Returns random index from URLs
	return urls[index]

# Returns array of 30s preview URLs from tracks
def get_preview_urls(tracks):
	urls = []
	for track in tracks['items']:
		urls.append(track.preview_url)

# Returns number of tracks in playlist
def get_size(playlist):
	return playlist['total']

def play_song(emotion):
	# Tracks from playlist corresponding to given emotion
	tracks = get_playlist_tracks(emotion)
	# Returns random 30s preview from tracks
	return get_random_preview(tracks)
