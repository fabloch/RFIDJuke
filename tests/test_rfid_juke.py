import json
from code.link_new_file import link_new_file
from unittest import TestCase
from code.listmp3files import listmp3files
import os

TEST_FILEPATH = "tests/playlist.json"


class RFIDJukeTest(TestCase):
    def test_store_new_key_with_no_json(self):
        # ÉTANT DONNÉ
        id = "azerty"
        filename = "lara_fabian666.mp3"

        # QUAND
        output = link_new_file(id, filename, filepath=TEST_FILEPATH)

        # ALORS
        with open(TEST_FILEPATH, "r") as json_file:
            self.assertEqual(
                {"azerty": "lara_fabian666.mp3"},
                json.load(json_file),
            )

        self.assertEqual({"azerty": "lara_fabian666.mp3"}, output)

    def test_store_new_key_with_existing_json(self):
        # ÉTANT DONNÉ
        id = "qsdf"
        filename = "didier_barbelivien69.mp3"
        with open(TEST_FILEPATH, "w") as outfile:
            playlist = {"azerty": "lara_fabian666.mp3"}
            json.dump(playlist, outfile)

        # QUAND
        output = link_new_file(id, filename, filepath=TEST_FILEPATH)

        # ALORS

        self.assertEqual(
            {
                "azerty": "lara_fabian666.mp3",
                "qsdf": "didier_barbelivien69.mp3",
            },
            output,
        )
        with open(TEST_FILEPATH, "r") as json_file:
            self.assertEqual(
                {
                    "azerty": "lara_fabian666.mp3",
                    "qsdf": "didier_barbelivien69.mp3",
                },
                json.load(json_file),
            )

    # def test_list_all_mp3_files(self):
    #     # ÉTANT DONNÉ
    #     # que j'ai une liste de fichiers mp3 dans un dossier mp3

    #     # QUAND
    #     ma_liste = listmp3files()

    #     # ALORS
    #     self.assertEqual(["lara_fabian666.mp3", "didier_barbelivien69.mp3"], ma_liste)

    # def test_select_input_in_list(self):
    #     pass

    def tearDown(self):
        try:
            os.remove(TEST_FILEPATH)
        except FileNotFoundError:
            pass
