import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.feature import hessian_matrix, hessian_matrix_eigvals

def detect_ridges(gray, sigma=3.0):
	#This function uses the Hessian matrix to detect edges (ridges) in a grayscale image.
	H_elems = hessian_matrix(gray, sigma=sigma, order='rc')
	maxima_ridges, minima_ridges = hessian_matrix_eigvals(H_elems)
	return maxima_ridges, minima_ridges

def plot_images(*images): 
	#This function is used to display and save images. 
	#It creates a figure with the specified images and saves them as PNG files.
	images = list(images)
	n = len(images)
	fig, ax = plt.subplots(ncols=n, sharey=True)
	for i, img in enumerate(images):
		ax[i].imshow(img, cmap='gray')
		ax[i].axis('off')
		extent = ax[i].get_window_extent().transformed(fig.dpi_scale_trans.inverted())
		plt.savefig('fig'+str(i)+'.png', bbox_inches=extent)
	plt.subplots_adjust(left=0.03, bottom=0.03, right=0.97, top=0.97)
	plt.show()




def main(): #This is the main function of the script, where different image processing steps are performed.

	# -------------------------- Step 1: import the image whose background has been removed ----------
	# Step 1: The input image is loaded using cv2.imread. 
	# This image should already have its background removed, as indicated in a previous step in the code.

	img = cv2.imread("input.jpg",1)


	# -------------------------- Step 2: Sharpen the image -------------------------------------------
	# Step 2: The image is sharpened using a sharpening kernel to enhance edges.
	kernel = np.array([[-1,-1,-1], 
                   [-1, 9,-1],
                   [-1,-1,-1]])
	sharpened = cv2.filter2D(img, -1, kernel)
	# cv2.imshow("sharpened",sharpened)


	# --------------------------- Step 3: Grayscale the image------------------------------------------
	# Step 3: The sharpened image is converted to grayscale.
	gray = cv2.cvtColor(sharpened,cv2.COLOR_BGR2GRAY)
	# cv2.imshow("gray",gray)


	# --------------------------- Step 4: Perform histogram equilisation ------------------------------
	# Step 4: Histogram equalization is applied to the grayscale image to enhance contrast.
	hist,bins = np.histogram(gray.flatten(),256,[0,256])
	cdf = hist.cumsum()
	cdf_normalized = cdf * hist.max()/ cdf.max()

	cdf_m = np.ma.masked_equal(cdf,0)
	cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
	cdf = np.ma.filled(cdf_m,0).astype('uint8')

	img2=cdf[gray]
	# cv2.imshow("histogram",img2)
	# cv2.imwrite('hist.jpeg',img2)


	# ----------------------------- Step 5: Ridge detection filter ------------------------------------
	#Step 5: The detect_ridges function is called on the processed image to detect edges, 
	# and the results are displayed using plot_images.
	#sigma = 2.7
	a, b = detect_ridges(img2, sigma=2.7)
	plot_images(a, b)


	# ----------------------------- Step 6: Convert image to binary image -----------------------------
	# Step 6: The result image from Step 5 is converted into a binary image, 
	# and various image processing steps are applied.
	img = cv2.imread('fig1.png',0)
	# cv2.imshow("img",img)
	bg = cv2.dilate(img,np.ones((5,5),dtype=np.uint8))
	bg = cv2.GaussianBlur(bg,(5,5),1)
	# cv2.imshow("bg",bg)
	src_no_bg = 255 - cv2.absdiff(img,bg)
	# cv2.imshow("src_no_bg",src_no_bg)
	ret,thresh = cv2.threshold(src_no_bg,240,255,cv2.THRESH_BINARY)
	cv2.imshow("threshold",thresh)


	# --------------------------- Step 7: Thinning / Skeletonizing Algorithm ----------------------------
	# Step 7: A thinning or "Thinning" operation is performed on the binary image, 
	# and the result is displayed and saved as "trial-out.png."
	thinned = cv2.ximgproc.thinning(thresh)
	cv2.imshow("thinned",thinned)
	cv2.imwrite("./trial-out.png",thinned)

	cv2.waitKey(0)
	cv2.destroyAllWindows()

if __name__=='__main__':
	main()