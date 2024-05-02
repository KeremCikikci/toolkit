from functions import *

### Convert ###
# convert_unit('time', 'attosecond', 'femtosecond')



"""
##### International Sytem of Units (SI) --> Metric System #####

### BASIC UNITS ###
Name	Symbol	Measure	Post-2019 formal definition[1]	Historical origin / justification	Dimension symbol
- second	s	time	"The second, symbol s, is the SI unit of time. It is defined by taking the fixed numerical value of the caesium frequency, ∆νCs, the unperturbed ground-state hyperfine transition frequency of the caesium 133 atom, to be 9192631770 when expressed in the unit Hz, which is equal to s−1."[1]	The day is divided into 24 hours, each hour divided into 60 minutes, each minute divided into 60 seconds.
A second is 1 / (24 × 60 × 60) of the day. Historically, a day was defined as the mean solar day; i.e., the average time between two successive occurrences of local apparent solar noon.	T
- metre	m	length	"The metre, symbol m, is the SI unit of length. It is defined by taking the fixed numerical value of the speed of light in vacuum c to be 299792458 when expressed in the unit m s−1, where the second is defined in terms of ∆νCs."[1]	1 / 10000000 of the distance from the Earth's equator to the North Pole measured on the meridian arc through Paris.	L
- kilogram	kg	mass	"The kilogram, symbol kg, is the SI unit of mass. It is defined by taking the fixed numerical value of the Planck constant h to be 6.62607015×10−34 when expressed in the unit J s, which is equal to kg m2 s−1, where the metre and the second are defined in terms of c and ∆νCs."[1]	The mass of one litre of water at the temperature of melting ice. A litre is one thousandth of a cubic metre.	M
- ampere	A	electric current	"The ampere, symbol A, is the SI unit of electric current. It is defined by taking the fixed numerical value of the elementary charge e to be 1.602176634×10−19 when expressed in the unit C, which is equal to A s, where the second is defined in terms of ∆νCs."[1]	The original "International Ampere" was defined electrochemically as the current required to deposit 1.118 milligrams of silver per second from a solution of silver nitrate.	I
- kelvin	K	thermodynamic temperature	"The kelvin, symbol K, is the SI unit of thermodynamic temperature. It is defined by taking the fixed numerical value of the Boltzmann constant k to be 1.380649×10−23 when expressed in the unit J K−1, which is equal to kg m2 s−2 K−1, where the kilogram, metre and second are defined in terms of h, c and ∆νCs."[1]	The Celsius scale: the Kelvin scale uses the degree Celsius for its unit increment, but is a thermodynamic scale (0 K is absolute zero).	Θ
- mole	mol	amount of substance	"The mole, symbol mol, is the SI unit of amount of substance. One mole contains exactly 6.022 140 76 × 1023 elementary entities. This number is the fixed numerical value of the Avogadro constant, NA, when expressed in the unit mol−1 and is called the Avogadro number.
The amount of substance, symbol n, of a system is a measure of the number of specified elementary entities. An elementary entity may be an atom, a molecule, an ion, an electron, any other particle or specified group of particles."[1]

Atomic weight or molecular weight divided by the molar mass constant, 1 g/mol.	N
- candela	cd	luminous intensity	"The candela, symbol cd, is the SI unit of luminous intensity in a given direction. It is defined by taking the fixed numerical value of the luminous efficacy of monochromatic radiation of frequency 540×1012 Hz, Kcd, to be 683 when expressed in the unit lm W−1, which is equal to cd sr W−1, or cd sr kg−1 m−2 s3, where the kilogram, metre and second are defined in terms of h, c and ∆νCs."[1]	The candlepower, which is based on the light emitted from a burning candle of standard properties.	J

### DERIVED UNITS ###
hertz	Hz	frequency	1/s	s−1
radian	rad	angle	m/m	1
steradian	sr	solid angle	m2/m2	1
newton	N	force, weight	kg⋅m/s2	kg⋅m⋅s−2
pascal	Pa	pressure, stress	N/m2	kg⋅m−1⋅s−2
joule	J	energy, work, heat	m⋅N, C⋅V, W⋅s	kg⋅m2⋅s−2
watt	W	power, radiant flux	J/s, V⋅A	kg⋅m2⋅s−3
coulomb	C	electric charge or quantity of electricity	s⋅A, F⋅V	s⋅A
volt	V	voltage, electrical potential difference, electromotive force	W/A, J/C	kg⋅m2⋅s−3⋅A−1
farad	F	electrical capacitance	C/V, s/Ω	kg−1⋅m−2⋅s4⋅A2
ohm	Ω	electrical resistance, impedance, reactance	1/S, V/A	kg⋅m2⋅s−3⋅A−2
siemens	S	electrical conductance	1/Ω, A/V	kg−1⋅m−2⋅s3⋅A2
weber	Wb	magnetic flux	J/A, T⋅m2,V⋅s	kg⋅m2⋅s−2⋅A−1
tesla	T	magnetic induction, magnetic flux density	V⋅s/m2, Wb/m2, N/(A⋅m)	kg⋅s−2⋅A−1
henry	H	electrical inductance	V⋅s/A, Ω⋅s, Wb/A	kg⋅m2⋅s−2⋅A−2
degree Celsius	°C	temperature relative to 273.15 K	K	K
lumen	lm	luminous flux	cd⋅sr	cd
lux	lx	illuminance	lm/m2	cd⋅m−2
becquerel	Bq	radioactivity (decays per unit time)	1/s	s−1
gray	Gy	absorbed dose (of ionizing radiation)	J/kg	m2⋅s−2
sievert	Sv	equivalent dose (of ionizing radiation)	J/kg	m2⋅s−2
katal	kat	catalytic activity	mol/s	s−1⋅mol.


pressure
force
density
weight
conductivity
heat
volume
mass
time
magnetic field
surface tension
capacitance
resistance
electricity
momentum
speed
humidity
voltage
electric charge
light
radioactivity
energy
power
work
temperature
current
torque
length
velocity
viscosity
magnetic flux
acceleration
inductance
sound
frequency
moment of inertia
distance
vibration
displacement
wavelength
electic field
electric flux
angle
"""



















