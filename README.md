# Playwright 101 Certification Assignment (Python)

## Overview
This repository contains automated test scenarios for LambdaTest Selenium Playground using Playwright framework with Python.

## Test Scenarios Covered
1. **Simple Form Demo** - Form input validation
2. **Drag & Drop Sliders** - Slider interaction to value 95
3. **Input Form Submit** - Complete form submission with validation

## Prerequisites
- Python 3.8 or higher
- pip package manager
- LambdaTest Account
- Git

## Project Structure
```
playwright-lambdatest-certification/
├── tests/
│   ├── __init__.py
│   ├── test_scenario1.py
│   ├── test_scenario2.py
│   └── test_scenario3.py
├── conftest.py
├── pytest.ini
├── run_parallel_tests.py
├── requirements.txt
├── .gitpod.yml
├── .env
└── README.md
```

## Setup Instructions

### 1. Clone Repository
```bash
git clone <your-repo-url>
cd playwright-lambdatest-certification
```

### 2. Create Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Linux/Mac:
source venv/bin/activate
# Windows:
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
playwright install chromium firefox
```

### 4. Configure LambdaTest Credentials

Create a `.env` file in the project root:
```
LT_USERNAME=your_lambdatest_username
LT_ACCESS_KEY=your_lambdatest_access_key
```

Or set environment variables:
```bash
# Linux/Mac:
export LT_USERNAME="your_username"
export LT_ACCESS_KEY="your_access_key"

# Windows:
set LT_USERNAME=your_username
set LT_ACCESS_KEY=your_access_key
```

## Running Tests

### Run All Tests in Parallel (Recommended)
```bash
python run_parallel_tests.py
```

### Run Individual Scenarios
```bash
# Scenario 1: Simple Form Demo
pytest tests/test_scenario1.py -v

# Scenario 2: Drag & Drop Sliders
pytest tests/test_scenario2.py -v

# Scenario 3: Input Form Submit
pytest tests/test_scenario3.py -v
```

### Run on Specific Browser/OS Combination
```bash
# Chrome on Windows 10
pytest tests/ --browser-combo=chrome-windows -v

# Firefox on macOS Catalina
pytest tests/ --browser-combo=firefox-macos -v
```

### Run with Markers
```bash
# Run only Scenario 1
pytest -m scenario1 -v

# Run only Scenario 2
pytest -m scenario2 -v

# Run only Scenario 3
pytest -m scenario3 -v
```

## Gitpod Setup

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#<your-repo-url>)

### Steps:
1. Click the Gitpod button above
2. Wait for environment to initialize
3. Set your LambdaTest credentials:
```bash
   export LT_USERNAME="your_username"
   export LT_ACCESS_KEY="your_access_key"
```
4. Run tests:
```bash
   python run_parallel_tests.py
```

## Test Execution Details

### Browser/OS Combinations (Parallel Execution)
- **Configuration 1**: Windows 10, Chrome (Latest)
- **Configuration 2**: macOS Catalina, Firefox (Latest)

### Locators Used (3+ Different Types)
1. **Text Locator**: `text=Simple Form Demo`
2. **ID Locator**: `#user-message`, `#showInput`, `#message`
3. **XPath Locator**: `(//input[@type="range"])[3]`
4. **CSS Selector**: `.success-msg`, `button[type="submit"]`
5. **Attribute Locator**: `input[name="name"]`, `select[name="country"]`
6. **Placeholder Locater**: `.get_by_placeholder("Please enter your Message")`
7. **Label Locater**: `.get_by_label("Username")`
8. **Role Locater**: `.get_by_role("button", name="Submit")")`

### Enabled LambdaTest Capabilities
- ✅ Network Logs: `'network': True`
- ✅ Video Recording: `'video': True`
- ✅ Screenshots: `'visual': True`
- ✅ Console Logs: `'console': True`

## Test Results

### LambdaTest Dashboard
Visit [LambdaTest Automation Dashboard](https://automation.lambdatest.com/) to view detailed results.

### Test IDs
- **Test ID 1 (Chrome - Windows 10)**:
    Scenario 1: DA-WIN-2874856-1763290183137574049UAA
    Scenario 2: DA-WIN-2874856-1763290212103160267XBQ
    Scenario 3: DA-WIN-2874856-1763290247909761920CMJ
- **Test ID 2 (Firefox - macOS Catalina)**: 
    Scenario 1: DA-MAC-2874856-1763290183139156887QRC
    Scenario 2: DA-MAC-2874856-1763290220270584935VSJ
    Scenario 3: DA-MAC-2874856-1763290250598637871KCD

## Troubleshooting

### Common Issues

1. **Connection Timeout**
```
   Solution: Verify LambdaTest credentials in .env file
```

2. **Module Not Found Error**
```bash
   # Ensure virtual environment is activated
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   
   # Reinstall dependencies
   pip install -r requirements.txt
```

3. **Playwright Browsers Not Installed**
```bash
   playwright install chromium firefox
```

4. **Slider Value Not 95**
```python
   # Use alternative method in test_scenario2.py:
   slider.fill('95')
```

5. **Parallel Execution Issues**
```bash
   # Run tests sequentially
   pytest tests/ --browser-combo=chrome-windows -v
   pytest tests/ --browser-combo=firefox-macos -v
```

## Key Features

✅ Python-based Playwright automation
✅ Parallel execution on 2 browser/OS combinations
✅ LambdaTest Cloud integration
✅ Comprehensive error handling
✅ Multiple locator strategies 
✅ Video recording and screenshots enabled
✅ Gitpod ready for one-click setup
✅ Detailed assertions and logging

## Support

For issues, contact:
- **LambdaTest Support**: support@lambdatest.com
- **Certification Support**: admin@lambdatestcertifications.com

## Author
Prajesh Shrestha

