from webapp import WebApp

PORT = 5000

app = WebApp()

if __name__ == "__main__":
    app.set_request_interval(0)
    app.run(host='0.0.0.0', port=PORT, debug=True)
    

