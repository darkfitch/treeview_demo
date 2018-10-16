import py7zlib
import zipfile

from execption_handle import tolerant_execute

COMPACTTYPE = ['ZIP','7Z','RAR','TGZ','TAR']

class Compact(object):
    
    def _judge_file_type(self,filename):
        type = filename.rsplit('.')[-1].upper()
        if type in COMPACTTYPE:
            ret = type
        else:
            ret = None
        return ret
