# Test calendar date picker functionality
from datetime import date
from main import check_mpin_strength

def test_calendar_dates():
    """Test that calendar dates work correctly"""
    print("Testing calendar date functionality...")
    
    # Simulate calendar picker dates (these would come from st.date_input)
    calendar_dob = date(2002, 6, 24)  # 24-06-2002
    calendar_spouse_dob = date(2003, 3, 12)  # 12-03-2003
    calendar_anniversary = date(2003, 4, 14)  # 14-04-2003
    
    # Convert to string format (like the app does)
    user_data = {
        'dob': calendar_dob.strftime("%d-%m-%Y"),
        'spouse_dob': calendar_spouse_dob.strftime("%d-%m-%Y"),
        'anniversary': calendar_anniversary.strftime("%d-%m-%Y")
    }
    
    print(f"Calendar dates converted to: {user_data}")
    
    # Test MPIN that should match DOB
    result = check_mpin_strength("2406", user_data)
    print(f"\nMPIN 2406 result: {result}")
    
    if result['strength'] == 'WEAK' and 'DEMOGRAPHIC_DOB_SELF' in result['reasons']:
        print("✅ Calendar dates working correctly!")
    else:
        print("❌ Calendar dates not working!")
    
    # Test MPIN that should match spouse DOB
    result = check_mpin_strength("1203", user_data)
    print(f"\nMPIN 1203 result: {result}")
    
    if result['strength'] == 'WEAK' and 'DEMOGRAPHIC_DOB_SPOUSE' in result['reasons']:
        print("✅ Spouse DOB detection working!")
    else:
        print("❌ Spouse DOB detection not working!")
    
    # Test MPIN that should match anniversary
    result = check_mpin_strength("1404", user_data)
    print(f"\nMPIN 1404 result: {result}")
    
    if result['strength'] == 'WEAK' and 'DEMOGRAPHIC_ANNIVERSARY' in result['reasons']:
        print("✅ Anniversary detection working!")
    else:
        print("❌ Anniversary detection not working!")

if __name__ == "__main__":
    test_calendar_dates() 