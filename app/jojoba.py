from webapp import WebApp
import os

PORT = 5000

request_latency = os.getenv('REQUEST_LATENCY')

app = WebApp()

if __name__ == "__main__":
    if request_latency.isdigit():
        request_latency = int(request_latency)
        app.set_request_latency(request_latency)
    app.run(host='0.0.0.0', port=PORT, debug=True)
    

