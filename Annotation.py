# Import dependencies
import cv2
# Read Images
img = cv2.imread(r"C:\Users\saivi\Downloads\Dog.jpg")
# Display Image
cv2.imshow('Original Image',img)
#cv2.waitKey(0)
# Print error message if image is null
if img is None:
    print('Could not read image')
# Draw line on image
imageLine = img.copy()
#Draw the image from point A to B
pointA = (200,80)
pointB = (450,80)
cv2.line(imageLine, pointA, pointB, (255, 255, 0), thickness=3, lineType=cv2.LINE_AA)
cv2.imshow('Image Line', imageLine)
cv2.imwrite(r"C:\Users\saivi\OneDrive\Pictures\Screenshots\image_line.jpg", imageLine)
#cv2.waitKey(0)
# Make a copy of image
imageCircle = img.copy()
imageFilledCircle = img.copy()
# define the center of circle
circle_center = (415,190)
# define the radius of the circle
radius =100
#  Draw a circle using the circle() Function
cv2.circle(imageCircle, circle_center, radius, (0, 0, 255), thickness=3, lineType=cv2.LINE_AA)
cv2.circle(imageFilledCircle, circle_center, radius, (0, 0, 255), thickness=-1, lineType=cv2.LINE_AA) 
# Display the result
cv2.imshow("Image Circle",imageCircle)
cv2.imshow("Image with Filled Circle",imageFilledCircle)
cv2.imwrite(r"C:\Users\saivi\OneDrive\Pictures\Screenshots\image_circle.jpg", imageCircle)
cv2.imwrite(r"C:\Users\saivi\OneDrive\Pictures\Screenshots\image_filledcircle.jpg", imageFilledCircle)
#cv2.waitKey(0)
# make a copy of the original image
imageRectangle = img.copy()
# define the starting and end points of the rectangle
start_point =(300,115)
end_point =(475,225)
# draw the rectangle
cv2.rectangle(imageRectangle, start_point, end_point, (0, 0, 255), thickness= 3, lineType=cv2.LINE_8) 
# display the output
cv2.imshow('imageRectangle', imageRectangle)
cv2.imwrite(r"C:\Users\saivi\OneDrive\Pictures\Screenshots\image_rectangle.jpg", imageRectangle)
#cv2.waitKey(0)
# make a copy of the original image
imageEllipse = img.copy()
imageHalfEllipse = img.copy()
# define the center point of ellipse
ellipse_center = (415,190)
# define the major and minor axes of the ellipse
axis1 = (100,50)
axis2 = (125,50)
# draw the ellipse
#Horizontal
cv2.ellipse(imageEllipse, ellipse_center, axis1, 0, 0, 360, (255, 0, 0), thickness=3)
#Vertical
cv2.ellipse(imageEllipse, ellipse_center, axis2, 90, 0, 360, (0, 0, 255), thickness=3)
# draw the Incomplete/Open ellipse, just a outline
cv2.ellipse(imageHalfEllipse, ellipse_center, axis1, 0, 180, 360, (255, 0, 0), thickness=3)
# if you want to draw a Filled ellipse, use this line of code
cv2.ellipse(imageHalfEllipse, ellipse_center, axis1, 0, 0, 180, (0, 0, 255), thickness=-2)
# display the output
cv2.imshow('ellipse Image',imageEllipse)
cv2.imshow('halfEllipse',imageHalfEllipse)
cv2.imwrite(r"C:\Users\saivi\OneDrive\Pictures\Screenshots\image_ellipse.jpg", imageEllipse)
cv2.imwrite(r"C:\Users\saivi\OneDrive\Pictures\Screenshots\image_half_ellipse.jpg", imageHalfEllipse)
cv2.waitKey(0)
