playlist = {
    'title' : '',
    'author' : '',
    'songs' : [
        {'title':'song1', 'artist':['blue'], 'duration':2.5},
        {'title':'meow', 'artist':['blue', 'dj kitty'], 'duration':5.25}
    ]
}
total_length = 0
for song in playlist['songs']:
    total_length += song['duration']
print(total_length)
