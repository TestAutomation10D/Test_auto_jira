import os

# Set a value in os.environ
os.environ['MY_VARIABLE'] = 'Hello, GitHub Actions!'

# Print the value
print(f"MY_VARIABLE set to: {os.environ['MY_VARIABLE']}")