##### Imperial System --> British System #####
"""
Table of length equivalent units
Unit	Abbr. or symbols	Relative to previous	Feet	Metres	Notes
twip			1⁄17280	0.0000176389	typographic measure
thou	th	1.44 twip	1⁄12000	0.0000254	
Abbreviation of "thousandth of an inch". Also known as mil.[14]

barleycorn		333+1⁄3 th	1⁄36	0.0084667	1⁄3 in
inch	in″	3 Bc	1⁄12	0.0254	1 metre ≈ 39.3701 in
hand	hh	4 in	1⁄3	0.1016	Still used in some English-speaking (i.e. US and Commonwealth) nations to measure heights of horses.
foot	ft′	3 h	1	0.3048	12 in
yard	yd	3 ft	3	0.9144	Defined as exactly 0.9144 m by the international yard and pound agreement of 1959
chain	ch	22 yd	66	20.1168	100 links, 4 rods, or 1⁄10 of a furlong. The distance between the two wickets on a cricket pitch.
furlong	fur	10 chains	660	201.168	220 yd
mile	mi	8 furlongs	5280	1609.344	1760 yd or 80 chains
league	lea	3 mi	15840	4828.032	No longer an official unit in any nation.[citation needed]
Maritime units
fathom	ftm	2.02667 yd	6.0761	1.852	The British Admiralty in practice used a fathom of 6 ft. This was despite its being 1⁄1000 of a nautical mile (i.e. 6.08 ft) until the adoption of the international nautical mile.[15]
cable		100 fathoms	607.61	185.2	One tenth of a nautical mile. Equal to 100 fathoms under the strict definition.
nautical mile	nmi	10 cables	6076.1	1852	Used for measuring distances at sea (and also in aviation) and approximately equal to one arc minute of a great circle. Until the adoption of the international definition of 1852 m in 1970, the British nautical (Admiralty) mile was defined as 6080 ft.[16]
Gunter's survey units (17th century onwards)
link		7.92 in	66⁄100	0.201168	1⁄100 of a chain and 1⁄1000 of a furlong
rod		25 links	66⁄4	5.0292	The rod is also called pole or perch and equal to 5+1⁄2 yards
Area
Table of area units and equivalents
Unit	Abbr. or symbol	Relative to previous	Relation to units of length	Square feet	Square yards	Acres	Square metres	Hectares
perch*			1 rd × 1 rd	272+1⁄4	30+1⁄4	1⁄160	25.29285264	0.002529285264
rood		40 perches	1 furlong × 1 rd[17]	10890	1210	1⁄4	1011.7141056	0.10117141056
acre		4 roods	1 furlong × 1 chain	43560	4840	1	4046.8564224	0.40468564224
square mile	sq mi	640 acres	1 mi × 1 mi	27878400	3097600	640	2589988.110336	258.9988110336
Note: *The square rod has been called a pole or perch or, more properly, square pole or square perch for centuries.

Volume

Table of equivalences
Unit	Imperial
ounces	Imperial
pints	Millilitres	Cubic inches	US ounces	US pints
fluid ounce (fl oz)	1    	1⁄20    	28.4130625	1.7339	0.96076	0.060047
gill (gi)	5    	1⁄4    	142.0653125	8.6694	4.8038	0.30024
pint (pt)	20    	1    	568.26125	34.677	19.215	1.2009
quart (qt)	40    	2    	1136.5225	69.355	38.430	2.4019
gallon (gal)	160    	8    	4546.09	277.42	153.72	9.6076
Note: The millilitre equivalences are exact, but cubic-inch and US measures are correct to 5 significant figures.
Unit measures defined by the Weights and Measures Act 1824,
all measures determined by reference to the statute gallon of 277.274 cubic inches.[18]
Liquid	Dry	Capacity
1⁄2 gill		4.32 cu in (70.8 mL)
gill	1⁄4 pint	8.64 cu in (141.6 mL)
1⁄2 pint	1⁄2 pint	17.38 cu in (284.8 mL)
pint	pint	34.76 cu in (569.6 mL; 0.5696 L)
quart	quart	69.32 cu in (1.1360 L)
1⁄2 gallon	1⁄4 peck or 1⁄2 gallon	138.64 cu in (2.2719 L)
gallon	1⁄2 peck or gallon	277.274 cu in (4.54371 L)
2 gallons (peck)	peck	554.548 cu in (9.08741 L)
4 gallons (1⁄2 bushel)	1⁄2 bushel	1,109.096 cu in (18.17483 L)
8 gallons	bushel	2,218.192 cu in (36.34965 L)
64 gallons	quarter	17,745.536 cu in (290.79723 L)
Note: The 1824 Act removed the distinction between liquid and dry measure, specifying instead that
the dry quantities shall be unheaped. The metric equivalences shown are approximate.

Table of British apothecaries' volume units[nb 2]
Unit	Symbols and
abbreviations	Relative to
previous	Exact
metric value[note 1]
minim	♏︎, , m, m., min	  (1⁄9600 pint)	59.1938802083 µL
fluid scruple	fl ℈, fl s	20 minims (1⁄480 pint)	1.18387760416 mL
fluid drachm
(fluid dram, fluidram)	ʒ, fl ʒ, fʒ, ƒ 3, fl dr	3 fluid scruples (1⁄160 pint)	3.5516328125 mL
fluid ounce	℥, fl ℥, f℥, ƒ ℥, fl oz	8 fluid drachms	28.4130625 mL
pint	O, pt	20 fluid ounces	568.26125 mL
gallon	C, gal	8 pints	4.54609 L
Note:
 The vinculum over numbers (e.g. 3) represents a repeating decimal.

Table of mass units
Unit	Pounds	In SI units	Notes
grain (gr)	1⁄7000	64.79891 mg	Exactly 64.79891 milligrams.
drachm (dr)	1⁄256	1.7718451953125 g	A dram is 1⁄16 of an ounce
ounce (oz)	1⁄16	28.349523125 g	An ounce is 1⁄16 of a pound
pound (lb)	1	0.45359237 kg	Defined by The Units of Measurement Regulations 1994[33]
stone (st)	14	6.35029318 kg	The plural stone is often used when providing a weight (e.g. "this sack weighs 8 stone").[34] A person's weight is usually quoted in stone and pounds in English-speaking countries that use the avoirdupois system, with the exception of the United States and Canada, where it is usually quoted in pounds.
quarter (qr or qtr)	28	12.70058636 kg	One quarter (literally a quarter of a hundredweight) is equal to two stone or 28 pounds. The term quarter is also used in retail contexts, where it refers to four ounces, i.e. a quarter of a pound. (The 1824 Act defined a quarter as a unit of volume, as above: thus a 'quarter of wheat', 64 gallons, would weigh about 494 lb.[35]).
hundredweight (cwt)	112	50.80234544 kg	One imperial hundredweight is equal to eight stone. This is the long hundredweight, 112 pounds, as opposed to the short hundredweight of 100 pounds used in the United States and Canada.[36]
ton (t[citation needed])	2240	1016.0469088 kg	Twenty hundredweight equals a ton (as in the US and Canadian[36] systems). The imperial hundredweight is 12% greater than the US and Canadian one. The imperial ton (or long ton) is 2240 pounds, which is much closer to a tonne (about 2204.6 pounds), compared to the 10.7% smaller North American short ton of 2000 pounds (907.185 kg).
Gravitational units
slug (slug)	32.17404856	14.59390294 kg	The slug, a unit associated with imperial and US customary systems, is a mass that accelerates by 1 ft/s2 when a force of one pound (lbf) is exerted on it.[37]
F 	= ma (Newton's second law)
1 lbf 	= 1 slug × 1 ft/s2 (as defined above)
1 lbf 	= 1 lb × g/gc (by definition of the pound force[citation needed])
g 	≈ 32.17404856 ft/s2		gc 	≈ 32.17404856 lbm⋅ft/lbf⋅s2
∴	1 slug 	≈ 32.17404856 pounds

"""