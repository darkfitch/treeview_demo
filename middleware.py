

class BaseMiddleWare(object):

    def __call__(self):
        pass


class ToleranceMiddleWare(BaseMiddleWare):
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
            