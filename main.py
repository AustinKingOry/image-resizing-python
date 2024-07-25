from PIL import Image
import os
import argparse

def resize_image(file_path,sizes:list[int] | None = None):
    '''
    Creates a new directory; **(resized)**, in the parent directory of the image. It then creates another directory inside "resized" with the name of the image, where it the stores the resized images.
    
    Parameters:
        :param file_path: A filename (list[str]).
        The absolute path of the file; image file.

        :param (optional) sizes: (list[int]).
        A list of sizes to be used as width and height (in pixels). E.g 20 will create a resized 20px by 20px image.
    '''
    try:
        # Resize the image to multiple sizes
        sizes_to_generate = [20, 100, 300, 500] if sizes is None else sizes
        mime_type = 'image'
        # Get the directory of the original media file
        media_directory = os.path.dirname(file_path)
        resized_directory = os.path.join(media_directory, "resized")
        # get the filename of the image without the extension part
        new_filename = f"{os.path.splitext(os.path.basename(file_path))[0]}"
        if mime_type.lower() == 'image':
            try:
                os.makedirs(resized_directory, exist_ok=True)
                # create a new directory inside resized that has the name of the file
                new_file_directory = os.path.join(resized_directory, new_filename)
                os.makedirs(new_file_directory, exist_ok=True)
                # Open the image using PIL
                image = Image.open(file_path)
                # Check if the image has an alpha channel (transparency)
                if 'A' in image.getbands():
                    # Convert the image to RGB mode (removing alpha channel)
                    image = image.convert('RGB')
                for size in sizes_to_generate:
                    resized_image = image.resize((size, size))
                    resized_image_path = os.path.join(new_file_directory, f"{new_filename}_{size}px.jpg")
                    # Save the resized image to the image path
                    resized_image.save(resized_image_path)
                return None
            except Exception as e:
                # Handle any exceptions that might occur during image generation
                print(f"Error resizing image: {e}")
                return None
    except FileNotFoundError as e:
        print(f"Error Accessing File: {e}")
    except Exception as e:
        print(f"Error: {e}")
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Reduce the size of an image by scale using the Pillow package.")
    parser.add_argument("file_path", type=str, help="Absolute path to the file (image) to be resized.")
    
    args = parser.parse_args()
    resize_image(args.file_path)