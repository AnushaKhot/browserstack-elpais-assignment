import threading
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.safari.options import Options as SafariOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.remote.webdriver import WebDriver

BROWSERSTACK_USERNAME = 'anushakhot_lrrkyv'
BROWSERSTACK_ACCESS_KEY = 'iyzjXx8gCg6tiqeqARR6'

article_urls = [
    "https://elpais.com/opinion/2025-08-05/mazon-y-la-nada.html",
    "https://elpais.com/opinion/2025-08-05/trump-despide-al-mensajero.html",
    "https://elpais.com/opinion/2025-08-05/migrantes-somos-todos.html",
    "https://elpais.com/opinion/2025-08-05/hacerse-el-fuerte-hacerse-el-debil.html",
    "https://elpais.com/opinion/2025-08-05/nepoliticos.html"
]

browsers = [
    {
        'os': 'Windows',
        'os_version': '11',
        'browser': 'Chrome',
        'browser_version': 'latest'
    },
    {
        'os': 'OS X',
        'os_version': 'Monterey',
        'browser': 'Safari',
        'browser_version': 'latest'
    },
    {
        'os': 'Windows',
        'os_version': '10',
        'browser': 'Edge',
        'browser_version': 'latest'
    },
    {
        'os': 'android',
        'device': 'Samsung Galaxy S22',
        'real_mobile': 'true'
    },
    {
        'os': 'ios',
        'device': 'iPhone 14',
        'real_mobile': 'true'
    }
]

def run_browser_test(config, url):
    capabilities = config.copy()
    capabilities['name'] = "ElPais Load Test"
    capabilities['build'] = "ElPais Articles Load"

    if 'browser' in config:
        browser = config['browser'].lower()
        if browser == 'chrome':
            options = ChromeOptions()
        elif browser == 'safari':
            options = SafariOptions()
        elif browser == 'edge':
            options = EdgeOptions()
        else:
            options = ChromeOptions()
    else:
        options = ChromeOptions()

    for key in capabilities:
        options.set_capability(key, capabilities[key])

    driver = WebDriver(
        command_executor=f"https://{BROWSERSTACK_USERNAME}:{BROWSERSTACK_ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub",
        options=options
    )

    try:
        driver.get(url)
        print(f"[✓] Loaded: {url} on {config.get('browser', config.get('device'))}")
        time.sleep(5)
        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Page loaded successfully"}}'
        )
    except Exception as e:
        driver.execute_script(
            f'browserstack_executor: {"action": "setSessionStatus", "arguments": {{"status":"failed", "reason": "{str(e)}"}}}'
        )
        print(f"[✗] Failed: {url} on {config.get("browser", config.get("device"))}")
    finally:
        driver.quit()

threads = []
for i in range(5):
    t = threading.Thread(target=run_browser_test, args=(browsers[i], article_urls[i]))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
