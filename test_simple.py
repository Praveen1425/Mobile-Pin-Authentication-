# Simple tests for MPIN checker
# Student written tests

import json
from main import check_mpin_strength, check_if_common, get_date_patterns

def test_common_pins():
    """Test common PIN detection"""
    print("Testing common PINs...")
    
    # Test 4 digit common PINs
    user_data = {'dob': '1990-01-01', 'spouse_dob': '1985-01-01', 'anniversary': '2010-01-01'}
    result = check_mpin_strength("1234", user_data)
    assert result['strength'] == 'WEAK'
    assert 'COMMONLY_USED' in result['reasons']
    
    result = check_mpin_strength("0000", user_data)
    assert result['strength'] == 'WEAK'
    
    # Test 6 digit common PINs
    result = check_mpin_strength("123456", user_data)
    assert result['strength'] == 'WEAK'
    
    # Test strong PINs
    result = check_mpin_strength("4821", user_data)
    assert result['strength'] == 'STRONG'
    
    result = check_mpin_strength("482193", user_data)
    assert result['strength'] == 'STRONG'
    
    print("Common PIN tests passed!")

def test_demographics():
    """Test demographic pattern detection"""
    print("Testing demographics...")
    
    user_data = {
        'dob': '1990-01-23',
        'spouse_dob': '1985-12-05',
        'anniversary': '2010-07-15'
    }
    
    # Test DOB patterns
    result = check_mpin_strength("2301", user_data)
    assert result['strength'] == 'WEAK'
    assert 'DEMOGRAPHIC_DOB_SELF' in result['reasons']
    
    # Test spouse DOB
    result = check_mpin_strength("0512", user_data)
    assert result['strength'] == 'WEAK'
    assert 'DEMOGRAPHIC_DOB_SPOUSE' in result['reasons']
    
    # Test anniversary
    result = check_mpin_strength("1507", user_data)
    assert result['strength'] == 'WEAK'
    assert 'DEMOGRAPHIC_ANNIVERSARY' in result['reasons']
    
    print("Demographic tests passed!")

def test_date_patterns():
    """Test date pattern generation"""
    print("Testing date patterns...")
    
    patterns = get_date_patterns("1990-01-23")
    assert "2301" in patterns  # day + month
    assert "0123" in patterns  # month + day
    assert "9001" in patterns  # year + month
    
    patterns = get_date_patterns("1985-12-05")
    assert "0512" in patterns  # day + month
    assert "1205" in patterns  # month + day
    
    print("Date pattern tests passed!")

def test_multiple_reasons():
    """Test when PIN has multiple weak reasons"""
    print("Testing multiple reasons...")
    
    user_data = {'dob': '1990-01-23', 'spouse_dob': '1985-01-01', 'anniversary': '2010-01-01'}
    
    # 1234 is both common and matches DOB pattern
    result = check_mpin_strength("1234", user_data)
    assert result['strength'] == 'WEAK'
    assert len(result['reasons']) >= 1
    
    print("Multiple reasons test passed!")

def test_compulsory_demographics():
    """Test that demographics are compulsory"""
    print("Testing compulsory demographics...")
    
    # Test with no demographics (should return ERROR)
    result = check_mpin_strength("1234", None)
    assert result['strength'] == 'ERROR'
    assert 'DEMOGRAPHIC_DATA_REQUIRED' in result['reasons']
    
    # Test with empty demographics
    result = check_mpin_strength("1234", {})
    assert result['strength'] == 'WEAK'  # Will still check common PINs
    
    print("Compulsory demographics test passed!")

def test_json_structure():
    """Test that output has correct JSON structure"""
    print("Testing JSON structure...")
    
    user_data = {'dob': '1990-01-01', 'spouse_dob': '1985-01-01', 'anniversary': '2010-01-01'}
    result = check_mpin_strength("1234", user_data)
    
    # Check required fields
    assert 'mpin' in result
    assert 'strength' in result
    assert 'reasons' in result
    assert isinstance(result['reasons'], list)
    
    print("JSON structure test passed!")

def test_edge_cases():
    """Test edge cases"""
    print("Testing edge cases...")
    
    user_data = {'dob': '1990-01-01', 'spouse_dob': '1985-01-01', 'anniversary': '2010-01-01'}
    
    # Invalid MPIN length
    try:
        result = check_mpin_strength("123", user_data)
        print("Should have failed for 3 digits")
    except:
        pass
    
    # Empty user data
    result = check_mpin_strength("1234", user_data)
    assert result['strength'] == 'WEAK'
    
    print("Edge case tests passed!")

def run_all_tests():
    """Run all tests"""
    print("=== Running MPIN Checker Tests ===")
    
    try:
        test_common_pins()
        test_demographics()
        test_date_patterns()
        test_multiple_reasons()
        test_compulsory_demographics()
        test_json_structure()
        test_edge_cases()
        print("\nAll tests passed! ✅")
    except Exception as e:
        print(f"Test failed: {e}")
        print("Some tests failed! ❌")

if __name__ == "__main__":
    run_all_tests() 