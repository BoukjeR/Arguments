# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

def greet(name:str, greeting_template:str='Hello, <name>!'):
    g = greeting_template.replace('<name>', name)
    return(g)
           
print(greet('Bob'))

def force(mass:float, body:str='earth'):
    if body == 'sun': gravity = 274
    if body == 'jupiter': gravity = 24.9
    if body == 'neptune': gravity = 11.2
    if body == 'saturn': gravity = 10.4
    if body == 'earth': gravity = 9.8
    if body == 'uranus': gravity = 8.9
    if body == 'venus': gravity = 8.9
    if body == 'mars': gravity = 3.7
    if body == 'mercury': gravity = 3.7
    if body == 'moon': gravity = 1.6
    if body == 'pluto': gravity = 0.6
    return(mass * gravity)

print(force(1.1, 'pluto')) 

def pull(m1:float, m2:float, d:float):
    return((6.674*(10**-11))*((m1*m2)/(d*d)))

print(pull(0.1, 5.972*10**24, 6.371*10**6)) #an apple and the earth: 0.98 N