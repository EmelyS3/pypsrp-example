from pypsrp.client import Client
from pypsrp.exceptions import WSManFaultError
from pypsrp.exceptions import WinRMTransportError
from pypsrp.exceptions import AuthenticationError
from requests.exceptions import ConnectionError
from requests.exceptions import ReadTimeout
import time


def exec():
    client = Client("192.168.1.119", ssl=False, username="os", password="pxgtsjmnt")

    try:
        # cmd = "tasklist"
        # cmd = "taskkill /im MEGAsync.exe /f"
        cmd = "logoff 1"
        # cmd = 'powershell -Command {"{0:N2} MB" -f ((Get-ChildItem C:\\Users\\os\AppData\\Local\\Microsoft -Recurse | Measure-Object -Property Length -Sum -ErrorAction Stop).Sum / 1MB)}'
        # cmd = 'powershell -Command {Install-Module PSFolderSize}'
        # cmd = 'powershell -Command {Ps-FolderSize  -Path "C:\\Users\\os\AppData\\Local\\Microsoft" }'
        # cmd = 'dir'
        # cmd = "taskkill /im bash.exe /f"
        stdout, stderr, rc = client.execute_cmd(cmd)

    except (WSManFaultError, ConnectionError, WinRMTransportError, AuthenticationError, ReadTimeout):
        print("[!] ERROR WSManFaultError or ConnectionError or WinRMTransportError, AuthenticationError, ReadTimeout")
        return -1

    # stdout, stderr, rc = client.execute_cmd("tasklist")
    print(stdout)
    print(stderr)


def main():
    ret = exec()

    while ret is -1:
        ret = exec()
        time.sleep(5)



main()
