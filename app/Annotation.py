import cv2
import os
import sys

def main():
    workspace = os.getenv("WORKSPACE")

    if not workspace:
        print("ERROR: WORKSPACE not found")
        sys.exit(1)

    print("Using workspace:", workspace)

    output_dir = os.path.join(workspace, "output")
    os.makedirs(output_dir, exist_ok=True)

    img1 = cv2.imread(r"C:\Users\saivi\Downloads\Tiger.jpg")
    img2 = cv2.imread(r"C:\Users\saivi\Downloads\Car.jpg")

    if img1 is None or img2 is None:
        print("ERROR: Image read failed")
        sys.exit(1)

    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    out1 = os.path.join(output_dir, "output_gray1.jpg")
    out2 = os.path.join(output_dir, "output_gray2.jpg")

    cv2.imwrite(out1, gray1)
    cv2.imwrite(out2, gray2)

    print("Saved:", out1)
    print("Saved:", out2)

if __name__ == "__main__":
    main()
