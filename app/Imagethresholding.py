# import opencv 
import cv2 
import os

def main():
    # Read image 
    src = cv2.imread(r"C:\Users\saivi\Downloads\Numbers.jpg", cv2.IMREAD_GRAYSCALE) 
    
    # Basic threshold example 
    th, dst = cv2.threshold(src, 0, 255, cv2.THRESH_BINARY); 
    if os.getenv("CI") == "true":
        cv2.imwrite(r"C:\Users\saivi\OneDrive\Pictures\Screenshots\opencv-threshold-numbers-example.jpg", dst)
    else:
        cv2.imshow('Basic_Threshold', dst)
        cv2.imwrite(r"C:\Users\saivi\OneDrive\Pictures\Screenshots\opencv-threshold-example.jpg", dst)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
