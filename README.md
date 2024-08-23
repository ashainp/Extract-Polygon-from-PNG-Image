# Extract-Polygon-from-PNG-Image
This Python script extracts polygons from a PNG image based on a target color and converts them into vector polygons in QGIS. The polygons are added to a temporary vector layer with a specified CRS. Ideal for converting image data into spatial data for analysis.

**Features**
1. Target Color Extraction: Extracts polygons from a PNG image by detecting pixels of a specified color (e.g., purple).
2. Polygon Creation: Generates polygons from the detected pixels using the skimage library.
3. Spatial Adjustment: Translates and scales the extracted polygons to fit into a specific geographic area (e.g., Glenorchy, Tasmania).
4. Vector Layer Creation: Adds the extracted polygons to a temporary vector layer in QGIS with a specified CRS (GDA94 / MGA Zone 55, EPSG:28355).
5. Filtering by Size: Filters polygons based on a minimum size to ensure only meaningful geometries are included.

**Requirements**
1. QGIS with Python support
2. Libraries: numpy, PIL (Pillow), skimage

You can install the required Python libraries using pip
pip install numpy pillow scikit-image

**Installation**
1. Download or clone this repository.
2. Save the script as Extract_Polygon_from_PNG_Image.py.
3. Open the script in the QGIS Python console.

**Usage**
1. Modify the image_path variable in the script to point to your PNG image file.
2. Adjust the purple_colour variable to target the RGB color you want to extract from the image.
3. Set the translation and scaling factors to adjust the spatial placement of the extracted polygons as needed.
4. Run the script in the QGIS Python console.
5. The extracted polygons will be added as a temporary vector layer in QGIS, with CRS set to GDA94 / MGA Zone 55 (EPSG:28355).
6. Word file with simple example uploaded

**Example**
image_path = r"C:\path\to\your\imagename.png"
purple_colour = (160, 32, 240)  # RGB value for purple

Cheers
