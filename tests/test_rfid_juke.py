import json
from code.link_new_file import link_new_file
from unittest import TestCase


class RFIDJukeTest(TestCase):
    def test_store_new_key_in_empty_dict(self):
        # ÉTANT DONNÉ
        id = "azerty"
        filename = "lara_fabian666.mp3"
        playlist = {}

        # QUAND
        output = link_new_file(id, filename, playlist)

        # ALORS
        with open('code/playslist.json', 'r') as json_file:
            self.assertEqual({'azerty': 'lara_fabian666.mp3'}, json.load(json_file))

        self.assertEqual("Playlist updated!", output)

    def test_store_new_key_in_filled_dict(self):
        # ÉTANT DONNÉ
        id = "azerty"
        filename = "lara_fabian666.mp3"
        playlist = {"qsdf": "didier_barbelivien69.mp3"}

        # QUAND
        output = link_new_file(id, filename, playlist)

        # ALORS
        with open('code/playslist.json', 'r') as json_file:
            self.assertEqual({'qsdf': 'didier_barbelivien69.mp3', 'azerty': 'lara_fabian666.mp3'}, json.load(json_file))
            
        self.assertEqual("Playlist updated!", output)

    def test_list_all_mp3_files(self):
        # ÉTANT DONNÉ
        # que j'ai une liste de fichiers mp3 dans un dossier mp3

        # QUAND
        ma_liste = list_mp3_files()

        # ALORS
        self.assertEqual(["lara_fabian666.mp3", "didier_barbelivien69.mp3"], ma_list)
        raise

    def test_select_input_in_list(self):
        raise
