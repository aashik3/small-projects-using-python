import requests

def track_phone_number_location(phone_number, api_key):
    url = f"http://apilayer.net/api/validate?access_key={api_key}&number={phone_number}&country_code=&format=1"

    response = requests.get(url)
    data = response.json()

    if data["valid"]:
        print("Phone number details:")
        print("Country Name:", data["country_name"])
        print("Location:", data["location"])
        print("Carrier:", data["carrier"])
        print("Line Type:", data["line_type"])
    else:
        print("Invalid phone number.")

def main():
    api_key = "c8e64f61e2c8d76d65b26d5d7236f775"
    phone_number = input("Enter the phone number to track (including country code): ")

    track_phone_number_location(phone_number, api_key)

if __name__ == "__main__":
    main()
