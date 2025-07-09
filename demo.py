# Demo script for MPIN Checker
# Shows different examples

from main import check_mpin_strength

def demo_common_pins():
    """Demo common PIN detection"""
    print("=== Demo: Common PINs ===")
    
    test_pins = ["1234", "0000", "4821", "123456", "482193"]
    user_data = {'dob': '1990-01-01', 'spouse_dob': '1985-01-01', 'anniversary': '2010-01-01'}
    
    for pin in test_pins:
        result = check_mpin_strength(pin, user_data)
        print(f"PIN: {pin} -> {result['strength']}")
        if result['reasons']:
            print(f"  Reasons: {result['reasons']}")
        print()

def demo_demographics():
    """Demo demographic pattern detection"""
    print("=== Demo: Demographics ===")
    
    user_data = {
        'dob': '1990-01-23',
        'spouse_dob': '1985-12-05',
        'anniversary': '2010-07-15'
    }
    
    test_pins = ["2301", "0512", "1507", "4821"]
    
    for pin in test_pins:
        result = check_mpin_strength(pin, user_data)
        print(f"PIN: {pin} -> {result['strength']}")
        if result['reasons']:
            print(f"  Reasons: {result['reasons']}")
        print()

def demo_multiple_reasons():
    """Demo when PIN has multiple weak reasons"""
    print("=== Demo: Multiple Reasons ===")
    
    user_data = {'dob': '1990-01-23', 'spouse_dob': '1985-01-01', 'anniversary': '2010-01-01'}
    
    # 1234 is both common and matches DOB pattern
    result = check_mpin_strength("1234", user_data)
    print(f"PIN: 1234 -> {result['strength']}")
    print(f"  Reasons: {result['reasons']}")
    print()

def demo_6_digit():
    """Demo 6-digit PINs"""
    print("=== Demo: 6-digit PINs ===")
    
    user_data = {'dob': '1990-01-23', 'spouse_dob': '1985-01-01', 'anniversary': '2010-01-01'}
    
    test_pins = ["123456", "230190", "482193"]
    
    for pin in test_pins:
        result = check_mpin_strength(pin, user_data)
        print(f"PIN: {pin} -> {result['strength']}")
        if result['reasons']:
            print(f"  Reasons: {result['reasons']}")
        print()

def demo_json_structure():
    """Demo JSON structure output"""
    print("=== Demo: JSON Structure ===")
    
    user_data = {'dob': '1990-01-23', 'spouse_dob': '1985-01-01', 'anniversary': '2010-01-01'}
    
    test_cases = [
        ("1234", "Common weak PIN"),
        ("4821", "Strong PIN"),
        ("2301", "DOB pattern")
    ]
    
    for pin, description in test_cases:
        result = check_mpin_strength(pin, user_data)
        print(f"\n{description}:")
        print(f"Input: {pin}")
        print(f"Output: {result}")
        print()

def demo_compulsory_demographics():
    """Demo compulsory demographics requirement"""
    print("=== Demo: Compulsory Demographics ===")
    
    # Test with no demographics
    result = check_mpin_strength("1234", None)
    print(f"No demographics provided:")
    print(f"Result: {result}")
    print()
    
    # Test with partial demographics
    partial_data = {'dob': '1990-01-23'}
    result = check_mpin_strength("1234", partial_data)
    print(f"Partial demographics provided:")
    print(f"Result: {result}")
    print()

def run_demo():
    """Run all demos"""
    print("MPIN Checker Demo")
    print("=" * 50)
    
    demo_common_pins()
    demo_demographics()
    demo_multiple_reasons()
    demo_6_digit()
    demo_json_structure()
    demo_compulsory_demographics()
    
    print("Demo completed!")

if __name__ == "__main__":
    run_demo() 