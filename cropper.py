from pathlib import Path
import matplotlib.pyplot as plt
import cv2
import numpy as np
import argparse


def main(args):
    root = Path(args.input)
    if root.is_file():
        convert(str(root))
    elif root.is_dir():
        for ext in [".jpg", ".JPG", ".png", ".PNG"]:
            for path in sorted(list(root.glob(f"*{ext}"))):
                convert(str(path))


def convert(path):
    img = plt.imread(path)
    fig = plt.figure(dpi=200)
    ax = fig.add_subplot(111)
    ax.imshow(img)
    plots_input = plt.ginput(n=4, mouse_add=1)
    plots_input = np.array(plots_input, dtype=np.float32)
    plt.close(fig)

    # Align the coordinates to fix for "plot_to".
    left = np.argsort(plots_input[:, 0], axis=0)[0:2]
    top, bottom = np.argsort(plots_input[left, 1])
    topleft = plots_input[left][top]
    bottomleft = plots_input[left][bottom]

    right = np.argsort(plots_input[:, 0], axis=0)[2:4]
    top, bottom = np.argsort(plots_input[right, 1])
    topright = plots_input[right][top]
    bottomright = plots_input[right][bottom]

    plots_from = np.array([topleft, bottomleft, bottomright, topright])

    h, w = (args.height, args.width)
    plots_to = np.array([(0, 0),
                         (0, h),
                         (w, h),
                         (w, 0)], dtype=np.float32)
    mat = cv2.getPerspectiveTransform(plots_from, plots_to)
    warped = cv2.warpPerspective(img, mat, (w, h))
    if warped.max() <= 1:
        warped *= 255
    warped_bgr = cv2.cvtColor(warped, cv2.COLOR_RGB2BGR)
    save_as = f"{args.outdir/Path(path).stem}_cropped{Path(path).suffix}"
    cv2.imwrite(str(save_as), warped_bgr)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("input")
    parser.add_argument("--outdir", default=".", type=Path)
    parser.add_argument("--width", default=1600, type=int)
    parser.add_argument("--height", default=900, type=int)
    args = parser.parse_args()
    main(args)
