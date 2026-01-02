import cv2
import os

def main():
    img1 = cv2.imread(r"C:\Users\saivi\Downloads\Tiger.jpg")
    img2 = cv2.imread(r"C:\Users\saivi\Downloads\Car.jpg")
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)


    if os.getenv("CI") == "true":
        # CI mode → save output instead of showing
        cv2.imwrite(r"C:\Users\saivi\OneDrive\Pictures\Screenshots\output_gray1.jpg", gray1)
        cv2.imwrite(r"C:\Users\saivi\OneDrive\Pictures\Screenshots\output_gray2.jpg", gray2)

    else:
        # Local mode → show window
        cv2.imshow("grayscale image1", gray1)
        cv2.imshow("grayscale image2", gray2)
        cv2.imwrite(r"C:\Users\saivi\OneDrive\Pictures\Screenshots\dog_gray1.jpg", gray1)
        cv2.imwrite(r"C:\Users\saivi\OneDrive\Pictures\Screenshots\dog_gray2.jpg", gray2)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
