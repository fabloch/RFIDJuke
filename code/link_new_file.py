import json


def link_new_file(id, filename, playlist):
    playlist.update({id: filename})
    with open('playslist.json', 'w') as outfile:
        json.dump(playlist, outfile)

    return "Playlist updated!"
