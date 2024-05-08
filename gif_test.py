from threading import Thread
import cv2
import time
from ultralytics import YOLO

# Load OpenVINO model
ov_model = YOLO('models\\final_model_20_epochs_openvino_model', task="detect")

class VideoStreamWidget(object):
    def __init__(self, src=0):
        self.capture = cv2.VideoCapture(src)
        self.capture.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*"MJPG"))
        # Start the thread to read frames from the video stream
        self.thread = Thread(target=self.update, args=())
        self.thread.daemon = True
        self.thread.start()
        self.circle_pos_x = 200
        self.circle_pos_y = 200

    def update(self):
        # Read the next frame from the stream in a different thread
        while True:
            if self.capture.isOpened():
                (self.status, self.frame) = self.capture.read()
            time.sleep(.01)

    def center_points(self, results):
        box_list = []
        sports_ball_id = 32
        person_id = 0

        if results[0].boxes.xywh is not None:
            for obj in results[0].boxes:
                if obj.cls == sports_ball_id:
                    x, y, w, h = obj.xywh[0].tolist()
                    box_list.append([x, y])

                # elif obj.cls == person_id:
                #     x_n, y_n, w, h = obj.xywhn[0].tolist()
                #     box_list.append([x_n, y_n])
        return box_list

    def show_frame(self):
        # Display frames in main program
        if self.frame is not None:
            
            results = ov_model.track(self.frame, persist=True)
            #frame_ = results[0].plot()
            #cv2.imshow('frame', frame_)

            if results[0] is not None:
                pos = self.center_points(results)
                if pos:
                    self.circle_pos_x, self.circle_pos_y = pos[0]
                    print(self.circle_pos_x, self.circle_pos_y)
                else:
                    self.circle_pos_x = self.circle_pos_x
                    self.circle_pos_y = self.circle_pos_y
            # Show a circle on the position of the ball
            cv2.circle(self.frame, (int(self.circle_pos_x), int(self.circle_pos_y)), radius=15, color=(0, 255, 0), thickness=-1)  # Adjust radius and color as needed
            cv2.imshow('frame', self.frame)
            key = cv2.waitKey(1)
            if key == ord('q'):
                self.capture.release()
                cv2.destroyAllWindows()
                exit(1)

if __name__ == '__main__':
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
