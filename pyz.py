#!/usr/bin/env python
import os
import os.path
import stat
import zipfile

def create_archive(source, output):
    with open(output, 'wb') as fd:
        fd.write(b'#!/usr/bin/env python\n')
        with zipfile.ZipFile(fd, 'w') as z:
            for dir_path, dir_names, file_names in os.walk(source):
                if dir_path in ('.git', '.svn', '.settings'):
                    continue
                relative_dir_path = os.path.relpath(dir_path, source)
                if not file_names:
                    z.write(dir_path, relative_dir_path)
                else:
                    for file_name in file_names:
                        file_path = os.path.join(dir_path, file_name)
                        relative_file_path = os.path.join(relative_dir_path, file_name)
                        z.write(file_path, relative_file_path)
        os.chmod(output, os.stat(output).st_mode | stat.S_IEXEC)

if __name__ == '__main__':
    import sys
    output = sys.argv[1]
    source = sys.argv[2]
    create_archive(source, output)
