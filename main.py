
import os
import traceback




class TreeView(object):
    '''
    主目录,可以实现指定目录下子目录文件的树形结构展示
    '''

    def __init__(self):
        self.tree = {}
        self.name = ''

    def presentation(self, path,method='con'):
        try:
            ret = [os.path.basename(path)]
            index = 0
            ret = self.file_list_loop(path,index,ret)
            if method == 'con':
                self.console_display(ret)
        except FileNotFoundError:
            print('未发现该文件夹/文件,请检查后重试')

    def file_list_loop(self,path,index,ret):
        file_list = os.listdir(path)
        for file in file_list:
            file_path = os.path.join(path,file)
            index += 1
            format_str = '--' *index
            space = '  '
            format_str = f'|{format_str}{space}{file}'
            ret.append(format_str)
            if not os.path.isfile(file_path):
                self.file_list_loop(file_path,index,ret)
        return ret

    def console_display(self,args):
        for arg in args:
            print(arg)

    def file_display(self,args,tag_file_path='',file_name=''):
        try:
            if os.path.isfile(tag_file_path):
                pass
        except:
            pass

    def _write(self,name,path):
        with open

if __name__ == '__main__':
    path = 'E:\_projects\document\\1~25-ly'
    tree_view = TreeView()
    tree_view.presentation(path)
