
:- dynamic has_symptom/2.

% Symptoms
symptom(fever).
symptom(dry_cough).
symptom(shortness_of_breath).
symptom(loss_of_taste_smell).
symptom(sore_throat).
symptom(fatigue).
symptom(runny_nose).
symptom(headache).
symptom(muscle_ache).
symptom(congestion).
symptom(bluish_lips).
symptom(chest_pain).
symptom(confusion).

% Risk Assessment Rules
high_risk(Patient) :-
    has_symptom(Patient, fever),
    has_symptom(Patient, dry_cough),
    has_symptom(Patient, shortness_of_breath).

high_risk(Patient) :-
    has_symptom(Patient, loss_of_taste_smell),
    (has_symptom(Patient, fever); has_symptom(Patient, dry_cough)).

moderate_risk(Patient) :-
    has_symptom(Patient, fever),
    has_symptom(Patient, dry_cough),
    \+ has_symptom(Patient, shortness_of_breath),
    \+ has_symptom(Patient, loss_of_taste_smell).

moderate_risk(Patient) :-
    has_symptom(Patient, sore_throat),
    has_symptom(Patient, fatigue),
    has_symptom(Patient, runny_nose),
    (has_symptom(Patient, fever); has_symptom(Patient, headache)).

low_risk(Patient) :-
    \+ emergency(Patient),
    \+ high_risk(Patient),
    \+ moderate_risk(Patient),
    (has_symptom(Patient, muscle_ache); 
    has_symptom(Patient, headache); 
    has_symptom(Patient, congestion)).

emergency(Patient) :-
    has_symptom(Patient, bluish_lips);
    has_symptom(Patient, chest_pain);
    has_symptom(Patient, confusion).

no_risk(Patient) :-
    \+ has_symptom(Patient, _).
    
clear_facts :-
    retractall(has_symptom(_, _)).
