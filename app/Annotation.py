import cv2
import os
import sys

def run():

    workspace = os.getenv("WORKSPACE", os.getcwd())
    print("WORKSPACE =", workspace)

    output_dir = os.path.join(workspace, "output")
    os.makedirs(output_dir, exist_ok=True)

    print("Output dir:", output_dir)

    img1_path = os.path.join(workspace, "Tiger1.jpg")
    img2_path = os.path.join(workspace, "Car2.jpg")

    if not os.path.exists(img1_path) or not os.path.exists(img2_path):
        raise FileNotFoundError("One or more images are missing")

    img1 = cv2.imread(img1_path)
    img2 = cv2.imread(img2_path)

    if img1 is None or img2 is None:
        raise FileNotFoundError("Images exist but could not be read")

    print("Images loaded successfully")

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
