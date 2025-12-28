import os
import zipfile


class SavePgn:
    def __init__(self, folder_path):
        self.folder_path = folder_path

    def Save(self, pgn_bytes, pgn_name):
        save_path = f"{self.folder_path}{pgn_name}.pgn"

        with open(save_path, "wb") as f:
            f.write(pgn_bytes)
