from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_ip_details(api_key, ip_address):
    try:
        response = requests.get(f'http://api.ipstack.com/{ip_address}?access_key={api_key}')
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print("Error fetching IP details:", e)
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    ip_details = None
    if request.method == 'POST':
        ip_address = request.form['ip_address']
        api_key = '6521eca336b59fa4c01ff70c74e4fd7e'  # Replace with your actual API key
        ip_details = get_ip_details(api_key, ip_address)

    return render_template('index.html', ip_details=ip_details)

if __name__ == '__main__':
    app.run(debug=True)
