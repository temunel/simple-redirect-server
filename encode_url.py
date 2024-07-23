import base64

redirect_url = "http://example.com"

encoded_url = base64.b64encode(redirect_url.encode()).decode()
input_url = f"http://localhost:8080/{encoded_url}"
print(input_url)