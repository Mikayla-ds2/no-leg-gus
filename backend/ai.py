from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Dictionary legend: { Planet : [temp (F), radius (mi), volume (billion mi^3), # of moons ]}
d = {
    'Mercury' : [333, 1516, 14.6, 0], 
    'Venus' : [867, 3760, 222.9, 0],
    'Mars' : [-85, 2106, 39.2, 2], 
    'Earth' : [59, 3959, 259.9, 1],
    'Jupiter' : [-166, 43441, 343345, 95],
    'Saturn' : [-220, 36184, 263846, 146], 
    'Uranus' : [-320, 15759, 65394, 28], 
    'Neptune' : [-330, 15299, 57754, 16]
}

remaining_planets = list(d.keys())
question = f'Is the mean temperature of the planet more than 0 degrees Fahrenheit?'
print(question)
response = input('(yes/no): ').strip.lower()
if response == 'yes':
    remaining_planets.remove('Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune')
    print(remaining_planets)
    question2 = f'Is the mean radius of the planet more than 10,000 miles?'
    print(question2)
    if response == 'yes':
        
        
elif response == 'no': 
    remaining_planets.remove('Earth', 'Mercury', 'Venus')
    print(remaining_planets)

        
    
    
    
    
    
'''
    if characteristic == 'temp':
        question = f'Is the mean temperature of the planet {>} {0} degrees Fahrenheit?'
    elif characteristic == 'radius':
        question = f'Is the mean radius of the planet {>} {10,000} miles?'
    elif characteristic == 'volume':
        question = f'Is the mean volume of the planet {>} {50,000} billion cubic miles?'
    elif characteristic == 'number of moons': 
        question = f'Is the number of moons the planet has {<} {10}?'
    print(question)
    response = input('yes/no): ').strip.lower()
    return response == 'yes'
def filter_planets(remaining_planets, characteristic, comparison, value): 
    new_planets = []
    for planet in remaining_planets: 
        if comparison == ">":
            if d[planet][characteristic_index(characteristic)] > value:
                new_planets.append(planet)
    return new_planets
while len(remaining_planets) > 1: 
    if ask_questions(remaining_planets, "radius", ">", )
'''   



'''
Is the mean temperature of the planet more than or less than 0 degrees Fahrenheit?
Is the mean radius of the planet more than or less than 10,000 miles?
Is the mean volume of the planet more than or less than 50,000 billion cubic miles?
Is the number of moons the planet has more than or less than 10?
'''