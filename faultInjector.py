import numpy as np
from skimage.util import random_noise



class FaultInjector:
    def cameraNoiseIntoCarla(image):
        return add_gaussian_noise(image)

    def add_gaussian_noise(self, image, variance=0.152)
        img_arr = np.asarray(image)
        noise = random_noise(img_arr, var=variance)
        noise_arr = (255noise).astype(np.uint8)
        noise_img = Image.fromarray(noise_arr)
        return noise_img

    def add_saltandpepper_noise(self, image, proportion=0.05)
        img_arr = np.asarray(image)
        noise = random_noise(img_arr,mode='s&p', amount=proportion)
        noise_arr = (255noise).astype(np.uint8)
        noise_img = Image.fromarray(noise_arr)
        return noise_img
