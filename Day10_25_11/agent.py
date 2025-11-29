# =============================================================
#                          OOPs – Agent Example
# =============================================================
# This example explains:
# ✔ __init__ (constructor)
# ✔ self (object reference)
# ✔ instance attributes (name, age, health, alive)
# ✔ methods that modify object state (punched, shot)
# ✔ checking object status (is_alive)
# ✔ returning formatted info
# ✔ inheritance with Boss class
# =============================================================


# -------------------------
# CLASS: Agent
# -------------------------
# Represents a player/character in a game.
# Every agent has:
# - name
# - age
# - health (default 100)
# - alive status (default True)

class Agent:
    
    def __init__(self, name, age):
        """
        __init__ is the constructor.
        It runs automatically whenever an object is created.

        self → refers to the current object (p1, p2 …)
        """
        print("Welcome to the game")
        self.name = name          # instance attribute
        self.age = age            # instance attribute
        self.health = 100         # default health
        self.alive = True         # default alive status
        
        
    # Method: punched
    # Reduces health by 10
    def punched(self):
        self.health -= 10
    
    
    # Method: shot
    # Reduces health by 25
    def shot(self):
        self.health -= 25
        
        
    # Method: is_alive
    # Checks whether health > 0
    # Updates the 'alive' property and returns True/False
    def is_alive(self):
        self.alive = (self.health > 0)
        return self.alive
    
    
    # Method: info
    # Returns a formatted string containing the agent’s details
    def info(self):
        return f"{self.name}: {self.age}, health = {self.health}"


# ----------------------------------------------------
# Example Usage
# ----------------------------------------------------
# p1 = Agent("sam", 25)       # Creates an Agent object
# print(p1.info())             # Shows initial details
# p1.punched()                 # health -= 10
# p1.shot()                    # health -= 25
# p1.shot()
# p1.shot()
# p1.shot()
# print(p1.info())             # Final health after attacks
# print(p1.is_alive())         # Check if still alive


# p2 = Agent("Ravi", 30)       # Another agent


# =============================================================
#                         INHERITANCE
# =============================================================
# Boss class inherits all properties & methods from Agent.
# Boss has everything an Agent has (name, age, health, punched…)
# PLUS extra capabilities (e.g., blow_fire)

class Boss(Agent):
    
    def blow_fire(self):
        print("uses Blow Fire!")


# Example:
# b1 = Boss("Boss1", 24)
# print(b1.info())    # Can use parent class method
# b1.blow_fire()      # Boss-specific method
