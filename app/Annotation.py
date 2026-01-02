import cv2
import os

def main():
    img1 = cv2.imread(r"C:\Users\saivi\Downloads\Tiger.jpg")
    img2 = cv2.imread(r"C:\Users\saivi\Downloads\Car.jpg")

    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    workspace = os.getenv("WORKSPACE", os.getcwd())
    output_dir = os.path.join(workspace, "output")

    os.makedirs(output_dir, exist_ok=True)

    cv2.imwrite(os.path.join(output_dir, "output_gray1.jpg"), gray1)
    cv2.imwrite(os.path.join(output_dir, "output_gray2.jpg"), gray2)

    print(f"Images saved in: {output_dir}")

if __name__ == "__main__":
    main()
