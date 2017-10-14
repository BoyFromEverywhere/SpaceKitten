import hashlib

def md5_common(url):
    if isinstance(url,str):
        url = url.encode('utf-8')

    m = hashlib.md5()
    m.update(url)
    return m.hexdigest