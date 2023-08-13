#!/usr/bin/env python3

import time
import math
import threading
import numpy as np

class TransformBroadcaster:
    def __init__(self):
        self.transforms = {}
        self.lock = threading.Lock()

    def send_transform(self, transform):
        with self.lock:
            self.transforms[transform['child']] = transform

    def publish_transforms(self):
        while True:
            with self.lock:
                for child, transform in self.transforms.items():
                    print(f"Child: {child}, Translation: {transform['translation']}, Rotation: {transform['rotation']}")
            time.sleep(1.0)

def main():
    broadcaster = TransformBroadcaster()
    thread = threading.Thread(target=broadcaster.publish_transforms)
    thread.daemon = True
    thread.start()

    while True:
        time_now = time.time()

        planeta_angulo = time_now * math.pi / 5.0
        planeta_transform = {
            'child': 'planeta',
            'translation': [radius * math.cos(planeta_angulo), radius * math.sin(planeta_angulo), 0.0],
            'rotation': [0.0, 0.0, 0.0, 1.0]
        }
        broadcaster.send_transform(planeta_transform)

        satelite_angulo = time_now * math.pi / 2.0
        satelite_transform = {
            'child': 'satelite',
            'translation': [radius * math.cos(satelite_angulo), radius * math.sin(satelite_angulo), 0.0],
            'rotation': [0.0, 0.0, 0.0, 1.0]
        }
        broadcaster.send_transform(satelite_transform)

        time.sleep(0.1)

if __name__ == '__main__':
    radius = 5.0  # Altere o raio da órbita aqui
    main()
