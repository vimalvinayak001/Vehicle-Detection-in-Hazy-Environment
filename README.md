# Vehicle Detection in Hazy Environment

An innovative solution for Vehicle Detection in Foggy/Hazy Environments by integrating YOLO V4, a state-of-the-art object detection model, after effective defogging of images. This approach significantly enhanced visibility and accuracy in adverse weather conditions.

## Steps followed in the Project:
* It starts with a hazy image and estimates the airlight and transmission.
* The transmission is refined using contextual information.
* Haze is removed from the image to obtain a dehazed version.
* The dehazed image is then passed to a vehicle detector, which identifies vehicles in the image and draws bounding boxes around them.

![original](https://github.com/kumarpradumn/Vehicle-Detection-in-Hazy-Environment/assets/91341367/e5626719-e05b-47ca-b702-198612494687)
![dehazed](https://github.com/kumarpradumn/Vehicle-Detection-in-Hazy-Environment/assets/91341367/c1423a29-fb23-4fbf-9ebf-fac6145b615a)
![vehicles](https://github.com/kumarpradumn/Vehicle-Detection-in-Hazy-Environment/assets/91341367/b4e8d231-cd56-48e5-978f-bed49f342a87)
