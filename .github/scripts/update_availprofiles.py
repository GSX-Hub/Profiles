import os
import json
import logging
from copy import deepcopy

avail_profiles_path = "AvailProfiles.json"
airports_dir = "Airports"

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def get_actual_files(profile_path):
    """Get list of .ini and .py files in the profile directory"""
    actual_files = []
    if os.path.exists(profile_path):
        for file_name in os.listdir(profile_path):
            if file_name.endswith(".ini") or file_name.endswith(".py"):
                actual_files.append(file_name)
    return sorted(actual_files)  # Sort for consistent ordering


def profiles_are_equal(profile1, profile2):
    """Compare two profiles to see if they have the same content"""
    # Compare all fields except FileNames first
    fields_to_compare = ["ProfileICAO", "Scenery", "Creator", "Version"]
    for field in fields_to_compare:
        if profile1.get(field) != profile2.get(field):
            return False

    # Compare FileNames (order doesn't matter)
    files1 = sorted(profile1.get("FileNames", []))
    files2 = sorted(profile2.get("FileNames", []))
    return files1 == files2


def get_airports():
    # Load existing data
    if os.path.exists(avail_profiles_path):
        with open(avail_profiles_path, "r") as f:
            data = json.load(f)
        logging.info(f"Loaded {len(data)} existing profiles from AvailProfiles.json")
    else:
        data = []
        logging.info("AvailProfiles.json not found, starting with empty list")

    # Create a mapping of existing profiles by folder name for quick lookup
    existing_profiles = {profile["Folder"]: profile for profile in data}

    # Track which profiles we've seen (to remove obsolete ones later)
    found_profiles = set()

    # Track if any changes were made
    changes_made = False

    # Process each airport directory
    logging.info(f"Scanning {airports_dir} for airport profiles...")
    for root, dirs, files in os.walk(airports_dir):
        for dir_name in dirs:
            profile_path = os.path.join(root, dir_name)
            profile_json_path = os.path.join(profile_path, "profile.json")

            # Skip if no profile.json exists
            if not os.path.exists(profile_json_path):
                logging.warning(f"No profile.json found in {profile_path}, skipping")
                continue

            logging.info(f"Processing {dir_name}")
            found_profiles.add(dir_name)

            try:
                # Read profile.json
                with open(profile_json_path, "r") as profile_file:
                    profile_data = json.load(profile_file)

                # Get actual files in directory
                actual_files = get_actual_files(profile_path)

                # Create new profile data
                new_profile = {
                    "Folder": dir_name,
                    "ProfileICAO": profile_data["ProfileICAO"],
                    "Scenery": profile_data["Scenery"],
                    "Creator": profile_data["Creator"],
                    "Version": str(profile_data["Version"]),
                    "FileNames": actual_files,
                }

                # Check if this profile exists and compare
                if dir_name in existing_profiles:
                    existing_profile = existing_profiles[dir_name]
                    if not profiles_are_equal(existing_profile, new_profile):
                        # Log what changed
                        changes = []
                        for field in ["ProfileICAO", "Scenery", "Creator", "Version"]:
                            if existing_profile.get(field) != new_profile.get(field):
                                changes.append(
                                    f"{field}: '{existing_profile.get(field)}' -> '{new_profile.get(field)}'"
                                )

                        old_files = sorted(existing_profile.get("FileNames", []))
                        new_files = sorted(new_profile.get("FileNames", []))
                        if old_files != new_files:
                            changes.append(f"FileNames: {old_files} -> {new_files}")

                        logging.info(
                            f"Updating existing profile for {dir_name}: {'; '.join(changes)}"
                        )
                        # Update the existing profile in place to preserve position
                        for i, profile in enumerate(data):
                            if profile["Folder"] == dir_name:
                                data[i] = new_profile
                                changes_made = True
                                break
                    else:
                        logging.info(f"No changes needed for {dir_name}")
                else:
                    logging.info(f"Adding new profile for {dir_name}")
                    data.append(new_profile)
                    changes_made = True

            except (json.JSONDecodeError, KeyError) as e:
                logging.error(f"Error processing {profile_json_path}: {e}")
                continue

    # Remove profiles that no longer exist in the filesystem
    original_length = len(data)
    data = [profile for profile in data if profile["Folder"] in found_profiles]
    if len(data) != original_length:
        logging.info(f"Removed {original_length - len(data)} obsolete profiles")
        changes_made = True

    # Only write the file if changes were made
    if changes_made:
        logging.info("Writing updated AvailProfiles.json")
        with open(avail_profiles_path, "w") as f:
            json.dump(data, f, indent=4)
    else:
        logging.info("No changes needed, file not modified")


get_airports()
