from qgis.core import QgsVectorLayer, QgsFeature, QgsGeometry, QgsPointXY, QgsProject, QgsField
from qgis.PyQt.QtCore import QVariant
from PIL import Image
import numpy as np
from skimage import measure

# Load the image
image_path = r"C:\Users\enoks\Desktop\test qgis\24000_HOME\06 - Calculations\imagename.png"
image = Image.open(image_path)
pixels = np.array(image)

# Define the target colour for purple (RGB values)
purple_colour = (160, 32, 240)  # RGB value for purple

# Define a tolerance level
tolerance = 30

# Create a mask for the specified purple colour
purple_mask = np.all(np.abs(pixels[:, :, :3] - purple_colour) <= tolerance, axis=-1)

# Debugging: Check the number of matching pixels
print("Number of matching pixels:", np.sum(purple_mask))

# Create a function to generate polygons from the mask, filtering by size
def create_polygons_from_mask(mask, min_size=10):
    contours = measure.find_contours(mask, 0.5)
    print("Number of contours found:", len(contours))  # Debugging
    polygons = []

    # Apply a rough translation and scaling to place the polygons in Glenorchy
    translation_x = 525000  # Approximate UTM Easting for Glenorchy, Tasmania
    translation_y = 5250000  # Approximate UTM Northing for Glenorchy, Tasmania
    scale_factor = 5  # Reduced scale factor to improve accuracy

    for contour in contours:
        points = [QgsPointXY(point[1] * scale_factor + translation_x, 
                             point[0] * scale_factor + translation_y) for point in contour]
        if points:
            polygon = QgsGeometry.fromPolygonXY([points])
            if polygon.area() > min_size and polygon.isGeosValid():  # Check for validity
                polygons.append(polygon)
    
    return polygons

# Generate polygons from the purple mask, with a minimum size filter
min_polygon_size = 10  # Adjust this value based on your needs
polygons = create_polygons_from_mask(purple_mask, min_size=min_polygon_size)

# Create a vector layer to store the polygons as a temporary layer
# Set CRS to GDA94 / MGA zone 55 (EPSG:28355)
vector_layer = QgsVectorLayer("Polygon?crs=EPSG:28355", "Temporary Flood Extents", "memory")
provider = vector_layer.dataProvider()

# Add fields (for example, an ID field)
provider.addAttributes([QgsField("id", QVariant.Int)])
vector_layer.updateFields()

# Add features to the vector layer
for i, poly in enumerate(polygons):
    if poly.isGeosValid():  # Ensure the geometry is valid
        feature = QgsFeature()
        feature.setGeometry(poly)
        feature.setAttributes([i])
        provider.addFeature(feature)

# Update the layer's extents and add it to the current QGIS project
vector_layer.updateExtents()
QgsProject.instance().addMapLayer(vector_layer)

print("Temporary vector layer successfully added to the QGIS project with CRS GDA94 / MGA zone 55!")
