import time
from ai_test_optimizer import get_optimized_test_order
from test_logger import log_test_result

# Mock test suite for demonstration purposes
def test_example():
    """A sample test that passes."""
    time.sleep(1)  # Simulate test runtime
    return True

def test_example_fail():
    """A sample test that fails."""
    time.sleep(2)  # Simulate test runtime
    return False

def test_another():
    """Another sample test that passes."""
    time.sleep(0.5)  # Simulate test runtime
    return True

# Mapping of test names to test functions
TEST_SUITE = {
    "test_example": test_example,
    "test_example_fail": test_example_fail,
    "test_another": test_another,
}

def run_tests():
    """
    Run the test suite in optimized order and log each result.
    """
    # Get the optimized test execution order
    optimized_order = get_optimized_test_order()
    print("Running tests in optimized order:", optimized_order)
    
    for test_name in optimized_order:
        if test_name not in TEST_SUITE:
            print(f"Warning: Test '{test_name}' not found in the test suite.")
            continue
        
        test_func = TEST_SUITE[test_name]
        start_time = time.time()
        
        try:
            # Execute the test and determine pass/fail
            passed = test_func()
        except Exception as e:
            print(f"Test '{test_name}' encountered an error: {e}")
            passed = False
        
        end_time = time.time()
        duration = end_time - start_time
        
        # Log the result
        log_test_result(test_name, duration, passed)
        print(f"Test '{test_name}' {'PASSED' if passed else 'FAILED'} in {duration:.2f} seconds.")

if __name__ == "__main__":
    run_tests()