import requests

def get_ip_details(api_key):
    try:
        response = requests.get(f'http://api.ipstack.com/check?access_key={api_key}')
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print("Error fetching IP details:", e)
        return None

def display_ip_details(ip_details):
    if ip_details:
        print("IP Address:", ip_details['ip'])
        print("Type:", ip_details['type'])
        print("Continent:", ip_details['continent_name'])
        print("Country:", ip_details['country_name'])
        print("Region:", ip_details['region_name'])
        print("City:", ip_details['city'])
        if 'ip' in ip_details:
            print("IPv6 Address:", ip_details['ip'])
        if 'isp' in ip_details:
            print("ISP:", ip_details['isp'])
    else:
        print("Failed to retrieve IP details.")

def main():
    api_key = '2132c95bfe51fcb7fe15c09101fd6cd8'
    ip_details = get_ip_details(api_key)
    display_ip_details(ip_details)

if __name__ == "__main__":
    main()