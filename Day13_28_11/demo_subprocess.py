import subprocess

# -------------------------------------------
# BASIC COMMAND EXECUTION
# -------------------------------------------

# Example 1: Run a simple command using the Windows shell.
# `shell=True` is required because commands like echo/dir are CMD built-ins.
# subprocess.run("echo hello", shell=True)

# Linux/Mac version of the same command:
# subprocess.run(["echo", "Hello"])   # Does NOT require shell=True on Linux

# Example 2: Run Windows directory commands
# subprocess.run("dir", shell=True)  # Lists files in current directory

# Example 3: Create a folder
# subprocess.run("mkdir test_folder", shell=True)

# Example 4: Print a message
# subprocess.run("echo Done!", shell=True)


# -------------------------------------------
# CAPTURING OUTPUT (VERY IMPORTANT)
# -------------------------------------------

# Example 5: Capture STDOUT instead of printing directly to terminal
# This allows us to *use* the output inside Python.
# result = subprocess.run("echo hello", capture_output=True, text=True, shell=True)
# print("Output:", result.stdout)


# -------------------------------------------
# CAPTURING ERRORS (STDERR)
# -------------------------------------------

# Example 6: Run an invalid command to see error capture
# result = subprocess.run(["abc"], capture_output=True, text=True, shell=True)
# print("Output:", result.stdout)      # Usually empty
# print("Output Err:", result.stderr)  # Shows the error message


# -------------------------------------------
# RETURN CODE (SUCCESS OR FAILURE)
# -------------------------------------------
# 0 = success
# Non-zero = error

# res = subprocess.run("ping google.com", shell=True)
# print("Result code:", res.returncode)   # Likely 0

# res = subprocess.run("ping google123425vfv.com", shell=True)
# print("Result code:", res.returncode)   # Non-zero (error)


# -------------------------------------------
# RUNNING MULTIPLE COMMANDS (&&)
# -------------------------------------------

# `&&` means:
# Run the next command ONLY if previous succeeded.

# subprocess.run("echo Hello && echo world", shell=True)


# -------------------------------------------
# FULL REALISTIC EXAMPLE
# -------------------------------------------
# A complete workflow:
# 1. Print a message
# 2. Create a folder
# 3. Change directory into that folder
# 4. Create a file inside
# 5. List all items inside the folder
#
# IMPORTANT (WINDOWS):
# - Must be in ONE LINE
# - Multi-line triple quotes break CMD syntax
# - Always use shell=True for chained commands

cmd = (
    "echo starting process.... && "
    "mkdir mydata && "
    "cd mydata && "
    "echo This is inside folder > info.txt && "
    "dir"
)

subprocess.run(cmd, shell=True)
