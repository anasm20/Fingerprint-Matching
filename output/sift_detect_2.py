import numpy as np
import cv2 as cv
import glob

# Erhöhen, um mehr Übereinstimmungen zu benötigen
MIN_MATCH_COUNT = 20

input_img = cv.imread('./output/1.png')
input_img = input_img.astype('uint8')
gray = cv.cvtColor(input_img, cv.COLOR_BGR2GRAY)
sift = cv.SIFT_create()
kp = sift.detect(input_img, None)
img1 = cv.drawKeypoints(input_img, kp, input_img)

flag = 0

for file in glob.glob("*.png"):
    frame = cv.imread(file)
    frame = frame.astype('uint8')
    gray1 = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    sift = cv.SIFT_create()
    kp = sift.detect(frame, None)
    img2 = cv.drawKeypoints(frame, kp, frame)
    kp1, des1 = sift.detectAndCompute(img1, None)
    kp2, des2 = sift.detectAndCompute(img2, None)

    FLANN_INDEX_KDTREE = 0
    index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
    search_params = dict(checks=50)
    flann = cv.FlannBasedMatcher(index_params, search_params)
    matches = flann.knnMatch(np.asarray(des1, np.float32), np.asarray(des2, np.float32), k=2)
    good = []
    for m, n in matches:
        if m.distance < 0.75 * n.distance:  # Erhöhen, um genauere Übereinstimmungen zu erhalten
            good.append(m)
    if len(good) > MIN_MATCH_COUNT:
        src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
        dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)
        M, mask = cv.findHomography(src_pts, dst_pts, cv.RANSAC, 3.0)  # Verringern, um die Auswirkungen auf Linien zu minimieren
        matchesMask = mask.ravel().tolist()
        print("Matched " + str(file))
        flag = 1
    else:
        matchesMask = None

    draw_params = dict(matchColor=(0, 255, 0),
                       singlePointColor=None,
                       matchesMask=matchesMask,
                       flags=2)

    img3 = cv.drawMatches(img1, kp1, img2, kp2, good, None, **draw_params)
    cv.imshow("Match", img3)
    cv.waitKey(0)
    cv.destroyAllWindows()

if flag == 0:
    print("No Matches among the given set!!")
else:
    print("Fingerprint Matched!")
