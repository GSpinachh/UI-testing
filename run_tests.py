import pytest
import sys

if __name__ == "__main__":

    result = pytest.main([
        "tests/test_sample_form.py", 
        "tests/test_bank_manager.py",
        "tests/test_customer_operations.py",
        "-v", 
        "--tb=short",
        "-s",
        "--strict-markers"
    ])
    
    sys.exit(result)