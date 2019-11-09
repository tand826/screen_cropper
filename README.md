# screen_cropper
Manually crop the screen or the whiteboard or etc. from an image with GUI of matplotlib.

# Example
<img src="https://raw.githubusercontent.com/tand826/screen_cropper/master/img/lena.png" height=200px>
<img src="https://raw.githubusercontent.com/tand826/screen_cropper/master/img/cropping.png" height=200px>
<img src="https://raw.githubusercontent.com/tand826/screen_cropper/master/img/lena_cropped.png" height=200px>

# How To Use

- Install the requirements

```python: Installation
pip install -r requirements.txt
```

- Run the script like below

```python: Run
python cropper.py img/lena.png --outdir img --width 200 --height 200
```

- And just click 4 points of the corners.
    - You don't have to care about its order.

# Arguments
| name   | default    | Example  | Description  |
| ----   | ----       | ----     | ---- |
| input  | Positional | abc      | Path to the input image or the directory which contains input images.  |
| outdir | "."        | out_pics | Path to save the output image.  |
| width  | 1600       | 800      | Width of the output image.  |
| height | 900        | 600      | Height of the output image.  |

