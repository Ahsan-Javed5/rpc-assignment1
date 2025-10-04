import requests
import json

# base URL
BASE_URL = "http://127.0.0.1:8080"
TIMEOUT_SECONDS = 2

def call_server(endpoint, x, y):
    url = f"{BASE_URL}/{endpoint}"
    data = {"x": x, "y": y}
    
    try:
        response = requests.post(url, json=data, timeout=TIMEOUT_SECONDS)
        
        if response.status_code == 200:
            return response.json().get("result")
        else:
            return f"Server returned error code: {response.status_code}"

    except requests.exceptions.Timeout:
        return "Request timed out" 

    except requests.exceptions.RequestException as e:
        return f"Request failed: Connection Error"

def add(x, y):
    return call_server("add", x, y)

def multiply(x, y):
    return call_server("multiply", x, y)


if __name__ == '__main__':
    print("Example client output:")
    
    # examples...
    a, b = 2, 3
    add_result = add(a, b)
    print(f"add({a},{b}) = {add_result}") 

    c, d = 4, 5
    multiply_result = multiply(c, d)
    print(f"multiply({c},{d}) = {multiply_result}")