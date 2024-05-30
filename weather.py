import python_weather
import asyncio
import os

async def getweather():
    async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
        city = input("Enter City: ")
        weather = await client.get(city)
        
        print("\n" + "="*50)
        print(f"WEATHER FOR: {city.upper()}".center(50))
        print(f"{weather.country.upper()}".center(50))
        print(f"{weather.datetime}".center(50))
        print("="*50)
        
        print("\nCURRENT TEMP:")
        print(f"{weather.temperature}°F".center(50))
        print("-"*50)
        
        print("\nFEELS LIKE:")
        print(f"{weather.feels_like}°F".center(50))
        print("="*50)

        print("\nDAILY FORECASTS:")
        for daily in weather.daily_forecasts:
            print("\n" + "-"*50)
            print(f"Date: {daily.date.strftime('%A, %B %d, %Y')}".center(50))
            print(f"Temperature: {daily.temperature}°F".center(50))
            print(f"Weather: {weather.description}".center(50))
            print("-"*50)
            
            print("HOURLY FORECASTS:")
            print('*'*50)
            for hourly in daily.hourly_forecasts:
                print(f"Time: {hourly.time.strftime('%I:%M %p')}, Temp: {hourly.temperature}°F, Weather: {hourly.kind}".center(50))

if __name__ == '__main__':
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(getweather())
