# MPIN Checker - Simple version
# Made by a 4th year BTech student
# This checks if MPIN is weak or strong

import json
import os

def load_common_pins():
    """Load common PINs from files"""
    try:
        with open('data/common_4_digit.json', 'r') as f:
            common_4 = json.load(f)
        with open('data/common_6_digit.json', 'r') as f:
            common_6 = json.load(f)
        return common_4, common_6
    except:
        print("Error loading data files")
        return [], []

def check_if_common(mpin, common_4, common_6):
    """Check if MPIN is in common list"""
    if len(mpin) == 4:
        return mpin in common_4
    elif len(mpin) == 6:
        return mpin in common_6
    return False

def get_date_patterns(date_str):
    """Get possible patterns from date"""
    if not date_str:
        return []
    
    # Try to parse date - student approach
    patterns = []
    try:
        # Handle multiple date formats
        if '-' in date_str:
            parts = date_str.split('-')
            if len(parts) == 3:
                # Try different formats
                # Format 1: YYYY-MM-DD
                if len(parts[0]) == 4:  # year first
                    year = parts[0]
                    month = parts[1]
                    day = parts[2]
                # Format 2: DD-MM-YYYY  
                elif len(parts[2]) == 4:  # year last
                    day = parts[0]
                    month = parts[1]
                    year = parts[2]
                else:
                    return patterns
                
                # 4 digit patterns
                patterns.append(day + month)
                patterns.append(month + day)
                patterns.append(year[2:] + month)
                patterns.append(month + year[2:])
                
                # 6 digit patterns
                patterns.append(day + month + year[2:])
                patterns.append(year[2:] + month + day)
                patterns.append(day + month + year)
                patterns.append(year + month + day)
    except:
        pass
    
    return patterns

def check_demographics(mpin, user_data):
    """Check if MPIN matches user demographics"""
    reasons = []
    
    # Check own DOB
    if user_data.get('dob'):
        dob_patterns = get_date_patterns(user_data['dob'])
        if mpin in dob_patterns:
            reasons.append('DEMOGRAPHIC_DOB_SELF')
    
    # Check spouse DOB
    if user_data.get('spouse_dob'):
        spouse_patterns = get_date_patterns(user_data['spouse_dob'])
        if mpin in spouse_patterns:
            reasons.append('DEMOGRAPHIC_DOB_SPOUSE')
    
    # Check anniversary
    if user_data.get('anniversary'):
        ann_patterns = get_date_patterns(user_data['anniversary'])
        if mpin in ann_patterns:
            reasons.append('DEMOGRAPHIC_ANNIVERSARY')
    
    return reasons

def check_mpin_strength(mpin, user_data):
    """Main function to check MPIN strength - demographics are compulsory"""
    if not user_data:
        return {
            'mpin': mpin,
            'strength': 'ERROR',
            'reasons': ['DEMOGRAPHIC_DATA_REQUIRED']
        }
    
    common_4, common_6 = load_common_pins()
    
    reasons = []
    
    # Check if common
    if check_if_common(mpin, common_4, common_6):
        reasons.append('COMMONLY_USED')
    
    # Check demographics (compulsory)
    demo_reasons = check_demographics(mpin, user_data)
    reasons.extend(demo_reasons)
    
    # Determine strength
    if reasons:
        strength = 'WEAK'
    else:
        strength = 'STRONG'
    
    return {
        'mpin': mpin,
        'strength': strength,
        'reasons': reasons
    }

def main():
    """Main program"""
    print("=== MPIN Strength Checker ===")
    print("Enter your MPIN (4 or 6 digits):")
    mpin = input().strip()
    
    if not mpin.isdigit() or len(mpin) not in [4, 6]:
        print("Invalid MPIN! Must be 4 or 6 digits.")
        return
    
    print("\nEnter your details (ALL FIELDS ARE REQUIRED):")
    print("Date formats accepted: YYYY-MM-DD or DD-MM-YYYY")
    dob = input("Your DOB (e.g., 24-06-2002 or 2002-06-24): ").strip()
    spouse_dob = input("Spouse DOB (e.g., 12-03-2003 or 2003-03-12): ").strip()
    anniversary = input("Anniversary (e.g., 14-04-2003 or 2003-04-14): ").strip()
    
    # Check if all fields are provided
    if not dob or not spouse_dob or not anniversary:
        print("ERROR: All demographic fields are required!")
        return
    
    user_data = {
        'dob': dob,
        'spouse_dob': spouse_dob,
        'anniversary': anniversary
    }
    
    result = check_mpin_strength(mpin, user_data)
    
    # Print structured JSON output
    print("\n" + "="*50)
    print("RESULT:")
    print(json.dumps(result, indent=2))
    print("="*50)

if __name__ == "__main__":
    main() 