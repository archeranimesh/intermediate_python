import os

current_folder = os.getcwd()
print(f"I am in this folder: {current_folder}")

# with keyword is used for context management, so the clean-up can happen as soon as we exit.
with os.scandir(current_folder) as folder:
    print(type(folder))
    for entry in folder:
        print(f"->{entry.name}")