import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import os
from pytest_html import extras

@pytest.fixture
def driver():
    options = Options()
     # headless mode
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1920,1080')

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)

    yield driver
    driver.quit()

# Take screenshot on failure and attach to HTML report
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            screenshots_dir = "screenshots"
            os.makedirs(screenshots_dir, exist_ok=True)
            screenshot_path = os.path.join(
                screenshots_dir, f"{item.name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            )
            driver.save_screenshot(screenshot_path)

            if item.config.pluginmanager.hasplugin("html"):
                extra = getattr(report, "extra", [])
                extra.append(extras.image(screenshot_path))
                report.extra = extra
