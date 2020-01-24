# Objects_classification
In computer vision, local descriptors (features computed over limited spatial support) have proved well-adapted to matching and
recognition tasks, as they are robust to partial visibility and clutter. Such tasks require descriptors that are repeatable. 
Here, we mean repeatable in the sense that if there is a transformation between two instances of an object in a trajectory,
corresponding points are detected and identical descriptor values are obtained around each one of them. Specifically, we used SIFT
to detect keypoints and extract descriptors, and Hu moments asaverage of image pixel intensities  from both the training and testing
image data sets. Followed by assigning each image the respective tuple (Hu, descriptors) as attribute.
differents way of classifications was used.
