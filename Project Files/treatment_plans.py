# modules/treatment_plans.py
def get_treatment_plan(condition):
    # Dummy logic (replace with IBM Granite model call)
    condition = condition.lower()
    if "diabetes" in condition:
        return "Treatment for diabetes may include metformin, lifestyle changes (diet/exercise), and blood sugar monitoring."
    elif "hypertension" in condition:
        return "Treatment may include ACE inhibitors, reduced salt intake, and regular blood pressure monitoring."
    else:
        return "Treatment information not available. Please consult a healthcare provider."
