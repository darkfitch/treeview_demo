import unittest

from main import TreeView


class TreeViewCase(unittest.TestCase):

    a = "[('E:\\git_code\\treeview_demo', ['.idea', 'test'], ['main.py']), ('E:\\git_code\\treeview_demo\\.idea', ['inspectionProfiles'], ['misc.xml', 'modules.xml', 'treeview_demo.iml', 'workspace.xml']), ('E:\\git_code\\treeview_demo\\.idea\\inspectionProfiles', [], ['Project_Default.xml']), ('E:\\git_code\\treeview_demo\\test', [], ['presentationtest.py'])]"
    path = 'E:\git_code\\treeview_demo'
    # def test_key(self):
    #     temp = TreeView()

    def setUp(self):
        self.tree_view = TreeView()

    def tearDown(self):
        self.tree_view = None

    @unittest.skip('reason')
    def test_presentation(self):

        # self.assertEquals(self.tree_view.presentation(TreeViewCase.path),TreeViewCase.a)
        self.assertEqual(self.tree_view.presentation(TreeViewCase.path),TreeViewCase.a)

    def test_add(self):
        self.assertEqual(self.tree_view.add(3),9)

if __name__ == '__main__':
    unittest.main()

a = "[('E:\\git_code', ['start_app', 'treeview_demo', 'tum_spider'], []), ('E:\\git_code\\start_app', ['.git', '.idea'], ['config.txt', 'startapp.py']), ('E:\\git_code\\start_app\\.git', ['hooks', 'info', 'logs', 'objects', 'refs'], ['config', 'description', 'FETCH_HEAD', 'HEAD', 'index', 'packed-refs']), ('E:\\git_code\\start_app\\.git\\hooks', [], ['applypatch-msg.sample', 'commit-msg.sample', 'fsmonitor-watchman.sample', 'post-update.sample', 'pre-applypatch.sample', 'pre-commit.sample', 'pre-push.sample', 'pre-rebase.sample', 'pre-receive.sample', 'prepare-commit-msg.sample', 'update.sample']), ('E:\\git_code\\start_app\\.git\\info', [], ['exclude']), ('E:\\git_code\\start_app\\.git\\logs', ['refs'], ['HEAD']), ('E:\\git_code\\start_app\\.git\\logs\\refs', ['heads', 'remotes'], []), ('E:\\git_code\\start_app\\.git\\logs\\refs\\heads', [], ['master']), ('E:\\git_code\\start_app\\.git\\logs\\refs\\remotes', ['origin'], []), ('E:\\git_code\\start_app\\.git\\logs\\refs\\remotes\\origin', [], ['HEAD']), ('E:\\git_code\\start_app\\.git\\objects', ['info', 'pack'], []), ('E:\\git_code\\start_app\\.git\\objects\\info', [], []), ('E:\\git_code\\start_app\\.git\\objects\\pack', [], ['pack-fbee9f4940cdac447ebbb931bde68b6f5133f73e.idx', 'pack-fbee9f4940cdac447ebbb931bde68b6f5133f73e.pack']), ('E:\\git_code\\start_app\\.git\\refs', ['heads', 'remotes', 'tags'], []), ('E:\\git_code\\start_app\\.git\\refs\\heads', [], ['master']), ('E:\\git_code\\start_app\\.git\\refs\\remotes', ['origin'], []), ('E:\\git_code\\start_app\\.git\\refs\\remotes\\origin', [], ['HEAD']), ('E:\\git_code\\start_app\\.git\\refs\\tags', [], []), ('E:\\git_code\\start_app\\.idea', [], ['workspace.xml']), ('E:\\git_code\\treeview_demo', ['.idea', 'test'], ['main.py']), ('E:\\git_code\\treeview_demo\\.idea', ['inspectionProfiles'], ['misc.xml', 'modules.xml', 'treeview_demo.iml', 'workspace.xml']), ('E:\\git_code\\treeview_demo\\.idea\\inspectionProfiles', [], ['Project_Default.xml']), ('E:\\git_code\\treeview_demo\\test', [], ['presentationtest.py']), ('E:\\git_code\\tum_spider', [], ['main.py'])]"


