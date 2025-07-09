# Quick test to verify date parsing fix
from main import get_date_patterns, check_mpin_strength

def test_date_parsing():
    print("Testing date parsing...")
    
    # Test DD-MM-YYYY format
    patterns = get_date_patterns("24-06-2002")
    print(f"Patterns for 24-06-2002: {patterns}")
    
    # Test if 2406 is in patterns
    if "2406" in patterns:
        print("✅ 2406 found in patterns!")
    else:
        print("❌ 2406 NOT found in patterns!")
    
    # Test the full MPIN check
    user_data = {
        'dob': '24-06-2002',
        'spouse_dob': '12-03-2003',
        'anniversary': '14-04-2003'
    }
    
    result = check_mpin_strength("2406", user_data)
    print(f"\nResult for MPIN 2406: {result}")
    
    if result['strength'] == 'WEAK' and 'DEMOGRAPHIC_DOB_SELF' in result['reasons']:
        print("✅ Correctly detected as WEAK due to DOB match!")
    else:
        print("❌ Not correctly detected!")

if __name__ == "__main__":
    test_date_parsing() 