import cv2
import numpy as np
import copy

from Airlight import Airlight
from BoundCon import BoundCon
from CalTransmission import CalTransmission
from removeHaze import removeHaze

from vehicle_detector import VehicleDetector

if __name__ == '__main__':
    HazeImg = cv2.imread('images/img2.jpg')

    # Estimate Airlight
    windowSze = 15
    AirlightMethod = 'fast'
    A = Airlight(HazeImg, AirlightMethod, windowSze)

    # Calculate Boundary Constraints
    windowSze = 3
    C0 = 20         # Default value = 20 
    C1 = 300        # Default value = 300 
    Transmission = BoundCon(HazeImg, A, C0, C1, windowSze)  #   Computing the Transmission using equation (7) in the report

    # Refine estimate of transmission
    regularize_lambda = 1       # Default value = 1 --> Regularization parameter, the more this  value, the closer to the original patch wise transmission
    sigma = 0.5
    Transmission = CalTransmission(HazeImg, Transmission, regularize_lambda, sigma)     # Using contextual information

    # Perform DeHazing
    HazeCorrectedImg = removeHaze(HazeImg, Transmission, A, 0.85)


    # Vehicle detection

    # Load Veichle Detector
    vd = VehicleDetector()

    vehicle_image = copy.deepcopy(HazeCorrectedImg)
    vehicle_boxes = vd.detect_vehicles(vehicle_image)

    for box in vehicle_boxes:
        x, y, w, h = box

        cv2.rectangle(vehicle_image, (x, y), (x + w, y + h), (25, 0, 180), 3)
    
    cv2.imshow('Original', HazeImg)
    cv2.imshow('Dehazed image', HazeCorrectedImg)
    cv2.imshow("Vehicle image", vehicle_image)

    cv2.waitKey(0)

