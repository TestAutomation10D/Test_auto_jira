import os

# Set environment variable using os.system
os.system('echo "MY_VARIABLE=Hello, GitHub Actions!" >> $GITHUB_ENV')

# Print the value
print(f"MY_VARIABLE set to: {os.getenv('MY_VARIABLE')}")
