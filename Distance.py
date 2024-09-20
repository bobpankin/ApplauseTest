import pandas as pd
from geopy.geocoders import Nominatim
from geopy.distance import great_circle

def get_coordinates(zip_code):
    geolocator = Nominatim(user_agent="zip_distance_calculator")
    location = geolocator.geocode(zip_code)
    
    if location:
        return (location.latitude, location.longitude)
    else:
        raise ValueError(f"Could not find coordinates for ZIP code: {zip_code}")

def calculate_distance(zip_code1, zip_code2):
    coords_1 = get_coordinates(zip_code1)
    coords_2 = get_coordinates(zip_code2)
    
    distance = great_circle(coords_1, coords_2).miles
    return distance

if __name__ == "__main__":
    zip_code1 = input("Enter the first ZIP code: ")
    zip_code2 = input("Enter the second ZIP code: ")
    
    try:
        distance = calculate_distance(zip_code1, zip_code2)
        print(f"The distance between ZIP code {zip_code1} and {zip_code2} is approximately {distance:.2f} miles.")
    except Exception as e:
        print(e)
