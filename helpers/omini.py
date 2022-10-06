import requests
import json
from helpers.undetect_chrome_driver import UndetectChromeDriver
from selenium.webdriver.chrome import service
from selenium.webdriver.chrome.options import Options 
class Omni():
    API_OPEN_BROWSER_PATH = '/open'
    CONFIG = None
    api = None
    def __init__(self, config):
        self.CONFIG = config
        self.api = 'http://localhost:35000'

    def get(self):        
        driver = None
        url = self.api + self.API_OPEN_BROWSER_PATH + '?profile_id=1'
        res = requests.get(url)
        startedResult = res.json()
        status = bool(startedResult['status'])
        if(status):
            seleniumRemoteDebugAddress = str(startedResult["remote_debug_address"])
            driverPath = str(startedResult["drive_location"])
            options = Options()
            options.debugger_address = seleniumRemoteDebugAddress
            #options.add_experimental_option("detach", True)
            myService  = service.Service(driverPath)
            driver = UndetectChromeDriver(service = myService, options=options)
            driver.implicitly_wait(20)
        return driver
        