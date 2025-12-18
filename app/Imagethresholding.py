import cv2
import os

def main():
    src = cv2.imread("images/Numbers.jpg", cv2.IMREAD_GRAYSCALE)

    if src is None:
        print("ERROR: Source image not found")
        return

    th, dst = cv2.threshold(src, 0, 255, cv2.THRESH_BINARY)

    # Decide output path
    if os.getenv("CI") == "true":
        output_path = "opencv-threshold-numbers-example.jpg"
    else:
        output_path = "opencv-threshold-example.jpg"
        cv2.imshow("Basic_Threshold", dst)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    cv2.imwrite(output_path, dst)
    print(f"Saved output to: {os.path.abspath(output_path)}")

if __name__ == "__main__":
    main()
