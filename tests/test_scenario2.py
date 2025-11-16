import pytest
from playwright.sync_api import Page, expect

@pytest.mark.scenario2
class TestScenario2:
    """Test Scenario 2 - Drag & Drop Sliders"""
    
    def test_drag_drop_slider(self, page: Page):
        """
        Test Steps:
        1. Open Selenium Playground and click "Drag & Drop Sliders"
        2. Select slider with "Default value 15"
        3. Drag slider to value 95
        4. Validate range value shows 95
        """
        
        # Step 1: Open Selenium Playground and click "Drag & Drop Sliders"
        page.goto('https://www.lambdatest.com/selenium-playground', timeout=60000)
        page.wait_for_load_state('domcontentloaded')
        page.click('text=Drag & Drop Sliders')
        
        page.wait_for_url('**/drag-drop-range-sliders-demo**', timeout=10000)
        
        # Step 2: Select slider with "Default value 15" using XPath locator
        slider = page.locator("//input[@value='15']")
        
        # # Get slider bounding box
        # slider_box = slider.bounding_box()
        
        # # Calculate the position for value 95
        # # The slider range is 0-100, so we need to position it at 95%
        # start_x = slider_box['x'] + slider_box['width'] * 0.15  # Starting at value 15
        # start_y = slider_box['y'] + slider_box['height'] / 2
        
        # # Target position for value 95 (95% of slider width)
        # target_x = slider_box['x'] + (slider_box['width'] * 0.95)
        # target_y = start_y
        
        # # Drag slider to position
        # page.mouse.move(start_x, start_y)
        # page.mouse.down()
        # page.mouse.move(target_x, target_y, steps=10)
        # page.mouse.up()
        
        # # Alternative approach: Use fill method (more reliable)
        slider.fill('95')
        
        # # Step 3: Validate the range value shows 95 using CSS selector
        
        # # Step 3: Validate slider value shows 95
        range_locator = page.locator('#rangeSuccess')
        expect(range_locator).to_have_text('95')

        print(f"✓ Test Passed: Slider value is 95")
