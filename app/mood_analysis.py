from app.watson import get_sentiments

#Gets the score of a specific emotion in the emotion dictionary
def get_score(emotion, emotion_dict):
    return emotion_dict[emotion]

#Finds the emotion with the highest certainty score
def get_max_emotion(emotion_dict):
    return max(emotion_dict, key=lambda emotion: get_score(emotion, emotion_dict))

#Finds the inner product of each playlist
def emotion_ip(emotion_dict, playlist_scores):
    emotions = ['Anger', 'Disgust', 'Fear', 'Joy', 'Sadness']
    emotion_subproducts = []
    for emotion in emotions:
        emotion_subvalue.append(get_score(emotion, emotion_dict) * get_score(emotion, playlist_scores)) 
    return sum(emotion_subproducts)

#Returns the playlist with the highest inner product
def best_matching_playlist(emotion_dict, playlists):
    best_list = None
    last_score = None
    for playlist in playlists:
        curr_score = emotion_ip(emotion_dict, playlist)
        if best_list == None:
            best_list = playlist
        elif curr_score > last_score:
            best_list = playlist
        last_score = curr_score
    return best_list

