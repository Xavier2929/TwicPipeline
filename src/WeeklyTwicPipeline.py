from GetLatestTwic import GetLatestTwic
import os
from GetLatestTwicPgn import GetLatestTwicPgn

twic_main_site_url = os.getenv("TWIC_MAIN_SITE")
getLatestTwicNumber = GetLatestTwic(twic_main_site_url)
latest_twic = getLatestTwicNumber.get()
file_type_request = ".zip"
twic_postfix = "g"
last_twic_url = f"{os.getenv("TWIC_URL")}{latest_twic}{twic_postfix}{file_type_request}"
get_latest_pgn = GetLatestTwicPgn(last_twic_url)

pgn_file = get_latest_pgn.get()
