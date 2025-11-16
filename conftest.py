import pytest
import os
import json
import urllib.parse
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# LambdaTest credentials
LT_USERNAME = os.getenv('LT_USERNAME')
LT_ACCESS_KEY = os.getenv('LT_ACCESS_KEY')

# Validate credentials
if not LT_USERNAME or not LT_ACCESS_KEY:
    raise ValueError(
        "LambdaTest credentials not found! "
        "Please set LT_USERNAME and LT_ACCESS_KEY in .env file or as environment variables."
    )

print(f"✓ LambdaTest Username: {LT_USERNAME}")
print(f"✓ Access Key configured: {'*' * 20}{LT_ACCESS_KEY[-4:]}")


def get_capabilities(browser_name, platform):
    """Generate LambdaTest capabilities with correct browser names"""
    capabilities = {
        "browserName": browser_name,  # Use pw-chromium or pw-firefox
        "browserVersion": "latest",
        "LT:Options": {
            "platform": platform,
            "build": "Playwright 101 Certification - Python",
            "name": f"Test Execution - {browser_name} on {platform}",
            "user": LT_USERNAME,
            "accessKey": LT_ACCESS_KEY,
            "network": True,
            "video": True,
            "console": True,
            "visual": True,
            "tunnel": False,
            "tunnelName": "",
            "geoLocation": "",
            "resolution": "1920x1080"
        }
    }
    return capabilities


def pytest_addoption(parser):
    """Add command line options"""
    parser.addoption(
        "--browser-combo",
        action="store",
        default="chrome-windows",
        help="Browser and OS combination: chrome-windows or firefox-macos"
    )


@pytest.fixture(scope="function")
def page(request):
    """Create page instance with LambdaTest connection"""
    browser_combo = request.config.getoption("--browser-combo")
    
    # Determine browser and platform - USE CORRECT PLAYWRIGHT BROWSER NAMES
    if browser_combo == "chrome-windows":
        browser_name = "pw-chromium"  # Changed from "Chrome"
        platform = "Windows 10"
        display_name = "Chrome on Windows 10"
    elif browser_combo == "firefox-macos":
        browser_name = "pw-firefox"  # Changed from "Firefox"
        platform = "macOS Catalina"
        display_name = "Firefox on macOS Catalina"
    else:
        browser_name = "pw-chromium"
        platform = "Windows 10"
        display_name = "Chrome on Windows 10"
    
    print(f"\n{'='*60}")
    print(f"Connecting to LambdaTest: {display_name}")
    print(f"{'='*60}")
    
    # Get capabilities
    capabilities = get_capabilities(browser_name, platform)
    
    # Create WebSocket endpoint with proper URL encoding
    capabilities_json = json.dumps(capabilities)
    encoded_caps = urllib.parse.quote(capabilities_json)
    ws_endpoint = f"wss://cdp.lambdatest.com/playwright?capabilities={encoded_caps}"
    
    playwright = None
    browser = None
    context = None
    page_obj = None
    
    try:
        # Connect to LambdaTest
        playwright = sync_playwright().start()
        
        # Always use chromium.connect for LambdaTest (they handle the browser selection)
        browser = playwright.chromium.connect(ws_endpoint, timeout=60000)
        
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            ignore_https_errors=True
        )
        
        page_obj = context.new_page()
        
        print(f"✓ Successfully connected to LambdaTest!")
        print(f"✓ Running on: {display_name}")
        
        yield page_obj
        
    except Exception as e:
        print(f"\n❌ Error connecting to LambdaTest:")
        print(f"Error: {str(e)}")
        print(f"\nPlease check:")
        print(f"1. LambdaTest credentials are correct")
        print(f"2. You have available automation minutes")
        print(f"3. Your internet connection is stable")
        raise
        
    finally:
        # Cleanup
        if page_obj:
            try:
                page_obj.close()
            except:
                pass
        if context:
            try:
                context.close()
            except:
                pass
        if browser:
            try:
                browser.close()
            except:
                pass
        if playwright:
            try:
                playwright.stop()
            except:
                pass