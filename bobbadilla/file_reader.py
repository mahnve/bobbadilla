import os


class FileReader:

    def read(self, path):
        return {'size': self._to_mb(os.path.getsize(path))}

    def _to_mb(self, bytes):
        bytes_per_mb = 1024*1024
        return bytes/bytes_per_mb
