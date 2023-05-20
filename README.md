# Bible_png
![Screenshot](BIBLE.png)

This Python script visualizes textual data of the King James Bible, which is obtained from Project Gutenberg, by mapping each unique word in a text to a unique RGB color and creating an image from these colors. 

If you ever wondered what is the color of God, it's `RGB 0, 196, 24`.

## How to Use
Clone this repository, then install the dependencies using pip:
```
pip install pillow requests numpy
```
Next, just run the script, it will automatically create the BIBLE.png file:
```
python3 Bible_png.py
```

## Customization
If you want to use a different text, you can modify the URL variable to point to a different text file. Make sure to also update the TXT_START and TXT_END variables to match the start and end markers of the book content in the new text file.
