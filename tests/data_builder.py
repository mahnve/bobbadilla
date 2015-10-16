import subprocess
import os
import errno


def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise


class FileBuilder:

    def with_path(self, path=""):
        self.path = path
        makedir_p(self.path)
        return self

    def with_size(self, size_mb=0):
        self.size_mb = size_mb
        return self

    def build(self):
        size_bytes = self.size_mb*1024*1024
        cmd = ['dd',
               'if=/dev/zero',
               "of={}".format(self.path),
               "bs={}".format(size_bytes),
               "count=1"]
        subprocess.call(cmd)
