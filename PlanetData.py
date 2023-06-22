import numpy as np

# Mass in Earth masses, semi-major axis, eccentricity, orbital inclination/degrees,
# Radius in earth radii, Rotational period/days, orbital period/years, planet name,
#task 5 time increment 

object_data = {
    0: np.array([0.055, 0.387, 0.21, 7, 0.383, 58.646, 0.243, "Mercury", 0.01]),
    1: np.array([0.815, 0.723, 0.01, 3.39, 0.949, 243.018,  0.615, "Venus", 0.01]),
    2: np.array([1, 1, 0.02, 0, 1, 0.997, 1, "Earth", 0.1]),
    3: np.array([0.107, 1.523, 0.09, 1.85, 0.533, 1.026, 1.881, "Mars", 0.1]),
    4: np.array([317.85, 5.202, 0.05, 1.31, 11.209, 0.413, 11.861, "Jupiter", 1]),
    5: np.array([95.159, 9.576, 0.06, 2.49, 9.449, 0.444, 29.628, "Saturn", 1]),
    6: np.array([14.5, 19.293, 0.05, 0.77, 4.007, 0.718, 84.747, "Uranus", 1]),
    7: np.array([17.204, 30.246, 0.01, 1.77, 3.883, 0.671, 166.344, "Neptune", 2]),
    8: np.array([0.003, 39.509, 0.25, 17.5, 0.187, 6.387, 248.348, "Pluto", 2]),         # 0-8 are celestial bodies that orbit sol, 9 and above orbit other stars( star orbited is denoted in name of planet)
    9: np.array([804.30428,	2.1,	0.03,	"N/A", 13.226521,	"N/A",	3, "47 Ursae Majoris b", 0.1]),
    10: np.array([171.66969,	3.6,	0.1,	"N/A",	14.235323,	"N/A",	6.6, "47 Ursae Majoris c", 0.1]),
    11: np.array([521.3672,	11.6,	0.16,	"N/A",	13.4507,	"N/A",	38.4, "47 Ursae Majoris d", 1]),
    12: np.array([9.310125386,	0.1134,	0,	"N/A",	13.899055,	"N/A",	0.04027397, "55 Cancri b", 0.0001]),
    13: np.array([54.48923092,	0.2373,	0.03,	"N/A",	8.5187759,	"N/A",	0.1216438, "55 Cancri c", 0.0001]),
    14: np.array([43.4681751,	5.957,	0.13,	"N/A",	13.002342,	"N/A",	15.3, "55 Cancri d", 0.01]),
    15: np.array([7.99,	0.01544,	0.05,	"N/A",	1.875,	"N/A",	0.001917808, "55 Cancri e", 0.000001]),
    16: np.array([44.8248632,	0.7708,	0.08,	"N/A",	7.58843593,	"N/A",	0.712054795, "55 Cancri f", 0.001]),
    17: np.array([5.1,	0.050201,	0.12,	"N/A",	2.11,	"N/A",	0.01150685, "61 Virginis b", 0.0001]),
    18: np.array([18.2,	0.2175,	0.14,	"N/A",	4.46114845,	"N/A",	0.10411, "61 Virginis c", 0.001]),
    19: np.array([22.9,	0.476,	0.35,	"N/A",	5.11126556,	"N/A",	0.3369863, "61 Virginis d", 0.001]),
    20: np.array([4.07661,	1.681,	0,	"N/A",	1.681,	"N/A",	0.002465753, "CoRoT-7 b", 0.00001]),
    21: np.array([8.4,	0.046,	0,	"N/A",	2.83585567,	"N/A",	0.01013699, "CoRoT-7 c", 0.0001]),
    22: np.array([24.27,	0.1462,	0.083,	"N/A",	5.29060821,	"N/A",	0.050958904, "DMPP-1 b", 0.001]),
    23: np.array([9.6,	0.0733,	0.057,	"N/A",	3.06003399,	"N/A",	0.01808219, "DMPP-1 c", 0.001]),
    24: np.array([3.35,	0.0422,	0.07,	"N/A",	1.65,	"N/A",	0.007945205, "DMPP-1 d", 0.0001]),
    25: np.array([4.13,	0.0651,	0.07,	"N/A",	1.86,	"N/A",	0.01506849, "DMPP-1 e", 0.001]),
    26: np.array([8.75,	0.047,	0.06,	"N/A",	1.95,	"N/A",	0.009863014, "EPIC 249893012 b", 0.0001]),
    27: np.array([14.67,	0.13,	0.07,	"N/A",	3.66531544,	"N/A",	0.042739726, "EPIC 249893012 c", 0.001]),
    28: np.array([10.18,	0.22,	0.15,	"N/A",	3.94553833,	"N/A",	0.097808219, "EPIC 249893012 d", 0.001]),
    29: np.array([1.37,	0.021,	0.31,	"N/A",	1.1,	"N/A",	0.008767123, "GJ 1061 b", 0.0001]),
    30: np.array([1.74,	0.035,	0.29,	"N/A",	1.18,	"N/A",	0.01835616, "GJ 1061 c", 0.001]),
    31: np.array([1.64,	0.054,	0.53,	"N/A",	1.16,	"N/A",	0.0356164, "GJ 1061 d", 0.001]),
    32: np.array([10.6,	0.0607,	0.07,	"N/A", 	3.2505856,	"N/A",	0.02356164, "GJ 163 b", 0.001]),
    33: np.array([6.8,	0.1254,	0.1,	"N/A",	2.4995882,	"N/A",	0.070136986, "GJ 163 c", 0.001]),
    34: np.array([29.4,	1.0304,	0.37,	"N/A",	5.91830749,	"N/A", 	1.7, "GJ 163 d", 0.1]),
    35: np.array([5.3,	0.0648,	0,	"N/A",	0.82,	"N/A",	0.0169863, "Kepler-106 b", 0.001]),
    36: np.array([10.44,	0.1096,	0,	"N/A",	2.4995882,	"N/A",	0.037260274, "Kepler-106 c", 0.001]),
    37: np.array([8.1,	0.1602,	0,	"N/A",	0.95,	"N/A",	0.0657534, "Kepler-106 d", 0.001]),
    38: np.array([11.17,	0.2395,	0,	"N/A",	2.55563278,	"N/A",	0.12, "Kepler-106 e", 0.01]),
    39: np.array([0.704,	0.0677,	0.08,	"N/A",	0.914,	"N/A",	0.0273973, "TOI-700 b", 0.001]),
    40: np.array([7.27,	0.0929,	0.07,	"N/A",	2.60046844,	"N/A",	0.044109589, "TOI-700 c", 0.001]),
    41: np.array([1.25,	0.1633,	0.04,	"N/A",	1.073,	"N/A",	0.10246575, "TOI-700 d", 0.001]),
    42: np.array([0.818,	0.134,	0.06,	"N/A", 	0.953,	"N/A",	0.076164384, "TOI-700 e", 0.001])

}
    
inner_planets = {
    0: np.array([0.055, 0.387, 0.21, 7, 0.383, 58.646, 0.243, "Mercury"]),
    1: np.array([0.815, 0.723, 0.01, 3.39, 0.949, 243.018,  0.615, "Venus"]),
    2: np.array([1, 1, 0.02, 0, 1, 0.997, 1, "Earth"]),
    3: np.array([0.107, 1.523, 0.09, 1.85, 0.533, 1.026, 1.881, "Mars"])
}

outer_planets = {
    0: np.array([317.85, 5.202, 0.05, 1.31, 11.209, 0.413, 11.861, "Jupiter"]),
    1: np.array([95.159, 9.576, 0.06, 2.49, 9.449, 0.444, 29.628, "Saturn"]),
    2: np.array([14.5, 19.293, 0.05, 0.77, 4.007, 0.718, 84.747, "Uranus"]),
    3: np.array([17.204, 30.246, 0.01, 1.77, 3.883, 0.671, 166.344, "Neptune"]),
    4: np.array([0.003, 39.509, 0.25, 17.5, 0.187, 6.387, 248.348, "Pluto"])
}
    
