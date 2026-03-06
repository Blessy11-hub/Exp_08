import os

# Task 2: Get parameter values from environment variables
# Jenkins automatically sets these if we call them in the shell
app_name = os.getenv('APP_NAME', 'Default_App')
version = os.getenv('VERSION', '1.0')

# Task 2: Display values in the console
print("--- Jenkins Parameter Execution ---")
print(f"Project: {app_name}")
print(f"Version: {version}")

# Task 3: Store the values inside parameters.txt
try:
    with open("parameters.txt", "w") as f:
        f.write(f"APP_NAME={app_name}\n")
        f.write(f"VERSION={version}\n")
    print("Success: parameters.txt has been created.")
except Exception as e:
    print(f"Error writing file: {e}")