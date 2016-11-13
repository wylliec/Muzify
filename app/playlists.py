import sys, os, pprint
import subprocess
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

def get_playlist_tracks(emotion):
	token = util.prompt_for_user_token(username)
	tracks = None
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
	return tracks

# Returns random 30s preview from tracks
def get_random_preview(tracks):
	# Array of 30s preview URLs from tracks
	urls = get_preview_urls(tracks)
	# print('length of all urls:', len(urls))
	# Removes None values
	clean_urls = [x for x in urls if x != None]
	# print('length of clean urls:', len(clean_urls))
	# Randomly chooses index of tracks
	index = randint(0, len(clean_urls) - 1)
	# Returns random index from URLs
	# print(clean_urls)
	return clean_urls[index]

# Returns array of 30s preview URLs from tracks
def get_preview_urls(tracks):
	urls = []
	for track in tracks['items']:
		# print(track['track']['preview_url'])
		urls.append(track['track']['preview_url'])
	return urls

def play_song(emotion):
	# Tracks from playlist corresponding to given emotion
	tracks = get_playlist_tracks(emotion)
	# Returns random 30s preview from tracks
	return get_random_preview(tracks)
