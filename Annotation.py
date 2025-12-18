import cv2
import os

def main():
    img = cv2.imread(r"C:\Users\saivi\Downloads\Dog.jpg")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    if os.getenv("CI") == "true":
        # CI mode → save output instead of showing
        cv2.imwrite("output_gray.jpg", gray)
    else:
        # Local mode → show window
        cv2.imshow("grayscale image", gray)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
