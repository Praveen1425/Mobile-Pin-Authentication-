# Simple Streamlit app for MPIN Checker
# Made by a 4th year BTech student

import streamlit as st
import json
from datetime import datetime, date
from main import check_mpin_strength

def load_common_pins():
    """Load common PINs from files"""
    try:
        with open('data/common_4_digit.json', 'r') as f:
            common_4 = json.load(f)
        with open('data/common_6_digit.json', 'r') as f:
            common_6 = json.load(f)
        return common_4, common_6
    except:
        st.error("Error loading data files")
        return [], []

def format_date_for_display(d):
    """Format date for display"""
    if d:
        return d.strftime("%d-%m-%Y")
    return ""

def main():
    st.title("MPIN Strength Checker")
    st.write("Check if your MPIN is weak or strong!")
    
    # Sidebar with info
    st.sidebar.header("About")
    st.sidebar.write("""
    This app checks your MPIN against:
    - Common PINs (like 1234, 0000)
    - Your personal dates (birthday, anniversary, spouse birthday)
    
    **All demographic fields are required!**
    """)
    
    # Main input section
    st.header("Enter Your MPIN")
    
    mpin = st.text_input("MPIN (4 or 6 digits)", max_chars=6)
    
    if mpin:
        if not mpin.isdigit():
            st.error("MPIN must contain only numbers!")
        elif len(mpin) not in [4, 6]:
            st.error("MPIN must be 4 or 6 digits!")
        else:
            st.success(f"Valid MPIN: {mpin}")
    
    # Demographics section (COMPULSORY) with calendar pickers
    st.header("Personal Information (REQUIRED)")
    st.write("**All fields below are mandatory:**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Your Details")
        dob = st.date_input("Your Date of Birth *", 
                           min_value=date(1900, 1, 1),
                           max_value=date.today(),
                           help="Select your birth date")
        
        spouse_dob = st.date_input("Spouse Date of Birth *",
                                  min_value=date(1900, 1, 1),
                                  max_value=date.today(),
                                  help="Select your spouse's birth date")
    
    with col2:
        st.subheader("Anniversary")
        anniversary = st.date_input("Wedding Anniversary *",
                                  min_value=date(1900, 1, 1),
                                  max_value=date.today(),
                                  help="Select your wedding anniversary date")
        
        # Show selected dates
        if dob:
            st.write(f"**Your DOB:** {format_date_for_display(dob)}")
        if spouse_dob:
            st.write(f"**Spouse DOB:** {format_date_for_display(spouse_dob)}")
        if anniversary:
            st.write(f"**Anniversary:** {format_date_for_display(anniversary)}")
    
    # Alternative text input for manual entry
    st.subheader("Manual Date Entry (Alternative)")
    st.write("If you prefer to type dates manually:")
    
    col3, col4 = st.columns(2)
    
    with col3:
        dob_manual = st.text_input("Your DOB (DD-MM-YYYY) *", 
                                  placeholder="24-06-2002",
                                  help="Enter in DD-MM-YYYY format")
        spouse_dob_manual = st.text_input("Spouse DOB (DD-MM-YYYY) *", 
                                         placeholder="12-03-2003",
                                         help="Enter in DD-MM-YYYY format")
    
    with col4:
        anniversary_manual = st.text_input("Anniversary (DD-MM-YYYY) *", 
                                         placeholder="14-04-2003",
                                         help="Enter in DD-MM-YYYY format")
    
    # Choose which input method to use
    use_calendar = st.checkbox("Use calendar picker (recommended)", value=True)
    
    # Prepare user data based on selected method
    if use_calendar:
        # Use calendar picker dates
        all_fields_filled = dob and spouse_dob and anniversary
        
        if all_fields_filled:
            user_data = {
                'dob': dob.strftime("%d-%m-%Y"),
                'spouse_dob': spouse_dob.strftime("%d-%m-%Y"),
                'anniversary': anniversary.strftime("%d-%m-%Y")
            }
        else:
            user_data = None
            st.warning("⚠️ Please select all dates using the calendar pickers!")
    else:
        # Use manual text input
        all_fields_filled = dob_manual and spouse_dob_manual and anniversary_manual
        
        if all_fields_filled:
            user_data = {
                'dob': dob_manual,
                'spouse_dob': spouse_dob_manual,
                'anniversary': anniversary_manual
            }
        else:
            user_data = None
            st.warning("⚠️ Please fill in all date fields manually!")
    
    # Check button
    if st.button("Check MPIN Strength", type="primary"):
        if not mpin or not mpin.isdigit() or len(mpin) not in [4, 6]:
            st.error("Please enter a valid MPIN first!")
        elif not all_fields_filled:
            st.error("Please fill in ALL demographic fields!")
        else:
            # Check strength
            result = check_mpin_strength(mpin, user_data)
            
            # Display results
            st.header("Results")
            
            # Show structured JSON output
            st.subheader("Structured Output:")
            st.json(result)
            
            # Show user-friendly results
            st.subheader("Summary:")
            if result['strength'] == 'STRONG':
                st.success("✅ Your MPIN is STRONG!")
            else:
                st.error("❌ Your MPIN is WEAK!")
            
            # Show reasons
            if result['reasons']:
                st.write("**Reasons why it's weak:**")
                for reason in result['reasons']:
                    st.write(f"- {reason}")
            
            # Show some stats
            st.write("---")
            st.write(f"**MPIN Length:** {len(mpin)} digits")
            st.write(f"**Common PINs checked:** {len(load_common_pins()[0]) + len(load_common_pins()[1])}")
            
            # Show date patterns that were checked
            st.write("**Date patterns checked:**")
            if user_data:
                st.write(f"- Your DOB: {user_data['dob']}")
                st.write(f"- Spouse DOB: {user_data['spouse_dob']}")
                st.write(f"- Anniversary: {user_data['anniversary']}")
    
    # Examples section
    st.header("Examples")
    
    if st.button("Show Examples"):
        st.write("**Common weak PINs:**")
        st.code("1234, 0000, 1111, 123456")
        
        st.write("**Strong PINs:**")
        st.code("4821, 9374, 482193")
        
        st.write("**Date patterns (if DOB is 24-06-2002):**")
        st.code("2406, 0624, 0206 (day+month, month+day, year+month)")
        
        st.write("**Example JSON Output:**")
        example_output = {
            "mpin": "2406",
            "strength": "WEAK",
            "reasons": ["DEMOGRAPHIC_DOB_SELF"]
        }
        st.json(example_output)
    
    # Footer
    st.write("---")
    st.write("Simple and straightforward approach!")

if __name__ == "__main__":
    main() 