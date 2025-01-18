import base64

def print_type_and_value(label, value):
    print(f"{label:<50} {str(type(value)):<30} {value}")

# Original message
message = "Hello, World!"
print_type_and_value("message", message)

# Encode the message to UTF-8 bytes
utf8_encoded_message = message.encode("utf-8")
print_type_and_value("utf8_encoded_message", utf8_encoded_message)

# Encode the UTF-8 bytes to Base64
base64_encoded_utf8_encoded_message = base64.b64encode(utf8_encoded_message)
print_type_and_value("base64_encoded_utf8_encoded_message", base64_encoded_utf8_encoded_message)

# Decode the Base64 bytes back to a string
decoded_base64_encoded_utf8_encoded_message = base64_encoded_utf8_encoded_message.decode()
print_type_and_value("decoded_base64_encoded_utf8_encoded_message", decoded_base64_encoded_utf8_encoded_message)

# Create a payload dictionary with the Base64 string
payload = {"data": decoded_base64_encoded_utf8_encoded_message}
print_type_and_value("payload", payload)

# Extract the Base64 string from the payload
payload_data = payload["data"]
print_type_and_value("payload_data", payload_data)

# Decode the Base64 string back to UTF-8 bytes
base64_decoded_payload_data = base64.b64decode(payload_data)
print_type_and_value("base64_decoded_payload_data", base64_decoded_payload_data)

# Decode the UTF-8 bytes back to the original message
utf8_decoded_base64_decoded_payload_data = base64_decoded_payload_data.decode("utf-8")
print_type_and_value("utf8_decoded_base64_decoded_payload_data", utf8_decoded_base64_decoded_payload_data)

