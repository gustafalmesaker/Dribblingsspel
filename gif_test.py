from threading import Thread
import cv2
import time
from ultralytics import YOLO


#model = YOLO("models\model_v1.1.pt",task="detect") #load created model
ov_model = YOLO('models\\final_model_openvino_model',task="detect") #load openvino model


class VideoStreamWidget(object):
    def __init__(self, src=0):
        self.capture = cv2.VideoCapture(src)
        self.capture.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*"MJPG"))
        # Start the thread to read frames from the video stream
        self.thread = Thread(target=self.update, args=())
        self.thread.daemon = True
        self.thread.start()

    def update(self):
        # Read the next frame from the stream in a different thread
        while True:
            if self.capture.isOpened():
                (self.status, self.frame) = self.capture.read()
            time.sleep(.01)

    def show_frame(self):
        # Display frames in main program
        if self.frame is not None:
            cv2.imshow('frame', self.frame)
            results = ov_model.track(self.frame, persist=True)
            frame_ = results[0].plot()
            cv2.imshow('frame', frame_)
            key = cv2.waitKey(1)
            if key == ord('q'):
                self.capture.release()
                cv2.destroyAllWindows()
                exit(1)

if __name__ == "__main__":
    video_stream_widget = VideoStreamWidget()
    while True:
        try:
            video_stream_widget.show_frame()
        except AttributeError:
            pass


# def main():
#     # Open the default camera (usually the webcam)
#     #cap = cv2.VideoCapture(1)  # Change 1 to 0

#     cap = cv2.VideoCapture(1)
#     #cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
#     cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*"MJPG"))
#     width = 1920
#     height = 1080
#     cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
#     cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)


#     # Check if the camera is opened successfully
#     if not cap.isOpened():
#         print("Error: Could not open camera.")
#         return

#     while True:
#         # Capture frame-by-frame
#         ret, frame = cap.read()

#         # If frame is read correctly ret is True
#         if not ret:
#             print("Error: Can't receive frame (stream end?). Exiting ...")
#             break

#         # Display the resulting frame
#         cv2.imshow('Camera Feed', frame)

#         # Break the loop when 'q' is pressed
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     # Release the capture
#     cap.release()
#     cv2.destroyAllWindows()

# if __name__ == "__main__":
#     main()
