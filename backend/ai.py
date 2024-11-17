# Dictionary legend: { Planet : [temp (F), radius (mi), volume (billion mi^3), # of moons ]}
d = {
    'Mercury': [333, 1516, 14.6, 0], 
    'Venus': [867, 3760, 222.9, 0],
    'Mars': [-85, 2106, 39.2, 2], 
    'Earth': [59, 3959, 259.9, 1],
    'Jupiter': [-166, 43441, 343345, 95],
    'Saturn': [-220, 36184, 263846, 146], 
    'Uranus': [-320, 15759, 65394, 28], 
    'Neptune': [-330, 15299, 57754, 16]
}

def akinator_planet_style():
    remaining_planets = list(d.keys())
    
    question = f'Is the mean temperature of the planet more than 0 degrees Fahrenheit?'
    print(question)
    response = input('(yes/no): ').strip().lower()
    if response == 'yes':
        remaining_planets.remove('Mars')
        remaining_planets.remove('Jupiter')
        remaining_planets.remove('Saturn')
        remaining_planets.remove('Uranus')
        remaining_planets.remove('Neptune')
        print(remaining_planets)
        
        question2 = f'Is the mean volume of the planet more than 100 billion cubic miles?'
        print(question2)
        response = input('(yes/no): ').strip().lower()
        if response == 'yes': 
            remaining_planets.remove('Mercury')
            
            question3 = f'Is the number of moons the planet has 0?'
            print(question3)
            response = input('(yes/no): ').strip().lower()
            if response == 'yes': 
                remaining_planets.remove('Earth')
                return remaining_planets
            elif response == 'no':
                remaining_planets.remove('Venus')
                return remaining_planets
        
        elif response == 'no': 
            remaining_planets.remove('Earth')
            remaining_planets.remove('Venus')
            return remaining_planets

    elif response == 'no': 
        remaining_planets.remove('Earth')
        remaining_planets.remove('Mercury')
        remaining_planets.remove('Venus')
        print(remaining_planets)
        
        question2 = f'Is the mean radius of the planet more than 20,000 miles?'
        print(question2)
        response = input('(yes/no): ').strip().lower()
        if response == 'yes': 
            remaining_planets.remove('Mars')
            remaining_planets.remove('Uranus')
            remaining_planets.remove('Neptune')
            
            question3 = f'Is the number of moons the planet has more than 100?'
            print(question3)
            response = input('(yes/no): ').strip().lower()
            if response == 'yes': 
                remaining_planets.remove('Jupiter')
                return remaining_planets
            elif response == 'no': 
                remaining_planets.remove('Saturn')
                return remaining_planets
        
        elif response == 'no': 
            remaining_planets.remove('Jupiter')
            remaining_planets.remove('Saturn')
            
            question3 = f'Is the mean volume of the planet more than 50 billion cubic miles?'
            print(question3)
            response = input('(yes/no): ').strip().lower()
            if response == 'yes': 
                remaining_planets.remove('Mars')
                
                question4 = f'Is the number of moons more than 20?'
                print(question4)
                response = input('(yes/no): ').strip().lower()
                if response == 'yes': 
                    remaining_planets.remove('Neptune')
                    return remaining_planets
                elif response == 'no':
                    remaining_planets.remove('Uranus')
                    return remaining_planets
            
            elif response == 'no':
                remaining_planets.remove('Neptune')
                remaining_planets.remove('Uranus')
                return remaining_planets

akinator_planet_style()
