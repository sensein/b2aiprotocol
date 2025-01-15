import re

def extract_file_names(paths):
    """
    Extracts only the file names from a list of paths.

    Args:
        paths (list or str): A list of path strings or a single string containing paths separated by commas.

    Returns:
        list: A list of file names extracted from the paths.
    """
    if isinstance(paths, str):
        # Split the single string into a list of paths
        paths = [path.strip().strip('"') for path in paths.split(",") if path.strip()]
    
    # Extract file names using regex
    file_names = [re.search(r'[^/]+$', path).group() for path in paths]
    return file_names

# Example usage:
text = """
"items/confounders_session_id",
            "items/confounders_started_at",
            "items/confounders_completed_at",
            "items/confounders_duration",
            "items/smoking_entire_life",
            "items/smoking_occurrence",
            "items/smoking_age_regular_cigarette_smoking",
            "items/smoking_age_regular_cigarette_smoking_age",
            "items/smoking_age_stopped",
            "items/smoking_age_stopped_age",
            "items/smoking_years_cigarettes",
            "items/smoking_years_cigarettes_years",
            "items/smoking_cigarettes_day_current_avg",
            "items/smoking_cigarettes_day_current_avg_number",
            "items/smoking_cigarettes_day_past_avg",
            "items/smoking_cigarettes_day_past_avg_number",
            "items/smoking_marijuana",
            "items/smoking_electronic",
            "items/smoking_electronic_current_occurence",
            "items/is_regular_smoker",
            "items/smoking_hx",
            "items/age_start_smoking",
            "items/age_stop_smoking",
            "items/smoking_types",
            "items/smoking_freq",
            "items/other_smoking_specify",
            "items/alcohol_yn",
            "items/alcohol_freq",
            "items/alcohol_amt",
            "items/alcohol_drinks",
            "items/alcohol_today",
            "items/drinks_today_number",
            "items/alcohol_rehab",
            "items/current_recovery_alcohol",
            "items/recreational_drug_use",
            "items/substance_use_recovery",
            "items/painkillers",
            "items/stimulants",
            "items/sedatives",
            "items/marijuana",
            "items/cocaine",
            "items/club_drugs",
            "items/hallucinogens",
            "items/heroin",
            "items/inhalants",
            "items/methamphetamine",
            "items/caffeine_intake",
            "items/caffeine_intake_today",
            "items/hydration",
            "items/hydration_today",
            "items/dental_problems",
            "items/dental_tx",
            "items/seasonal_allergies",
            "items/seasonal_allergies_options",
            "items/tired_measure",
            "items/height",
            "items/weight",
            "items/unit",
            "items/symptoms",
            "items/ear_med_history",
            "items/nose_med_history",
            "items/throat_med_history",
            "items/head_med_history",
            "items/ear_surgical",
            "items/nose_surgical",
            "items/throat_surgical",
            "items/head_surgical",
            "items/neurological_history",
            "items/current_neuro_dx",
            "items/specify_current_neuro",
            "items/respiratory_conditions",
            "items/lung_or_metastatic",
            "items/covid",
            "items/covid_past",
            "items/cpap_conditions",
            "items/resp_medical_history",
            "items/exposed_environmental_pollution",
            "items/breathe_today",
            "items/breathe_today_difficulty",
            "items/cough_today",
            "items/cough_today_severity",
            "items/circulatory_conditions",
            "items/cardiac_condition",
            "items/circulatory_med_history",
            "items/infection_disease",
            "items/ph_standing",
            "items/ph_take_care",
            "items/ph_learn_task",
            "items/ph_problem_join",
            "items/ph_health_problem",
            "items/ph_concentrating",
            "items/ph_walking",
            "items/ph_washing",
            "items/ph_get_dressed",
            "items/ph_dealing_people",
            "items/ph_friendship",
            "items/ph_day_to_day_work",
            "items/physical_health_freq",
            "items/phys_health_impact",
            "items/phys_health_limited",
            "items/medications",
            "items/hormone_use",
            "items/pain_medication",
            "items/menstruate",
            "items/menstruate_no",
            "items/other_menstruate_specify",
            "items/menstrual_cycle_status",
            "items/voice_activity",
            "items/other_voice_activity",
            "items/hours_voice_activity",
            "items/reading_aloud"
"""

# Extracting file names
file_names = extract_file_names(text)
for name in file_names:
    print(name)
