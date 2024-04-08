import re
import pyaudio
import speech_recognition as sr

def calculate_molecular_mass(compound):
    elements_mass = {
        'H': 1.008, 'He': 4.0026, 'Li': 6.94, 'Be': 9.0122, 'B': 10.81, 'C': 12.011, 'N': 14.007,
        'O': 15.999, 'F': 18.998, 'Ne': 20.180, 'Na': 22.990, 'Mg': 24.305, 'Al': 26.982, 'Si': 28.085,
        'P': 30.974, 'S': 32.06, 'Cl': 35.45, 'Ar': 39.95, 'K': 39.098, 'Ca': 40.078, 'Sc': 44.956,
        'Ti': 47.867, 'V': 50.942, 'Cr': 51.996, 'Mn': 54.938, 'Fe': 55.845, 'Co': 58.933, 'Ni': 58.693,
        'Cu': 63.546, 'Zn': 65.38, 'Ga': 69.723, 'Ge': 72.63, 'As': 74.922, 'Se': 78.971, 'Br': 79.904,
        'Kr': 83.798, 'Rb': 85.468, 'Sr': 87.62, 'Y': 88.906, 'Zr': 91.224, 'Nb': 92.906, 'Mo': 95.95,
        'Tc': 98, 'Ru': 101.07, 'Rh': 102.91, 'Pd': 106.42, 'Ag': 107.87, 'Cd': 112.41, 'In': 114.82,
        'Sn': 118.71, 'Sb': 121.76, 'Te': 127.6, 'I': 126.9, 'Xe': 131.29, 'Cs': 132.91, 'Ba': 137.33,
        'La': 138.91, 'Ce': 140.12, 'Pr': 140.91, 'Nd': 144.24, 'Pm': 145, 'Sm': 150.36, 'Eu': 151.96,
        'Gd': 157.25, 'Tb': 158.93, 'Dy': 162.5, 'Ho': 164.93, 'Er': 167.26, 'Tm': 168.93, 'Yb': 173.05,
        'Lu': 174.97, 'Hf': 178.49, 'Ta': 180.95, 'W': 183.84, 'Re': 186.21, 'Os': 190.23, 'Ir': 192.22,
        'Pt': 195.08, 'Au': 196.97, 'Hg': 200.59, 'Tl': 204.38, 'Pb': 207.2, 'Bi': 208.98, 'Po': 209,
        'At': 210, 'Rn': 222, 'Fr': 223, 'Ra': 226, 'Ac': 227, 'Th': 232.04, 'Pa': 231.04, 'U': 238.03,
        'Np': 237, 'Pu': 244, 'Am': 243, 'Cm': 247, 'Bk': 247, 'Cf': 251, 'Es': 252, 'Fm': 257,
        'Md': 258, 'No': 259, 'Lr': 262, 'Rf': 267, 'Db': 270, 'Sg': 271, 'Bh': 270, 'Hs': 270,
        'Mt': 276, 'Ds': 281, 'Rg': 282, 'Cn': 285, 'Nh': 286, 'Fl': 289, 'Mc': 289, 'Lv': 293,
        'Ts': 294, 'Og': 294,
    }
    compound_regex = r'([A-Z][a-z]?)(\d*)'
    elements = re.findall(compound_regex, compound)

    molecular_mass = 0
    for element, quantity in elements:
        if quantity == '':
            quantity = 1
        molecular_mass += elements_mass[element] * int(quantity)
    
    return molecular_mass

def recog():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say Something")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    
    try:
        print("Recognizing..")
        text = r.recognize_google(audio, language='en-in')  # Specify Language Code
        text = text.upper().replace(" ", "")  # Remove spaces from the recognized text
        return text
    except Exception as e:
        print(e)
        return "Sorry"

data_type = input("How do you want to use the robot? Audio (a) or written (t)?")
if data_type == "t":
    compound = input("Enter a chemical compound: ")
    print(f"Molecular mass of {compound}: {calculate_molecular_mass(compound):.2f}")
elif data_type == "a":
    compound = recog()
    if compound != "Sorry":
        print(f"Molecular mass of {compound}: {calculate_molecular_mass(compound):.2f}")
    else:
        print("Sorry, could not understand. Please try again.")
else:
    print("Please enter the correct option!")