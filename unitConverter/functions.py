prefixes = ['quetta', 'ronna', 'yotta', 'zetta', 'exa', 'peta', 'tera', 'giga', 'mega', 'kilo', '', 'milli', 'micro', 'nano', 'pico', 'femto', ' atto', 'zepto', 'yocto', 'ronto', 'quecto']
prefixed_ = ['hecto', ' deca', '', 'deci', 'centi']

# x = y saniye
time = {('attosecond', 'as', 1e-18), ('femtosecond', 'fs', 1e-15), ('picosecond', 'ps', 1e-12), ('nanosecond', 'ns', 1e-9), ('microsecond', 'µs', 1e-6), ('millisecond', 'ms', 0.001), ('second', 's', 1), ('minute', 'min', 60), ('hour', 'h', 3600), ('day', 'd', 86400), ('week', 'wk', 604800), ('month', 'mo', 2628000), ('year', 'a', 31557600), ('decade', 'dec', 315576000), ('century', 'c', 315576e+4), ('millennium', 'millennium', 315576e+5)}
length = {('attometer', 'am', 1e-18), ('femtometer', 'fm', 1e-15), ('picometer', 'pm', 1e-12), ('nanometer', 'nm', 1e-9), ('micrometer', 'µm', 1e-6),  ('micron', 'µ', 1e-6), ('millimeter', 'mm', 0.001), ('centimeter', 'cm', 0.01), ('decimeter', 'dm', 0.1), ('meter', 'm', 1), ('dekameter', 'dam', 10), ('hectometer', 'hm', 100), ('megameter', 'Mm', 1e+6), ('gigameter', 'Gm', 1e+9), ('terameter', 'Tm', 1e+12), ('pentameter', 'Pm', 1e+15), ('exameter', 'Em', 1e+18), ('light year', 'ly', 9460730472580000), ('mile', 'mi', 1609.344), ('yard', 'yd', 0.9144), ('foot', 'ft', 0.3048), ('inch', 'in', 0.0254)}

measurements = {
    "time": time,
    "length": length,
    "mass": "kilogramm",
    "electric current": "amper",
}

def convert_unit(type, in_unit, out_unit, in_amount=None, out_amount=None, r=4):
    units = measurements[type]
    
    in_factor = None
    out_factor = None

    for unit in units:
        if in_factor == None and in_unit == unit[0]:
            in_factor = unit[2]
        elif out_factor == None and out_unit == unit[0]:
            out_factor = unit[2]
        if in_factor != None and out_factor != None:
            break
    
    _ = round(out_factor / in_factor, r)

    out = None

    if in_amount != None:
        out = in_amount / _
    
    elif out_amount != None:
        out = out_amount * _
    
    elif in_amount == None and out_amount == None:
        out = _

    return out

### UI de üstte tablar olacak dve ordan neyi cevirecegimizi secicez
### UI de girdi ve ya cikti textinputuna bir sey yazinca diger taraftaki silincek
    



"""
ana einheit, einheitlar, sembolleri, einheiten ana einheite cevrimi
Basic:
Time
Length
Mass
Electric Current
Thermodynamic Temperature
Amount of Substance

Common:
Length
Volume + 
Area + 
Energy +
Force + 
Speed + 
Fuel Consumption
Data Storage + 
Currency +
Weight and Mass 
Temperature + 
Pressure +
Power +
Time +
Angle +
Numbers +
Volume - Dry +

Engineering:
Volume
Area
Energy
Force
Speed
Fuel
Consumption
Data Storage
Currency
Acceleration
Density
Moment of Inertia
Torque
Temperature
Pressure
Power
Time
Angle
Numbers
Volume - Dry
Velocity - Angular
Specific Volume
Moment of Force

Heat:
Fuel Efficiency - Mass
Temperature Interval
Thermal Resistance
Specific Heat Capacity
Heat Flux Density
Fuel Efficency - Volume
Thermal Expansion
Thermal Conductivity
Heat Density
Heat Transder Coefficient

Fluids:
Flow
Flow - Molar
Concentration - Molar
Viscosity - Dynamic
Surface Tension
Flow - Mass
Mass Flux Density
Concentration - Solution
Viscosity - Kinematic
Permeability

Light:
Luminance
Illumination
Frequency Wavelength
Luminous Intensity
Digital Image Resolution

Electricity:
Charge
Surfe Charge Density
Current
Surface Current Density
Electric Potential
Electric Resistivity
Electric Conductivity
Inductance
Linear Charge Density
Volume Charge Density
Linear Current Density
Electric Field Strength
Electric Resistance
Electric Conductance
Electrostatic Capacitance

Magnetism:
Magnetomotive Force
Magnetic Flux
Magnetic Field Strength
Magnetic Flux Density

Radiology:
Radiation
Radiation-Exposure
Radiation-Activity
Radiation-Absorved Dose


"""




