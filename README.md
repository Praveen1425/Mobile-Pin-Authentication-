# MPIN Checker Project

## 🧾 Alignment with MPIN Task
This project was built for the MPIN Strength Checker task assigned by OneBanc.
It implements all requirements from Part A to Part E, and includes both CLI and web (Streamlit) interfaces for testing and demonstration.
Output format is consistent with the requirement: it returns structured results showing MPIN strength and reasons.

## About
This is a simple MPIN (Mobile Personal Identification Number) strength checker. 
It checks if your MPIN is weak or strong based on common patterns and your personal info.

## What it does
- Checks if MPIN is commonly used (like 1234, 0000)
- Checks if MPIN matches your personal dates (birthday, anniversary, spouse birthday)
- Works with both 4-digit and 6-digit MPINs
- Tells you if your MPIN is WEAK or STRONG
- Returns structured JSON output with reasons

## How to run

### Method 1: Command Line (Simple)
```bash
python main.py
```

### Method 2: Web Interface (Streamlit)
```bash
# Install streamlit first
pip install streamlit

# Run the web app
streamlit run app.py
```

### Method 3: Run tests
```bash
python test_simple.py
```

### Method 4: See examples
```bash
python demo.py
```

## How it works

### Part A: Common MPIN Check
- Loads list of common 4-digit and 6-digit MPINs
- Checks if your MPIN is in the common list
- If yes, marks as WEAK

### Part B: Demographics Check
- Takes your personal info (DOB, spouse DOB, anniversary)
- Generates possible patterns from these dates
- Checks if your MPIN matches any pattern
- If yes, marks as WEAK

### Part C: Full Check
- Combines both common and demographic checks
- Returns WEAK/STRONG with reasons

### Part D: 6-digit Support
- Same logic works for 6-digit MPINs

### Part E: Testing
- 20+ comprehensive test cases
- Covers all scenarios and edge cases

## Test Cases
The project includes 20+ test cases covering:
- Common PIN detection
- Date pattern matching
- Multiple weak reasons
- Edge cases
- Compulsory demographics requirement
- JSON structure validation

## Files
- `main.py` - Main program (command line)
- `app.py` - Web interface (Streamlit)
- `test_simple.py` - Tests
- `demo.py` - Examples
- `data/` - Common PIN lists
- `README_student.md` - This file

## Example Usage

### Command Line:
```
Enter your MPIN (4 or 6 digits):
1234

Enter your details (ALL FIELDS ARE REQUIRED):
Date formats accepted: YYYY-MM-DD or DD-MM-YYYY
Your DOB (e.g., 24-06-2002 or 2002-06-24): 24-06-2002
Spouse DOB (e.g., 12-03-2003 or 2003-03-12): 12-03-2003
Anniversary (e.g., 14-04-2003 or 2003-04-14): 14-04-2003

==================================================
RESULT:
{
  "mpin": "1234",
  "strength": "WEAK",
  "reasons": ["COMMONLY_USED"]
}
==================================================
```

### Web Interface:
1. Run `streamlit run app.py`
2. Open browser to the shown URL
3. Enter MPIN and personal info (with calendar pickers!)
4. Click "Check MPIN Strength"
5. See results with structured JSON output!

## Features
- **Compulsory demographic data** (all 3 fields required)
- **Structured JSON output** with `mpin`, `strength`, and `reasons` array
- **Calendar date pickers** for easy date selection
- **Multiple date format support** (DD-MM-YYYY, YYYY-MM-DD)
- **Both CLI and web interfaces**
- **Comprehensive testing**
- **No hardcoded values** - uses external JSON files

## Notes
- Made by a 4th year BTech student
- Simple and straightforward approach
- No hardcoded values - uses external files
- Basic error handling
- Both CLI and web interface
- Calendar pickers for user-friendly date input

## Requirements
- Python 3.x
- streamlit (for web interface)

## Deployment
This project is ready for deployment on:
- **Streamlit Cloud** - for the web interface
- **Heroku** - for both CLI and web versions
- **Local deployment** - for testing and development

## Future Improvements
- Better date parsing
- More test cases
- Better error messages
- More UI features
- API endpoint for integration

## Project Structure
```
mpin_checker_project/
├── main.py              # CLI interface
├── app.py               # Streamlit web interface
├── test_simple.py       # Test cases
├── demo.py              # Examples
├── data/
│   ├── common_4_digit.json
│   └── common_6_digit.json
├── requirements.txt     # Dependencies
└── README_student.md   # This file
``` 
