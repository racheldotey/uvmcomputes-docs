from itertools import chain
import random

class SolarSystem:
    planets = [list (chain (planet, (index + 1,))) for index, planet in enumerate ((
        ('Mercury', 'hot', 2240),
        ('Venus', 'sulphurous', 6052),
        ('Earth', 'fertile', 6378),
        ('Mars', 'reddish', 3397),
        ('Jupiter', 'stormy', 71492),
        ('Saturn', 'ringed', 60268),
        ('Uranus', 'cold', 25559),
        ('Neptune', 'very cold', 24766) 
    ))]
    
    lines = (
        '{} is a {} planet',
        'The radius of {} is {} km',
        '{} is planet nr. {} counting from the sun'
    )
    
    def __init__ (self):
        self.planet = self.planets[random.randint(0, len(self.planets)-1)]
        self.lineIndex = random.randint(0, len(self.lines)-1)

    def greet (self):
        greeting = 'Hello from {}!'.format(self.planet[0])
        return greeting
        
    def explain (self):
        response = self.lines[self.lineIndex].format(self.planet[0], self.planet[self.lineIndex + 1])
        self.lineIndex = (self.lineIndex + 1) % 3
        return response
        
def runSolarSystem():
    response = []

    solarSystem = SolarSystem()
    response.append(solarSystem.greet())
    response.append(solarSystem.explain())
    response.append(solarSystem.explain())
    response.append(solarSystem.explain())
    
    return response

runSolarSystem()