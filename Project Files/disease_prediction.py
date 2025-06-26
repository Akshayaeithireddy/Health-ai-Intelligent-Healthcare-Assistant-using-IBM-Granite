# modules/disease_prediction.py
def predict_disease(symptoms):
    # Dummy logic (replace with real model or API call)
    symptoms_list = [s.strip().lower() for s in symptoms.split(',')]
    if "fever" in symptoms_list and "cough" in symptoms_list:
        return "You may have the flu or COVID-19. Please consult a doctor."
    elif "headache" in symptoms_list:
        return "Possible causes include stress, dehydration, or migraine."
    else:
        return "Symptoms are unclear. Please provide more detailed input."
