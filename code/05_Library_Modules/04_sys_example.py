import sys

# argv gives the command line arguments passed.
# argv is never empty, 0th index always contains the file name.
# The arguments passed, even though will be int, it is converted to strings.
arguments = sys.argv
print(f"The arguments passed are {arguments}")

# sys.platform gives the platform we are running the script.
print(f"We are currently running on {sys.platform} machine")

# python -m pip search <package_name>, searches for the package in pypi.org