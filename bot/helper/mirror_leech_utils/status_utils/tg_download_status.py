from bot.helper.ext_utils.bot_utils import get_readable_time
from bot.helper.ext_utils.human_format import get_readable_file_size
from bot.helper.mirror_leech_utils.status_utils.status_utils import MirrorStatus



class TelegramStatus:
    def __init__(self, obj, message, gid):
        self.message = message
        self.__obj = obj
        self.__gid = gid
        
    def gid(self):
        return self.__gid

    def processed_bytes(self):
        return self.__obj.downloaded_bytes

    def size_raw(self):
        return self.__obj.size

    def size(self):
        return get_readable_file_size(self.size_raw())

    def status(self):
        return MirrorStatus.STATUS_DOWNLOADING

    def name(self):
        return self.__obj.name

    def progress_raw(self):
        return self.__obj.progress

    def progress(self):
        return f'{round(self.progress_raw(), 2)}%'

    def speed_raw(self):
        """
        :return: Download speed in Bytes/Seconds
        """
        return self.__obj.download_speed

    def speed(self):
        return f'{get_readable_file_size(self.speed_raw())}/s'

    def eta(self):
        try:
            seconds = (self.size_raw() - self.processed_bytes()) / self.speed_raw()
            return f'{get_readable_time(seconds)}'
        except:
            return '-'

    def download(self):
        return self.__obj

    def type(self):
        return "Telegram"