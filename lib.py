from distutils.version import StrictVersion
import requests


def version_check():
    """检查是否有更新"""
    local_version = '0.0.9'
    remote = requests.get('https://raw.githubusercontent.com/FindHao/ciba/master/version').text
    print(remote)
    # todo 注意处理网络问题
    if StrictVersion(remote) > StrictVersion(local_version):
        return True, remote
    return False
