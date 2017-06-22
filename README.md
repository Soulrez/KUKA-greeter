# KUKA-greeter
An autonomous greeter built in ROS for a KUKA YouBot robot. It uses a facial recognition neural network to detect faces through the webcam, and if a face has found, it checks whether it is someone that it knows or a guest. If it is someone that it knows, then it will say a greeting. Otherwise, it welcomes the guest and does a wave with the arm!
Video demo: https://www.youtube.com/watch?v=pHbP-r5PXvs

Hardware:
KUKA YouBot 
Webcam
External laptop for processing

Software:
ROS Indigo or later
OpenFace 
espeak
