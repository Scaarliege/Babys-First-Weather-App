import requests
import geocoder

def check_api_status():
    print("Initializing, please wait")
    
    nominatim_url = "https://nominatim.openstreetmap.org/search"
    
    try:
        headers = {
        'User-Agent': 'BabysFirstWeatherApp/1.0 (scaarliege@gmail.com)'
            }
        response = requests.get(nominatim_url, params={'q': 'test', 'format': 'json'}, headers=headers)
        response.raise_for_status()
        print("Nominatim API is functional.")
    
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to Nominatim API: {e.response.status_code if e.response else 'No response'}")
        return False
    
    weather_url = "https://api.open-meteo.com/v1/forecast"
    
    try:
        response = requests.get(weather_url, params={'latitude': 0, 'longitude': 0, 'current_weather': 'true', 'timezone': 'auto'})
        response.raise_for_status()
        print("Open-Meteo API is functional.\n---------------")
    
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to Open-Meteo API: {e.response.status_code if e.response else 'No response'}")
        return False
    
    g = geocoder.ip('me')
    lat, lon = g.latlng
    city = g.city
    country = g.country
    
    if lat and lon:
        print("Fetching weather data for your location:")
        print(f"City: {city}")
        print(f"Latitude: {lat}, Longitude: {lon}\n")
        
        if country == "US" or country == "MM" or country == "LR":
            get_weather(lat, lon, "imperial")
        
        else:
            get_weather(lat, lon, "metric")
    else:
        print("Could not fetch your current location based on IP address.")
        return False
    
    print("---------------")
    return True

def get_lat_long(place_name):
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        'q': place_name,
        'format': 'json',
        'addressdetails': 1,
        'limit': 1
    }
    headers = {
        'User-Agent': 'BabysFirstWeatherApp/1.0 (scaarliege@gmail.com)'
    }
   
    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        data = response.json()
        if not data:
            print("Place not found!")
            return None, None
        lat = float(data[0]['lat'])
        lon = float(data[0]['lon'])
        return lat, lon
   
    except requests.exceptions.RequestException as e:
        print(f"Error fetching geolocation data: {e}")
        return None, None

def get_weather(latitude, longitude, data_type):
    url = f"https://api.open-meteo.com/v1/forecast"
    
    params = {
        'latitude': latitude,
        'longitude': longitude,
        'current_weather': 'true',
        'timezone': 'auto',
    }
   
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
       
        current_weather = data['current_weather']
        temperature = current_weather['temperature']
        wind_speed = current_weather['windspeed']
        weather_description = current_weather['weathercode']
       
        weather_codes = {
            0: 'Clear sky',
            1: 'Partly cloudy',
            2: 'Cloudy',
            3: 'Overcast',
            45: 'Fog',
            48: 'Depositing rime fog',
            51: 'Light drizzle',
            53: 'Drizzle',
            55: 'Heavy drizzle',
            56: 'Freezing drizzle',
            57: 'Heavy freezing drizzle',
            61: 'Light rain',
            63: 'Rain',
            65: 'Heavy rain',
            66: 'Freezing rain',
            67: 'Heavy freezing rain',
            71: 'Light snow',
            73: 'Snow',
            75: 'Heavy snow',
            77: 'Snow grains',
            80: 'Showers of rain',
            81: 'Heavy showers of rain',
            82: 'Violent showers of rain',
            85: 'Showers of snow',
            86: 'Heavy showers of snow',
            95: 'Thunderstorm',
            96: 'Thunderstorm with hail',
            99: 'Heavy thunderstorm with hail'
        }

        weather_description = weather_codes.get(weather_description, 'Unknown weather')

        if data_type == "metric" or data_type == "m":
            print(f"Current temperature: {temperature:.2f}°C")
            print(f"Wind speed: {wind_speed:.2f} km/h")
        
        elif data_type == "imperial" or data_type == "i":
            temperature = (temperature * (9/5)) + 32
            wind_speed = wind_speed * 0.621371
            print(f"Current temperature: {temperature:.2f}°F")
            print(f"Wind speed: {wind_speed:.2f} mph")
        
        else:
            print("Error processing unit_type, please enter valid unit type")
        
        print(f"Weather description: {weather_description}")
   
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")

if not check_api_status():
    print("\nExiting...")
    quit()

while __name__ == "__main__":
    place_name = input("Enter the place name: ")
    data_type = input("Enter Unit type [metric/imperial] [m/i]: ").lower()
    
    latitude, longitude = get_lat_long(place_name)
    
    if latitude is not None and longitude is not None:
        print(f"\nData:\nLatitude: {latitude}, Longitude: {longitude}")
        get_weather(latitude, longitude, data_type)
    
    print("\n---------------")