import numpy as np
import cv2 as cv
import glob, os


# It sets a minimum match count to 15, 
# which means that at least 15 matching features are required to consider two fingerprint images as a match.
MIN_MATCH_COUNT = 15



# PHOTO TO FIND FEATURE POINTS
# It loads a reference fingerprint image (specified as 'input_img') and converts it to grayscale. 

#input_img = cv.imread('./Fingerprint-Matching/fig0.png')
input_img = cv.imread('./output/1.png')
input_img = input_img.astype('uint8')
gray = cv.cvtColor(input_img, cv.COLOR_BGR2GRAY)
sift = cv.SIFT_create()  # Use cv.SIFT_create() instead of cv.xfeatures2d.SIFT_create()
# uses the Scale-Invariant Feature Transform (SIFT) algorithm to detect key points (features) in the image.
kp = sift.detect(input_img, None)
img1 = cv.drawKeypoints(input_img, kp, input_img)

flag = 0

os.chdir("./")
for file in glob.glob("*.png"):

    frame = cv.imread(file) # It reads the image file using cv.imread and assigns it to the variable frame.
    frame = frame.astype('uint8')
    gray1 = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # It uses the SIFT (Scale-Invariant Feature Transform) algorithm for feature detection.
    sift = cv.SIFT_create()  # Use cv.SIFT_create() instead of cv.xfeatures2d.SIFT_create()


    kp = sift.detect(frame, None)
    img2 = cv.drawKeypoints(frame, kp, frame)

    # The SIFT algorithm is applied to the 'frame' to detect key points. These key points are stored in the variable kp.
    kp1, des1 = sift.detectAndCompute(img1, None)
    kp2, des2 = sift.detectAndCompute(img2, None)

    FLANN_INDEX_KDTREE = 0 
    # is a constant indicating the algorithm to be used in the FLANN 
    # (Fast Library for Approximate Nearest Neighbors) matcher. 
    index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
    search_params = dict(checks=50)
    flann = cv.FlannBasedMatcher(index_params, search_params)
    matches = flann.knnMatch(np.asarray(des1, np.float32), np.asarray(des2, np.float32), k=2)
    good = []
    for m, n in matches:
        if m.distance < 0.7 * n.distance:
            good.append(m)
    if len(good) > 10:
        src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
        dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)
        M, mask = cv.findHomography(src_pts, dst_pts, cv.RANSAC, 5.0)
        matchesMask = mask.ravel().tolist()
        print("Matched " + str(file))
        flag = 1

    # If there are not enough good matches (less than 10 in this case), it sets 
    # matchesMask to None and doesn't set the flag to 1. 
    # This indicates that no match was found for this particular image.    
    else: 
        matchesMask = None

    draw_params = dict(matchColor=(0, 255, 0),  # draw matches in green color
                       singlePointColor=None, # is set to None, which means the single points (keypoints) won't be drawn in a different color.
                       matchesMask=matchesMask,  # draw only inliers
                       flags=2)

    img3 = cv.drawMatches(img1, kp1, img2, kp2, good, None, **draw_params)
    cv.imshow("Match", img3) # is used to display the image containing the visualized matches.

    cv.waitKey(0)
    cv.destroyAllWindows()


if flag == 0:
    print("No Matches among the given set!!")
else:
    print("Fingerprint Matche!")