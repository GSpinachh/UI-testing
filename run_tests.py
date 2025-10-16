import pytest
import sys

if __name__ == "__main__":
    result = pytest.main([
        "tests/", 
        "-v", 
        "--tb=short",
        "-s",
        "--strict-markers"
    ])
    
    sys.exit(result)