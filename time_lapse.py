import cv2
import time
from threading import Thread
from datetime import datetime


class TimeLapse:
    def __init__(self, period, max_frames=100, resolution=(1280, 720), fps=24, data_folder='image'):
        self.period = period
        self.max_frames = max_frames
        self.resolution = resolution
        self.fps = fps
        self.data_folder = data_folder

        self.images = []

        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.resolution[0])
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.resolution[1])

        self.thread = Thread(target=self.time_lapse_loop)

    def time_lapse_loop(self):
        while len(self.images) < self.max_frames:
            print(str(len(self.images)) + '/' + str(self.max_frames))
            _, frame = self.cap.read()
            self.save_img(frame)
            time.sleep(self.period)
        self.save_video()

    def save_img(self, frame):
        img_name = datetime.now().strftime('%Y-%m-%d-%H-%M-%S-%f')
        self.images.append(img_name)
        cv2.imwrite(self.data_folder + '/' + img_name + '.jpg', frame, [int(cv2.IMWRITE_JPEG_QUALITY), 90])

    def save_video(self):
        fourcc = cv2.VideoWriter_fourcc('D', 'I', 'V', 'X')
        video_name = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        out = cv2.VideoWriter('video/' + video_name + '.avi', fourcc, self.fps, self.resolution)
        for img in self.images:
            out.write(cv2.imread(self.data_folder + '/' + img + '.jpg'))
        out.release()
