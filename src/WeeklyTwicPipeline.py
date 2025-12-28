from GetLatestTwic import GetLatestTwic
import os
from GetLatestTwicPgn import GetLatestTwicPgn
from SavePgn import SavePgn
from IsDataWithLatestTwic import IsDataWithLatestTwic
import sys

twic_main_site_url = os.getenv("TWIC_MAIN_SITE")
getLatestTwicNumber = GetLatestTwic(twic_main_site_url)
latest_twic = getLatestTwicNumber.get()
twic_pgn_name = f"twic-{latest_twic}"
twic_pgn_folder_path = os.getenv("TWIC_FILES_FOLDER")

is_data_with_latest_twic = IsDataWithLatestTwic(twic_pgn_folder_path)

if is_data_with_latest_twic.is_folder_with_latest_twic(twic_pgn_name+".pgn"):
    print("the twic repo has the latest twic, there is no need to keep running the pipeline")
    sys.exit(0)

file_type_request = ".zip"
twic_postfix = "g"
last_twic_url = f"{os.getenv("TWIC_URL")}{latest_twic}{twic_postfix}{file_type_request}"
get_latest_pgn = GetLatestTwicPgn(last_twic_url)

pgn_file_bytes = get_latest_pgn.get()

save_pgn = SavePgn(twic_pgn_folder_path)
save_pgn.Save(pgn_file_bytes, twic_pgn_name)
