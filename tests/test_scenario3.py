import pytest
from playwright.sync_api import Page, expect
import time

@pytest.mark.scenario3
class TestScenario3:
    """Test Scenario 3 - Input Form Submit"""
    
    def test_input_form_submit(self, page: Page):
        # Step 1: Open Selenium Playground and click "Input Form Submit"
        page.goto('https://www.lambdatest.com/selenium-playground', timeout=60000)
        page.wait_for_load_state('domcontentloaded')
        
        input_form_link = page.locator('a:has-text("Input Form Submit")')
        input_form_link.click()
        
        page.wait_for_url('**/input-form-demo**', timeout=10000)
        
        # Step 2: Click Submit without filling form
        submit_button = page.locator('button:has-text("Submit")').last
        submit_button.scroll_into_view_if_needed()
        submit_button.click()
        
        # Step 3: Assert error message using attribute locator
        name_input = page.locator('input[name="name"]')
        validation_message = name_input.evaluate('el => el.validationMessage')
        
        assert validation_message and ('fill' in validation_message.lower() or 'required' in validation_message.lower()), \
            f"Expected validation message, got: {validation_message}"
        
        print(f"✓ Validation message: {validation_message}")
        
        # Step 4: Fill in Name, Email and other fields using attribute locators
        page.fill('#name', 'John Doe')
        page.fill('#inputEmail4', 'john.doe@example.com')
        page.fill('#inputPassword4', 'Password123!')
        page.fill('#company', 'Tech Corporation')
        page.fill('#websitename', 'https://example.com')
        
        # Step 5: Select "United States" from Country dropdown
        page.locator('select[name="country"]').select_option(value='US')
        
        # Step 6: Fill remaining fields
        page.fill('input[name="city"]', 'New York')
        page.fill('#inputAddress1', '123 Main Street')
        page.fill('#inputAddress2', 'Apt 4B')
        page.fill('#inputState', 'New York')
        page.fill('#inputZip', '10001')
        
        # Click Submit
        submit_button.click()
        
        # Step 7: Validate success message using class locator
        success_locator = page.locator('.success-msg')
        expect(success_locator).to_be_visible(timeout=10000)
        expect(success_locator).to_contain_text('Thanks for contacting us, we will get back to you shortly.')
        
        print(f"✓ Test Passed: Success message displayed")
        time.sleep(2)