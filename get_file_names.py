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
            "items/demographics_session_id",
            "items/demographics_started_at",
            "items/demographics_completed_at",
            "items/demographics_duration",
            "items/demographics_completed_by",
            "items/city",
            "items/state_province",
            "items/zipcode",
            "items/country",
            "items/gender_identity",
            "items/other_gender_identity",
            "items/specify_gender_identity",
            "items/sexual_orientation",
            "items/other_sex_orientation",
            "items/race",
            "items/native_american_race",
            "items/asian_race",
            "items/black_race",
            "items/pacific_islander_race",
            "items/white_race",
            "items/canadian_race",
            "items/other_race_specify",
            "items/ethnicity",
            "items/hispanic_latino_selection",
            "items/edu_level",
            "items/other_edu_level",
            "items/hearing",
            "items/vision",
            "items/cognition",
            "items/mobility",
            "items/self_care",
            "items/independent_living",
            "items/employ_status",
            "items/other_employ_specify",
            "items/occupation",
            "items/veteran",
            "items/household_income_usa",
            "items/financial_assistance_usa",
            "items/assistance_programs_usa",
            "items/household_income_ca",
            "items/financial_assistance_ca",
            "items/assistance_programs_ca",
            "items/citizen",
            "items/marital_status",
            "items/housing_status",
            "items/household_count",
            "items/spouse_partner_sig_other",
            "items/children",
            "items/parent",
            "items/grandparent",
            "items/other_live_with",
            "items/others_household_specify",
            "items/transportation_yn",
            "items/primary_transportation",
            "items/other_transportation"
"""

# Extracting file names
file_names = extract_file_names(text)
for name in file_names:
    print(name)
