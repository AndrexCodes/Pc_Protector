import requests

url = "https://ionextechsolutions.com/protector/upload"

def SendFootage(file_path):
    try:
        with open(file_path, 'rb') as file:
            files = {'video': file}
            print("Submitting video ....")
            response = requests.post(url, files=files)
            if response.status_code == 200:
                print("Video successfully sent.")
            else:
                print("Error sending video. Status code:", response.status_code)
    except FileNotFoundError:
        print("File not found.")