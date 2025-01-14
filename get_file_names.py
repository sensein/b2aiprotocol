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
            "activities/completed_by/completed_by_schema",
            "activities/required/activities/address/items/city",
            "b2ai_redcap2rs_activities:q_generic_demographics/items/state_province",
            "b2ai_redcap2rs_activities:q_generic_demographics/items/zipcode",
            "b2ai_redcap2rs_activities:q_generic_demographics/items/country",
            "activities/required/activities/gender/items/gender_identity",
            "activities/required/activities/gender/items/specify_gender_identity",
            "activities/required/activities/sexuality/items/sexual_orientation",
            "b2ai_redcap2rs_activities:q_generic_demographics/items/race",
            "b2ai_redcap2rs_activities:q_generic_demographics/items/native_american_race",
            "b2ai_redcap2rs_activities:q_generic_demographics/items/asian_race",
            "b2ai_redcap2rs_activities:q_generic_demographics/items/black_race",
            "b2ai_redcap2rs_activities:q_generic_demographics/items/pacific_islander_race",
            "b2ai_redcap2rs_activities:q_generic_demographics/items/white_race",
            "b2ai_redcap2rs_activities:q_generic_demographics/items/canadian_race",
            "b2ai_redcap2rs_activities:q_generic_demographics/items/other_race_specify",
            "b2ai_redcap2rs_activities:q_generic_demographics/items/ethnicity",
            "b2ai_redcap2rs_activities:q_generic_demographics/items/hispanic_latino_selection",
            "activities/required/activities/education/items/edu_level",
            "activities/required/activities/disability/items/hearing",
            "b2ai_redcap2rs_activities:q_generic_demographics/items/vision",
            "b2ai_redcap2rs_activities:q_generic_demographics/items/cognition",
            "b2ai_redcap2rs_activities:q_generic_demographics/items/mobility",
            "b2ai_redcap2rs_activities:q_generic_demographics/items/self_care",
            "activities/required/activities/disability/items/independent_living",
            "required/activities/employment/items/employ_status",
            "b2ai_redcap2rs_activities:q_generic_demographics/items/other_employ_specify",
            "b2ai_redcap2rs_activities:q_generic_demographics/items/occupation",
            "b2ai_redcap2rs_activities:q_generic_demographics/items/veteran",
            "b2ai_redcap2rs_activities:q_generic_demographics/items/country",
            "activities/optional/items/household_income_usa",
            "activities/optional/items/financial_assistance_usa",
            "activities/optional/items/assistance_programs_usa",
            "activities/optional/items/household_income_ca",
            "activities/optional/items/financial_assistance_ca",
            "activities/optional/items/assistance_programs_ca",
            "b2ai_redcap2rs_activities:q_generic_demographics/items/citizen",
            "b2ai_redcap2rs_activities:q_generic_demographics/items/marital_status",
            "b2ai_redcap2rs_activities:q_generic_demographics/items/housing_status",
            "b2ai_redcap2rs_activities:q_generic_demographics/items/household_count",
            "activities/optional/items/household_composition",
            "b2ai_redcap2rs_activities:q_generic_demographics/items/others_household_specify",
            "b2ai_redcap2rs_activities:q_generic_demographics/items/transportation_yn",
            "b2ai_redcap2rs_activities:q_generic_demographics/items/primary_transportation",
            "b2ai_redcap2rs_activities:q_generic_demographics/items/other_transportation"
"""

# Extracting file names
file_names = extract_file_names(text)
for name in file_names:
    print(name)
