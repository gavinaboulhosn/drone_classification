# Drone Classification

## Overview
This research involves classifying UAVs based on RF characteristics by using Change Point Detection, Dynamic Time Warping, and Convolutional Neural Networks. To do this, I implemented a change-point detection algorithm utilizing the radial basis function (RBF) kernel method to detect UAV signals.  Since Dynamic Time Warping is conventionally used with much smaller data sets, I had to implement a three-stage Haar Transform/Wavelet Decomposition algorithm to remove signal bias and decimate the signal without changing its signature.
