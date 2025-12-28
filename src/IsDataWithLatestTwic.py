import os


class IsDataWithLatestTwic:
    def __init__(self, twic_folder):
        self.twic_folder = twic_folder

    def is_folder_with_latest_twic(self, latest_twic_name):
        for dirpath, dirnames, filenames in os.walk(self.twic_folder):
            if latest_twic_name in filenames:
                return True
        return False
