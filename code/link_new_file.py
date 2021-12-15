import json

DEFAULT_FILEPATH = "code/playslist.json"


def link_new_file(id, filename, filepath=DEFAULT_FILEPATH):
    try:
        in_file = open(filepath, "r")
        playlist = json.load(in_file)
        in_file.close()

        with open(filepath, "w") as outfile:
            playlist[id] = filename
            json.dump(playlist, outfile)
    except FileNotFoundError:
        with open(filepath, "w") as outfile:
            playlist = {id: filename}
            json.dump(playlist, outfile)

    return playlist
