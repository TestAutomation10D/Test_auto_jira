import os

# Set a value in os.environ
os.environ['MY_VARIABLE'] = 'Hello, GitHub Actions!'

# Print the value
print(f"MY_VARIABLE set to: {os.environ['MY_VARIABLE']}")

env_file = os.getenv('GITHUB_ENV')
if env_file:
    with open(env_file, "a") as myfile:
        myfile.write("MY_VARIABLE=1\n")
