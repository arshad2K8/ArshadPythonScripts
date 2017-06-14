__author__ = 'arshad'
import numpy as np
import matplotlib
from PIL import Image


sampleImage = Image.open('TestImage.jpg')
iar = np.asarray(sampleImage)
print iar