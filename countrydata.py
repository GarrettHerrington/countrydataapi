import requests as rq


def GetCountryData(country_name):
    url = f"https://restcountries.com/v3.1/name/{country_name}"
    response = rq.get(url)
    if response:
        print("Success!")
    else:
        print("Failed to grab Data.")
        raise Exception(f"Non-success status code: {response.status_code}")
    return response.json()


def display_country_details(country_data):
    country = country_data[0]
    print("Country Details:")
    print(f"Name: {country['name']['common']}")
    print(f"Official Name: {country['name']['official']}")
    print(f"Capital: {', '.join(country.get('capital', ['N/A']))}")
    print(f"Region: {country.get('region', 'N/A')}")
    print(f"Population: {country.get('population', 'N/A')}")
    print("Languages:")
    for lang_code, lang_name in country.get('languages', {}).items():
        print(f"- {lang_name} ({lang_code})")
    print("Currencies:")
    for currency_code, currency_info in country.get('currencies', {}).items():
        print(f"- {currency_info['name']} ({currency_code})")


def main():
    country_name = input("Enter a country: ")
    country_data = GetCountryData(country_name)
    display_country_details(country_data)


if __name__ == "__main__":
    main()
