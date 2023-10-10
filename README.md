# Bible_png
![Screenshot](BIBLE.png)

This Python script visualizes textual data of the King James Bible, which is obtained from Project Gutenberg, by mapping each unique word in a text to a unique RGB color and creating an image from these colors. 

## How to Use
Clone this repository, then install the dependencies using pip:
```
pip install -r requirements.txt
```
Next, just run the script, which will create the BIBLE.png file:
```
python3 Bible_png.py
```

## Customization
If you want to use a different text, you can modify the URL variable to point to a different text file. Make sure to also update the TXT_START and TXT_END variables to match the start and end markers of the book content in the new text file.
