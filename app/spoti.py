import mood_analysis

#Playlist URIs
anger = "spotify:user:spotify:playlist:4qstWgP2KMRSiTY3a1fF2R"
disgust = "spotify:user:spotify:playlist:4dgsG6S4O8ZaTFk1gQWCk0"
fear = "spotify:user:spotify:playlist:1t9mj3y3HVmTf8QMfk4s2W"
joy = "spotify:user:spotify:playlist:65V6djkcVRyOStLd8nza8E"
sadness = "spotify:user:spotify:playlist:6ejgjp55cJWGzcDOp4HpGC"

def choose_playlist(emotion):
    if emotion == "Anger":
        return anger
    elif emotion == "Disgust":
        return disgust
    elif emotion == "Fear":
        return fear
    elif emotion == "Joy":
        return joy
    elif emotion == "Sadness":
        return sadness
    else:
        print("Playlist not found")