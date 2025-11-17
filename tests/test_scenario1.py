import pytest
from playwright.sync_api import Page, expect
import time
import re

@pytest.mark.scenario1
class TestScenario1:
    """Test Scenario 1 - Simple Form Demo"""
    
    def test_simple_form_demo(self, page: Page):
        # Step 1: Open LambdaTest's Selenium Playground
        page.goto('https://www.lambdatest.com/selenium-playground', timeout=60000)
        page.wait_for_load_state('domcontentloaded')
        
        # Step 2: Click "Simple Form Demo" using text locator
        page.get_by_role('link', name='Simple Form Demo').click()
        
        # Step 3: Validate URL contains "simple-form-demo"
        page.wait_for_url('**/simple-form-demo**', timeout=10000)
        expect(page).to_have_url(re.compile('.*simple-form-demo.*'))
        
        # Step 4: Create variable for string value
        message_text = 'Welcome to LambdaTest'
        
        # Step 5: Enter value in "Enter Message" text box using ID locator
        message_input = page.locator('input#user-message')
        message_input.fill(message_text)
        
        # Step 6: Click "Get Checked Value" button using ID locator
        get_value_button = page.locator('#showInput')
        get_value_button.click()
        
        # Step 7: Validate the message is displayed in right panel
        message_display = page.locator('p#message')
        expect(message_display).to_have_text(message_text)
        
        print(f"✓ Test Passed: Message '{message_text}' displayed correctly")
        time.sleep(2)
