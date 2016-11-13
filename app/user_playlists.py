import pprint, sys, os
import subprocess

import spotipy
import spotipy.util as util


def get_playlists():
	username = "spotify"
	token = util.prompt_for_user_token(username)

	if token:
		sp = spotipy.Spotify(auth=token)
		playlists = sp.user_playlists(username)
		for playlist in playlists['items']:
			print(playlist['name'])
	else:
		print("Can't get token for", username)
