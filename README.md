# Image Resizing with Pillow (Py imaging library)

I wrote this code to help me reduce the size of images as I used them on web projects for easier user experience during load time.

When called, the program creates a new directory; **(resized)**, in the parent directory of the image. It then creates another directory inside "resized" with the name of the image, where it the stores the resized images.

## Dependencies
- Pillow
```bash
pip install pillow
```

## Parameters
**file_path:**
- type: list[str] <br/>
The absolute path of the file; image file.

**sizes (optional):**
- type: list[int] <br/>
A list of sizes to be used as width and height (in pixels). E.g 20 will create a resized 20px by 20px image.

### Example
Let's resize the default image on this directory.
```python
resize("default.png",[20,50,100])
```
- Calling the resize function with those parameters will create 3 images (20px by 20px, 50px by 50px, 100px by 100px) resized from the default.png image.
