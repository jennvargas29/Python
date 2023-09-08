import requests
import schedule
import time


def get_weather(latitude, longitude):
    base_url = f"https://api.open-meteo.com/v1/forecast?latitud={latitude}&longitude={longitude}&current_weather=true&hourly=temperature_2m,relativehumidity_2m,windspeed_10m"
    response = requests.get(base_url)
    data = response.json()
    return data


def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5)+32


def send_text_message(body):
    account_sid = "twilio_sid"
    auth_token = "twilio_sid"
    from_phone_number = "from_phone_number"
    to_phone_number = "to_phone_number"

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body = body,
        from_ = from_phone_number,
        to = to_phone_number
    )
    print("Text message sent!")

def send_weather_update():
    #Hardcoded latitude and longitude for New York City
    latitude = 40.7128
    longitude = -74.0060

    weather_data =get_weather(latitude, longitude)
    temperature_celsius = weather_data["hourly"]["temperature_2m"][0]
    relativehumidity = weather_data["hourly"]["relativehumidity_2m"][0]
    wind_speed =weather_data["hourly"]["windspeed_10m"][0]
    temperature_fahrenheit = celsius_to_fahrenheit(temperature_celsius)

    weather_info = (
        f"Good morning! \n"
        f"Current weather in NYC:\n"
        f"Temperature: {temperature_fahrenheit:.2f}°F\n"
        f"Relative Humidity: {relativehumidity}%\n"
        f"Wind Speed:{wind_speed} m/s"
    )

    send_text_message(weather_info)

def main():
    schedule.every().day.at("08:00").do(send_weather_update)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()