import traceback

from loggle import Loggle

class ExecoptionHandling(object):

    def execute(self,func,method=''):
        if not method:
            self._execute(func)
        else:
            pass

    def _execute(self,func):
        try:
            ret = func()
            return ret
        except:
            #调用loggle的方法 看过之后在说
            pass


tolerant_execute = ExecoptionHandling().execute