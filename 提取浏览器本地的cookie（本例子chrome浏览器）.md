### 提取浏览器本地的cookie（本例子chrome浏览器）

```python

import re
import sqlite3

import requests
import urllib3
import os
import json

import sys
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def dpapi_decrypt(encrypted):
    import ctypes
    import ctypes.wintypes

    class DATA_BLOB(ctypes.Structure):
        _fields_ = [('cbData', ctypes.wintypes.DWORD),
                    ('pbData', ctypes.POINTER(ctypes.c_char))]

    p = ctypes.create_string_buffer(encrypted, len(encrypted))
    blobin = DATA_BLOB(ctypes.sizeof(p), p)
    blobout = DATA_BLOB()
    retval = ctypes.windll.crypt32.CryptUnprotectData(
        ctypes.byref(blobin), None, None, None, None, 0, ctypes.byref(blobout))
    if not retval:
        raise ctypes.WinError()
    result = ctypes.string_at(blobout.pbData, blobout.cbData)
    ctypes.windll.kernel32.LocalFree(blobout.pbData)
    return result


def aes_decrypt(encrypted_txt):
    with open(os.path.join(os.environ['LOCALAPPDATA'],r"Google\Chrome\User Data\Local State"), mode="r", encoding='utf-8') as f:
        jsn = json.loads(str(f.readline()))
    encoded_key = jsn["os_crypt"]["encrypted_key"]
    encrypted_key = base64.b64decode(encoded_key.encode())
    encrypted_key = encrypted_key[5:]
    key = dpapi_decrypt(encrypted_key)
    nonce = encrypted_txt[3:15]
    cipher = Cipher(algorithms.AES(key), None, backend=default_backend())
    cipher.mode = modes.GCM(nonce)
    decryptor = cipher.decryptor()
    return decryptor.update(encrypted_txt[15:])


def chrome_decrypt(encrypted_txt):
    if sys.platform == 'win32':
        try:
            if encrypted_txt[:4] == b'x01x00x00x00':
                decrypted_txt = dpapi_decrypt(encrypted_txt)
                return decrypted_txt.decode()
            elif encrypted_txt[:3] == b'v10':
                decrypted_txt = aes_decrypt(encrypted_txt)
                return decrypted_txt[:-16].decode()
        except WindowsError:
            return None
    else:
        raise WindowsError


def get_cookies_from_chrome(domain):
    sql = 'SELECT name, encrypted_value as value FROM cookies where host_key like "%{domain}%"'.format(domain=domain)
    filename = os.path.join(os.environ['USERPROFILE'], r'AppData\Local\Google\Chrome\User Data\default\Cookies')
    con = sqlite3.connect(filename)
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute(sql)
    cookie = ''
    for row in cur:
        if row['value'] is not None:
            name = row['name']
            value = chrome_decrypt(row['value'])
            if value is not None:
                cookie += name + '=' + value + ';'
    return cookie

def cookie_run(domain):
    # 目标网站域名

    domain = re.search(r'.(\w+).(\w+)/', domain)
    domain = "." + domain.group(1) + "." + domain.group(2)
    cookie = get_cookies_from_chrome(domain)
    cookies = {}
    cookie_list = cookie.split(';')
    for i in cookie_list:
        if i:
            temp = i.split('=')
            cookies[temp[0]] = temp[-1]

    return cookies
if __name__ == '__main__':
    print(cookie_run("https://www.csdn.net/"))

```

![image-20200728142343921](C:%5CUsers%5Cxingdao_1%5CDesktop%5Cblog%5C%E5%9B%BE%E7%89%87%5Cimage-20200728142343921.png)

注意截图函数内的标注部分，python2不需要 encoding, python3使用的时候则需要 加上 encoding部分

