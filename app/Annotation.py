import cv2
import os
import sys

def main():

    print("Application started")

    workspace = os.getenv("WORKSPACE", os.getcwd())
    print("WORKSPACE =", workspace)

    output_dir = os.path.join(workspace, "output")
    os.makedirs(output_dir, exist_ok=True)

    print("Output dir:", output_dir)

    img1 = cv2.imread("Tiger1.jpg")
    img2 = cv2.imread("Car2.jpg")

    if img1 is None or img2 is None:
        print("ERROR: Failed to read images")
        sys.exit(1)

    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    out1 = os.path.join(output_dir, "gray1.jpg")
    out2 = os.path.join(output_dir, "gray2.jpg")

    cv2.imwrite(out1, gray1)
    cv2.imwrite(out2, gray2)

    print("Saved:", out1)
    print("Saved:", out2)

if __name__ == "__main__":
    main()
