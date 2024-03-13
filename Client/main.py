import cv2
import time
import Client.connections as connections
import sys

def log_errors_to_file(file_path):
    try:
        # Redirect standard error to the specified file
        sys.stderr = open(file_path, 'a')
    except Exception as e:
        print("Error occurred while redirecting stderr:", e)

# Example usage
log_errors_to_file('error_log.txt')

file_path = "output.mp4"
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'X264')
out = cv2.VideoWriter("output.mp4",fourcc, 20.0, (640,480))

start_time = time.time()
elapse_time = 20
while True:
    rel, frame = cap.read()
    out.write(frame)

    stop_time = time.time()
    if (stop_time - start_time) > elapse_time:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
connections.SendFootage(file_path)