import json
import cv2
import base64
from channels.generic.websocket import WebsocketConsumer
from .models import Capture


class MouseWebcamConsumer(WebsocketConsumer):
    mouse_data = {'x': 0, 'y': 0}
    cap = cv2.VideoCapture(0)

    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        self.cap.release()

    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        event_type = text_data_json['event']

        if event_type == 'mouse_move':
            self.mouse_data['x'] = text_data_json['x']
            self.mouse_data['y'] = text_data_json['y']
            self.send(text_data=json.dumps({
                'type': 'mouse_update',
                'x': self.mouse_data['x'],
                'y': self.mouse_data['y']
            }))
        elif event_type == 'take_picture':
            ret, frame = self.cap.read()
            if ret:
                _, buffer = cv2.imencode('.jpg', frame)
                img_str = base64.b64encode(buffer).decode('utf-8')

                capture = Capture(x=self.mouse_data['x'], y=self.mouse_data['y'], image=img_str)
                capture.save()

                self.send(text_data=json.dumps({
                    'type': 'picture_taken',
                    'image': img_str
                }))
