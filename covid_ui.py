from pyswip import Prolog

def generate_explanation(patient_name, risk_level, symptoms):
    print("\n================================")
    print(f"\nResult of patient {patient_name}")
    explanations = {
        'emergency': {
            'title': "🛑 EMERGENCY",
            'reason': "Life-threatening symptoms detected:",
            'actions': "CALL AMBULANCE IMMEDIATELY",
            'symptoms': {
                'bluish_lips': "Bluish lips/face (oxygen deprivation)",
                'chest_pain': "Chest pressure/pain (possible cardiac involvement)",
                'confusion': "New confusion (neurological emergency)"
            }
        },
        'high_risk': {
            'title': "🔴 HIGH RISK", 
            'reason': "Core COVID-19 indicators present:",
            'actions': "Seek PCR test + strict isolation",
            'symptoms': {
                'fever': "Fever ≥38°C",
                'dry_cough': "Persistent dry cough",
                'shortness_of_breath': "Shortness of breath at rest",
                'loss_of_taste_smell': "Sudden loss of taste/smell (97% specific to COVID)"
            }
        },
        'moderate_risk': {
            'title': "🟡 MODERATE RISK",
            'reason': "Probable COVID-19 symptoms:",
            'actions': "Home isolation + rapid antigen test",
            'symptoms': {
                'fever': "Elevated temperature",
                'dry_cough': "Dry cough",
                'sore_throat': "Sore throat (common in Omicron)",
                'fatigue': "Unusual fatigue",
                'runny_nose': "Runny nose (Omicron variant)",
                'headache': "New persistent headache"
            },
            'notes': "Consider viral variants if runny nose present"
        },
        'low_risk': {
            'title': "🟢 LOW RISK",
            'reason': "Mild or non-specific symptoms:",
            'actions': "Monitor for 48 hours",
            'symptoms': {
                'muscle_ache': "Muscle aches",
                'headache': "Mild headache",
                'congestion': "Nasal congestion",
                'sore_throat': "Mild sore throat"
            },
            'notes': "May represent common cold or allergies"
        },
        'no_risk': {
            'title': "🟢 NO SYMPTOMS",
            'reason': "No COVID-19 symptoms reported",
            'actions': "Maintain standard precautions",
            'notes': "Consider exposure history and testing if recently exposed"
        }
    }

    explanation = explanations[risk_level]
    output = [
        f"\n{explanation['title']}: {explanation['reason']}"
    ]

    if not any(symptoms.values()):
        output.append(f"\nCLINICAL NOTE: {explanation['notes']}")
    else:
        for symptom, desc in explanation['symptoms'].items():
            if symptoms.get(symptom, False):
                output.append(f"  - {desc}")
        if risk_level == 'moderate_risk' and symptoms.get('runny_nose'):
            output.append("\nNOTE: Runny nose suggests Omicron variant")

    output.append(f"\nACTION: {explanation['actions']}")
    if 'notes' in explanation and any(symptoms.values()):  
        output.append(f"\nCLINICAL NOTE: {explanation['notes']}")

    return '\n'.join(output)


def covid_symptom_checker():
    prolog = Prolog()
    prolog.consult("covid_rules.pl") 
    
    print("\nCOVID-19 Symptom Checker Expert System")
    print("-----------------------------------\n")
    
    patient = input("Enter Patient Full name : ").strip()
    prolog_patient = f"'{patient}'"
    
    list(prolog.query(f"retractall(has_symptom({prolog_patient}, _))"))
    
    symptoms = {
        'fever': input("Fever ≥38°C? (yes/no): ").lower() == 'yes',
        'dry_cough': input("Dry persistent cough? (yes/no): ").lower() == 'yes',
        'shortness_of_breath': input("Shortness of breath at rest? (yes/no): ").lower() == 'yes',
        'loss_of_taste_smell': input("Sudden loss of taste/smell? (yes/no): ").lower() == 'yes',
        'fatigue': input("Severe fatigue? (yes/no): ").lower() == 'yes',
        'sore_throat': input("Sore throat? (yes/no): ").lower() == 'yes',
        'runny_nose': input("Runny nose? (yes/no): ").lower() == 'yes',
        'muscle_ache': input("Muscle/body aches? (yes/no): ").lower() == 'yes',
        'headache': input("New persistent headache? (yes/no): ").lower() == 'yes',
        'chest_pain': input("Chest pressure/pain? (yes/no): ").lower() == 'yes',
        'confusion': input("New confusion? (yes/no): ").lower() == 'yes',
        'congestion': input("Nasal congestion? (yes/no): ").lower() == 'yes',
        'bluish_lips': input("Bluish lips/face? (yes/no): ").lower() == 'yes'
    }
    
    symptom_detected = {
        'bluish_lips': "Bluish lips/face",
        'chest_pain': "Chest pressure/pain",
        'confusion': "New confusion",
        'fever': "Fever ≥38°C",
        'dry_cough': "Dry cough",
        'shortness_of_breath': "Shortness of breath",
        'loss_of_taste_smell': "Sudden loss of taste/smell",
        'sore_throat': "Sore throat",
        'fatigue': "Unusual fatigue",
        'runny_nose': "Runny nose ",
        'headache': "Persistent headache",
        'muscle_ache': "Muscle aches",
        'congestion': "Nasal congestion",
    }
    print("\nSyptoms Detected!")
    for key, value in symptom_detected.items():
        if symptoms[key]: 
            print(f" - {value}")

    
    for symptom, present in symptoms.items():
        if present:
            prolog.assertz(f"has_symptom({prolog_patient}, {symptom})")
    
    result = ""
    if list(prolog.query(f"no_risk({prolog_patient})")): 
        result = 'no_risk'
    elif list(prolog.query(f"emergency({prolog_patient})")):
        result = "emergency"
    elif list(prolog.query(f"high_risk({prolog_patient})")):
        result = "high_risk"
    elif list(prolog.query(f"moderate_risk({prolog_patient})")):
        result = "moderate_risk"
    else:
        result = "low_risk"
    
    print(f"{generate_explanation(prolog_patient,result,symptoms)}\n")
    
if __name__ == "__main__":
    covid_symptom_checker()
    while(True):
        cont = input("Continue next patient? (yes/no) : ").lower()
        if cont in ('yes', 'no'):
            if(cont=='yes'):
                covid_symptom_checker()
            elif(cont=='no'):
                print("\n 😁Chow")
                exit()
            break
        print("Please enter 'yes' or 'no'")
        