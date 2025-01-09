import requests

def get_weather(city):
    api_key = "YOU API KEY"  # You'll need to sign up for a free key at OpenWeatherMap
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"
    
    try:
        response = requests.get(url)
        weather_data = response.json()
        
        temperature = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']
        
        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Description: {description}")
        
    except:
        print("Sorry, couldn't get the weather for that city!")

# Use the function
city = input("Enter a city name: ")
get_weather(city)