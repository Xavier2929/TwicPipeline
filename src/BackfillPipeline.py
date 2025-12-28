from GetLatestTwic import GetLatestTwic
import os
from GetLatestTwicPgn import GetLatestTwicPgn
from SavePgn import SavePgn
from IsDataWithLatestTwic import IsDataWithLatestTwic
import sys


class BackfillPipeline:
    def __init__(self, start, finish, folder):
        self.start = start
        self.finish = finish
        self.twic_file_folder = folder

    def Backfill(self):
        for index in range(self.start, self.finish):
            twic_pgn_name = f"twic-{index}"

            file_type_request = ".zip"
            twic_postfix = "g"
            last_twic_url = f"{os.getenv("TWIC_URL")}{index}{twic_postfix}{file_type_request}"

            get_pgn = GetLatestTwicPgn(last_twic_url)
            pgn_file_bytes = get_pgn.get()

            save_pgn = SavePgn(twic_pgn_folder_path)
            save_pgn.Save(pgn_file_bytes, twic_pgn_name)


twic_pgn_folder_path = os.getenv("TWIC_FILES_FOLDER")
backfill = BackfillPipeline(920, 953, twic_pgn_folder_path)
backfill.Backfill()
