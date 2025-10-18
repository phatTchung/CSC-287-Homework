import os
import json
import sys
import shutil
from datetime import datetime

# simple replacements
replacements = {
    "enabled": {"status": "enabled", "since": "2024-10-01"},
    "disabled": {"status": "disabled", "since": "2024-10-01"},
    "manage_users": {"permission": "manage_users", "granted_at": "2024-10-05", "level": "full"},
    "view_content": {"permission": "view_content", "granted_at": "2024-09-25", "level": "read-only"}
}

def change_value(data):
    """
    Go through the JSON data and make changes.
    - If the value is a dictionary or list, check all items inside.
    - If it is a string, replace '@company.com' with '@newcompany.com'.
    - Also replace special words like 'enabled', 'disabled', etc. using the replacements map.
    """
    if isinstance(data, dict):
        new_data = {}
        for key, value in data.items():
            new_data[key] = change_value(value)
        return new_data
    elif isinstance(data, list):
        return [change_value(item) for item in data]
    elif isinstance(data, str):
        # replace @company.com
        if "@company.com" in data:
            data = data.replace("@company.com", "@newcompany.com")
        # replace special values
        if data in replacements:
            return replacements[data]
        return data
    else:
        return data

def main():
    """
    Main function of the program.
    1. Get the folder name from the command line.
    2. Create a new folder with the current date and time.
    3. Go through all files inside the given folder.
    4. Read and update each JSON file.
    5. Save the new files in the new folder.
    6. If a file cannot be read, copy it as it is.
    """
    if len(sys.argv) < 2:
        print("Usage: python batch_update_profiles.py user_profiles")
        return

    input_folder = sys.argv[1]
    if not os.path.exists(input_folder):
        print("Folder not found:", input_folder)
        return

    # make new output folder with time
    time_now = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_folder = f"user_profiles_updated_{time_now}"
    os.makedirs(output_folder, exist_ok=True)

    # walk through folders
    for root, dirs, files in os.walk(input_folder):
        rel_path = os.path.relpath(root, input_folder)
        save_folder = os.path.join(output_folder, rel_path)
        os.makedirs(save_folder, exist_ok=True)

        for file in files:
            if file.endswith(".json"):
                src = os.path.join(root, file)
                dst = os.path.join(save_folder, file)
                try:
                    with open(src, "r") as f:
                        data = json.load(f)
                    new_data = change_value(data)
                    with open(dst, "w") as f:
                        json.dump(new_data, f, indent=4)
                except Exception as e:
                    print("Error reading:", src)
                    shutil.copy(src, dst)

    print("All files updated! Saved to:", output_folder)

if __name__ == "__main__":
    """
    This runs the main() function when the file is executed.
    """
    main()
