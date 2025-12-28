from GetLatestTwic import GetLatestTwic
import os
from GetLatestTwicPgn import GetLatestTwicPgn
from SavePgn import SavePgn

twic_main_site_url = os.getenv("TWIC_MAIN_SITE")
getLatestTwicNumber = GetLatestTwic(twic_main_site_url)
latest_twic = getLatestTwicNumber.get()
file_type_request = ".zip"
twic_postfix = "g"
last_twic_url = f"{os.getenv("TWIC_URL")}{latest_twic}{twic_postfix}{file_type_request}"
get_latest_pgn = GetLatestTwicPgn(last_twic_url)

pgn_file_bytes = get_latest_pgn.get()

twic_pgn_folder_path = os.getenv("TWIC_FILES_FOLDER")
twic_pgn_name = f"twic-{latest_twic}"
save_pgn = SavePgn(twic_pgn_folder_path)
save_pgn.Save(pgn_file_bytes, twic_pgn_name)
