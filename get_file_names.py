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
"b2ai_redcap2rs_activities:q_generic_demographics/items/housing_status",
"b2ai_redcap2rs_activities:q_generic_demographics/items/household_count",
"activities/optional/items/household_composition",
"b2ai_redcap2rs_activities:q_generic_demographics/items/others_household_specify",
"activities/completed_by/completed_by_schema",
"activities/required/activities/address/items/city",
"b2ai_redcap2rs_activities:q_generic_demographics/items/state_province",
"b2ai_redcap2rs_activities:q_generic_demographics/items/zipcode",
"b2ai_redcap2rs_activities:q_generic_demographics/items/country",
"""

# Extracting file names
file_names = extract_file_names(text)
for name in file_names:
    print(name)
