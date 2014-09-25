import subprocess
import urllib2
import sys

class setup(object):
    def __init__(self):
        if "SUCCESS" in self.addToPath()['output']:
            print('[+] Added to Path')
            print('[-] Going to try installing setuptools..')
            if "Finished processing dependencies for setuptools" in self.installSetuptools()['output']:
                print('[+] Installed setuptools..')
                print('[-] Going to try installing pip..')
                if "Finished processing dependencies for pip" in self.installPip()['output']:
                    print('[+] Installed pip!')
                    if 'Successfully installed requests beautifulsoup4' in self.pipInstallModules()['output']:
                        print('[+] Successfully installed the modules, we are done here.')
                    else:
                        print('[+] Failed installing modules')
                else:
                    print('[+] Failed installing pip')
            else:
                print('[+] Failed installing setuptools')
        else:
            print('[+] Failed adding to PATH')

    def pipInstallModules(self):
        self.pipInstallOutput = subprocess.check_output(['C:\Python27\Scripts\pip.exe', 'install', 'requests', 'beautifulsoup4'])
        return { 'output': self.pipInstallOutput }

    def installPip(self):
        self.pipOutput = subprocess.check_output(['C:\Python27\Scripts\easy_install.exe', 'pip'])
        return { 'output': self.pipOutput }

    def installSetuptools(self):
        self.ez_setup = urllib2.urlopen('https://bootstrap.pypa.io/ez_setup.py')
        self.source = self.ez_setup.read()
        self.file = open('ez_setup.py', 'w')
        self.file.write(self.source)
        self.file.close()
        self.ezOutput = subprocess.check_output(['ez_setup.py'], shell=True)
        return { 'output': self.ezOutput }

    def addToPath(self):
        self.output = subprocess.check_output(['setx', 'PATH', ';C:\Python27;C:\Python27\Scripts'])
        return { 'output': self.output }

if __name__ == "__main__":
    setup()
