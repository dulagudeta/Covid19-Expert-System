
# COVID-19 Symptom Checker Expert System

## Overview

This expert system evaluates COVID-19 risk levels based on reported symptoms. It combines Prolog for logical rule-based assessment with a Python interface for user interaction. The system categorizes patients into five risk levels (Emergency, High, Moderate, Low, and No Risk) and provides detailed explanations and recommended actions.

## Features

- **Symptom Analysis**: Evaluates 13 COVID-19 related symptoms
- **Risk Assessment**: 
  - Emergency (life-threatening symptoms)
  - High Risk (core COVID indicators)
  - Moderate Risk (probable COVID symptoms)
  - Low Risk (mild/non-specific symptoms)
  - No Risk (asymptomatic)
- **Detailed Explanations**: Provides symptom-specific clinical notes
- **Actionable Recommendations**: Clear next steps for each risk level
- **Multi-patient Support**: Process multiple patients in one session

## System Components

1. **Prolog Knowledge Base (`covid_rules.pl`)**
   - Defines symptoms and risk assessment rules
   - Uses logical predicates to determine risk levels
   - Includes dynamic fact retraction for clean sessions

2. **Python Interface (`covid_ui.py`)**
   - Collects patient information and symptoms
   - Displays detected symptoms
   - Generates detailed risk assessment reports
   - Manages user interaction flow

## Installation Requirements

- Python 3.x
- PySwip library (for Prolog-Python integration)
- SWI-Prolog installed on your system

Install PySwip with:
```
pip install pyswip
```

## Usage

1. Run the program:
   ```
   python covid_ui.py
   ```

2. Enter patient information when prompted

3. Answer symptom questions (yes/no)

4. Review the risk assessment and recommendations

5. Choose to continue with another patient or exit

## Risk Assessment Logic

- **Emergency**: Bluish lips, chest pain, or confusion
- **High Risk**: 
  - Fever + dry cough + shortness of breath, OR
  - Loss of taste/smell + (fever or dry cough)
- **Moderate Risk**:
  - Fever + dry cough without severe symptoms, OR
  - Sore throat + fatigue + runny nose + (fever or headache)
- **Low Risk**: Mild symptoms without higher-risk indicators
- **No Risk**: No symptoms reported

## Example Output

```
================================

Result of patient 'John Doe'

🔴 HIGH RISK: Core COVID-19 indicators present:
  - Fever ≥38°C
  - Persistent dry cough
  - Shortness of breath at rest

ACTION: Seek PCR test + strict isolation
```

## Notes

- The system is designed for educational/decision-support purposes only
- Always consult a healthcare professional for medical advice
- Rules are based on typical COVID-19 symptom patterns and may need updating for new variants

## License

This project is open-source and available for educational use. For commercial applications, please contact the developer.

Made with ❤️ by [dulagudeta](https://github.com/dulagudeta)  
Feel free to tweak this for your needs!
