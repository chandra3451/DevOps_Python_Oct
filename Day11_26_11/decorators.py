# ----------------------------------------------------------
# FIRST-CLASS FUNCTIONS
# ----------------------------------------------------------
# Meaning: In Python, functions are treated like normal values.
# You can:
# 1. Store a function in a variable
# 2. Pass a function as an argument to another function
# 3. Return a function from another function
# 4. Store functions in lists, dicts, etc.
# This feature allows decorators to exist.
# ----------------------------------------------------------


# 1) Storing a function in a variable
def greet():
    print("Hello")

say = greet   # storing function in a variable
say()         # calling it using new name


# 2) Passing a function to another function
def call_me(fn):   # fn receives a function
    fn()           # calling the received function

call_me(greet)


# 3) Returning a function from another function
def outer():
    def inner():
        print("I am inner func")
    return inner      # Returning the inner function

func = outer()        # func now holds inner()
func()                # calling inner()


# 4) Storing functions inside a list
def a():
    print("A")

def b():
    print("B")

funcs = [a, b]  # list contains functions

funcs[0]()      # calling a()
funcs[1]()      # calling b()

for f in funcs:
    f()         # calling each function in list


# ----------------------------------------------------------
# DECORATORS
# ----------------------------------------------------------
# A decorator is simply a function that adds extra features
# to another function WITHOUT modifying the original function's code.
#
# Syntax:
# @decorator_name
# def target_function():
#     ...
# ----------------------------------------------------------


# Basic decorator example
def my_decorator(fun):
    def wrapper():
        print("Before func runs")  # Added feature
        fun()                      # Call original function
        print("After function runs") # Added feature
    return wrapper

@my_decorator   # Applying decorator
def say_hello():
    print("Hello")

say_hello()


# Decorator that accepts arguments in the wrapped function
def my_decorator(fun):
    def wrapper(a, b):
        print("Starting calculation...")
        res = fun(a, b)
        print("Calculation complete")
        return res
    return wrapper

@my_decorator
def add(x, y):
    return x + y

print(add(10, 5))


# ----------------------------------------------------------
# LOGGING
# ----------------------------------------------------------
# logging.basicConfig() sets up the logging system.
# It controls:
# 1. Log level (debug, info, warning, error, critical)
# 2. Log format
# 3. Where logs will appear (console or file)
#
# Logging is much better than print() in production scripts.
# ----------------------------------------------------------

import logging
logging.basicConfig(level=logging.INFO)

logging.info("Program started")
logging.warning("Low disk space")
logging.error("Something went wrong")


# Decorator that logs before and after running a function
def log_decorator(func):
    def wrapper(*args, **kwargs):
        logging.info(f"{func.__name__} started")   # before running
        res = func(*args, **kwargs)
        logging.info(f"{func.__name__} finished")  # after running
        return res
    return wrapper


@log_decorator
def greet(name):
    print(f"Hello {name}")

greet("Sam")


# ----------------------------------------------------------
# DECORATOR FOR PERMISSION CHECK (DevOps example)
# ----------------------------------------------------------
# This decorator checks if the user is admin.
# Useful in deployment scripts, where only specific users can trigger actions.
# ----------------------------------------------------------

def check_admin(func):
    def wrapper(user):
        if user != "admin":
            print("Access denied")
        else:
            func(user)
    return wrapper

@check_admin
def deploy(user_role):
    print(f"Deploying for {user_role}")

deploy("guest")   # Access denied
deploy("admin")   # Deployment allowed


# ----------------------------------------------------------
# FULL DEVOPS-STYLE EXAMPLE:
# Decorator that logs every step of a pipeline (CI/CD)
# ----------------------------------------------------------
# This decorator:
# - Logs when a step starts
# - Logs when a step ends
# - Logs errors if anything fails
# ----------------------------------------------------------

import logging
import time

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def log_step(func):
    """
    Decorator that logs:
    - Start of step
    - End of step
    - Any errors that occur
    """
    def wrapper():
        logging.info(f"START: {func.__name__}")   # before running the step
        try:
            res = func()
            logging.info(f"END: {func.__name__}") # after running successfully
            return res
        except Exception as e:
            logging.error(f"ERROR in {func.__name__}: {e}")  # log the error
            raise
    return wrapper


@log_step
def step1():
    time.sleep(3)
    print("Pulling code from Git")

@log_step
def step2():
    time.sleep(3)
    print("Building Docker image")

@log_step
def step3():
    time.sleep(3)
    print("Deploying the app to server")


# Running the pipeline steps
step1()
step2()
step3()
