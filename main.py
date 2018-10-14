
import os
import traceback




class TreeView(object):

    def __init__(self):
        self.tree = {}
        self.name = ''

    # def presentation(self,path):
    #     file_list = list(os.walk(path))
    #     self.path = os.path.basename(path)
    #
    #     ret = self.file_list_loop(file_list)
    #     # for file in ret[0]:
    #     #     # if os.path.isfile()
    #     #     pass
    #
    # def file_list_loop(self,files):
    #     level = 0
    #     for file_tuple in files:
    #         print(file_tuple)
    #         level += 1
    #         dir_list = file_tuple[1]
    #         file_list = file_tuple[2]
    #         father_name = os.path.basename(file_tuple[0])
    #         self.tree[str(level)] = {'dir_list':dir_list,'file_list':file_list,'father_name':father_name}
    #     print(self.tree)
    #     return (level)
    #
    # def serialize(self,args):
    #     tree_view = {}
    #     for level in len(args):
    #         dir_list = []
    #         file_list = []
    #         ret = args[str(level+1)]
    #         father_name = ret['father_name']
    #         if father_name == self.name:
    #             for dir in ret[dir_list]:
    #                 tree_view[father_name] = dir_list

    def presentation(self, path,method='con'):
        ret = [os.path.basename(path)]
        index = 0
        ret = self.file_list_loop(path,index,ret)
        if method == 'con':
            self.console_display(ret)


    def file_list_loop(self,path,index,ret):
        file_list = os.listdir(path)
        for file in file_list:
            file_path = os.path.join(path,file)
            index += 1
            format_str = '--' *index
            space = '  '
            if os.path.isfile(file_path):
                ret.append(f'|{format_str}{space}{file}')
            else:
                ret.append(f'|{format_str}{space}{file}')
                self.file_list_loop(file_path,index,ret)
        return ret

    def console_display(self,args):
        for arg in args:
            print(arg)

if __name__ == '__main__':
    path = 'E:\git_code\\treeview_demo'
    tree_view = TreeView()
    tree_view.presentation(path)
