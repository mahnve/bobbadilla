import subprocess


class FileBuilder:

    def with_path(self, path=""):
        self.path = path
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
