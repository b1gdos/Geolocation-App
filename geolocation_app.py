from geopy.geocoders import Nominatim

def get_coordinates(country, city):
    """
    Get latitude and longitude coordinates of the given city in the specified country.
    
    Args:
        country (str): The name of the country.
        city (str): The name of the city.
    
    Returns:
        tuple: A tuple containing the latitude and longitude coordinates.
    """
    address = f"{city}, {country}"
    geolocator = Nominatim(user_agent="geoapi")
    location = geolocator.geocode(address)
    
    if location:
        return location.latitude, location.longitude
    else:
        return None

def main():
    country = input("Enter the country: ")
    city = input("Enter the city: ")
    coordinates = get_coordinates(country, city)
    
    if coordinates:
        print(f"Latitude: {coordinates[0]}, Longitude: {coordinates[1]}")
    else:
        print("Coordinates not found for the given country and city.")

if __name__ == "__main__":
    main()
