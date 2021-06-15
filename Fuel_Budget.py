
########################################## HOME PAGE ##########################################
homepage = "GET ESTIMATED COST OF FUEL BEFORE GOING ON TRIP".center(120)
p = '==' * 56
print()
print(p)
print(homepage)
print(p)
########################################## HOME PAGE ##########################################

print('\nEnter cost of fuel:')
Fuel = float(input(''.center(20)))

print('\nEnter Average of Vehicle:')
avrg = float(input(''.center(20)))

print('\nEnter Kms of single trip:')
trip_distance = float(input(''.center(20)))

INR = "\u20B9"


def fuel_cost(fuel):
    rs = fuel
    return f'{round(rs)} {INR}'

def single_trip_distance(trip_distance):
    dist = trip_distance
    return f'{dist} Km'

def round_trip_distance(trip_distance):
    total_distance = trip_distance * 2
    return f'{total_distance} Km'

def total_fuel_required(trip_distance):
    total_fuel = (2 * trip_distance) / avrg
    return f'{round(total_fuel)} Ltr'

def total_fuel_cost(trip_distance, fuel):
    total_cost = ((2 * trip_distance)/avrg) * fuel
    return f'{round(total_cost)} {INR}'



print('\n\n\n\n\n\n*ALL VALUES ARE ESTIMATED IT MAY VARY DEPENDS UPON THE FUEL PRICE')
print('-' * 103)
print('{:10} | {:10} | {:10} | {:10} | {:10}'.format('Current Fuel Cost',
                                                     'Single Trip Distance',
                                                     'Round Trip Distance',
                                                     'Total Fuel Required',
                                                     'Total Fuel Cost'))
print('-' * 103)
print('{:18}| {:21}| {:20}| {:20}| {:10}'.format(fuel_cost(fuel).center(10),
                              single_trip_distance(trip_distance).center(10),
                              round_trip_distance(trip_distance).center(10),
                              total_fuel_required(trip_distance).center(10),
                              total_fuel_cost(trip_distance, fuel)))

print('{} {} {} {}'.format('|'.center(38),
                              '|'.center(5),
                              '|'.center(38),
                              '|'.center(4)))
print('-' * 103)
print('Designed By: ABHINAV BILWANKAR'.center(175))
