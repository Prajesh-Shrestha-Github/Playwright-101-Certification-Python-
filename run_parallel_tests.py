import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor

def run_browser_sequential(browser_combo):
 
    browser_name = 'Chrome (Windows 10)' if 'chrome' in browser_combo else 'Firefox (macOS Catalina)'
    
    print(f"\n{'='*70}")
    print(f"🚀 Running tests on: {browser_name}")
    print(f"   Platform: LambdaTest Cloud Playwright Grid")
    print(f"{'='*70}\n")
    
    # Run all tests for this browser
    cmd = [
        sys.executable, '-m', 'pytest',
        'tests/',
        f'--browser-combo={browser_combo}',
        '-v', '-s',
        '--tb=short'
    ]
    
    start_time = time.time()
    result = subprocess.run(cmd, capture_output=False)
    duration = time.time() - start_time
    
    status = "✓ PASSED" if result.returncode == 0 else "✗ FAILED"
    print(f"\n{status} {browser_name} - Completed in {duration:.1f}s")
    
    return {
        'browser': browser_combo,
        'browser_name': browser_name,
        'return_code': result.returncode,
        'duration': duration
    }

def main():
    
    
    browser_configs = [
        'chrome-windows',
        'firefox-macos'
    ]
    
    print("\n🚀 Starting PARALLEL execution on 2 browsers...")
    print("="*70)
    
    start_time = time.time()
    
    # Execute BOTH browsers in PARALLEL using ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=2) as executor:
        # Submit both browser test suites to run simultaneously
        futures = {
            executor.submit(run_browser_sequential, browser): browser 
            for browser in browser_configs
        }
        
        # Collect results as they complete
        results = []
        for future in futures:
            result = future.result()
            results.append(result)
    
    total_time = time.time() - start_time
    
    # Summary
    print("\n" + "="*70)
    print("📊 EXECUTION SUMMARY")
    print("="*70)
    
    passed_browsers = sum(1 for r in results if r['return_code'] == 0)
    failed_browsers = len(results) - passed_browsers
    total_tests = 6  # 3 scenarios x 2 browsers
    
    print(f"\nExecution Type:         PARALLEL (2 browsers simultaneously)")
    print(f"Platform:               LambdaTest Cloud Playwright Grid")
    print(f"Browser Configurations: {len(results)}")
    print(f"Total Test Sessions:    {total_tests}")
    print(f"Passed Browsers:        {passed_browsers} ✓")
    print(f"Failed Browsers:        {failed_browsers} ✗")
    print(f"Total Duration:         {total_time:.1f}s ({total_time/60:.1f} minutes)")
    
    print("\n" + "="*70)
    print("BROWSER RESULTS")
    print("="*70)
    
    for r in results:
        status = "✓ PASSED" if r['return_code'] == 0 else "✗ FAILED"
        print(f"\n{status} {r['browser_name']}")
        print(f"   Duration: {r['duration']:.1f}s")
        print(f"   Tests: 3 scenarios on LambdaTest Grid")
    
    print("\n" + "="*70)
    
    if failed_browsers == 0:
        print("✅ ALL TESTS PASSED ON LAMBDATEST CLOUD!")
        print("="*70)
        
      
        print("   Build: Playwright 101 Certification - Python")
        print("   ├─ test_simple_form_demo - Chrome (Windows 10)")
        print("   ├─ test_drag_drop_slider - Chrome (Windows 10)")
        print("   ├─ test_input_form_submit - Chrome (Windows 10)")
        print("   ├─ test_simple_form_demo - Firefox (macOS Catalina)")
        print("   ├─ test_drag_drop_slider - Firefox (macOS Catalina)")
        print("   └─ test_input_form_submit - Firefox (macOS Catalina)")
        
     
        print("   ### Build Information")
        print("   - Build Name: Playwright 101 Certification - Python")
        print("   - Execution Type: Parallel")
        print("   - Browser Combinations: 2 (Chrome + Firefox)")
        print("   ```")
        
        return 0
    else:
        print(f"❌ {failed_browsers} BROWSER CONFIGURATION(S) FAILED")
        print("\n💡 Troubleshooting:")
        print("   • Check LambdaTest dashboard for detailed error logs")
        print("   • Verify automation minutes are available")
        print("   • Ensure internet connection is stable")
        print("   • Check if credentials are correct")
        return 1

if __name__ == '__main__':
    sys.exit(main())