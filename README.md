# GIS_Demos
Simple spatially explicit models for presentations, usually written as QGIS plugins. Organized by name. 

Please note: These models are simplistic and generally use made-up parameters and data. Please consult an expert before making any decisions. Neither myself nor these models are an expert.

## TreeDiseases
Model predicts the spread of tree diseases, one year at a time. Generate a QGIS plugin using the included code and create a points file in QGIS. The points file should have one attribute for ID and a second attribute called 'status'. 'status' should be 0 for healthy trees, 1 for infected trees, and 2 for dead trees.

Trees will become infected based on a separate 20% chance of catching the pathogen from an infected tree and 0% chance of catching the pathogen from a healthy or dead tree, for each of up to 10 trees within a 1 km radius. 

Trees will die based on a 20% chance of death per year if they are infected or a 0% chance of death per year if they are healthy or dead.
