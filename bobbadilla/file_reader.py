import os


class FileReader:

    def read(self, path):
        try:
            size = self._to_mb(os.path.getsize(path))
        except FileNotFoundError:
            print("Nonexisting file: {}".format(path))
            return None

        return {'size': size}

    def _to_mb(self, bytes):
        bytes_per_mb = 1024*1024
        return bytes/bytes_per_mb
