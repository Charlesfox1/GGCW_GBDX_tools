![alt text][header]

[header]: https://github.com/krakchris/GGCW_GBDX_tools/blob/master/header.PNG "header"


# GGCW_toolbox
[![licence](https://img.shields.io/badge/Licence-GPL%203.0-green.svg)](https://github.com/krakchris/GGCW_GBDX_tools/blob/master/LICENSE)

Toolbox for python that can be used on the Digital Globe GBDX platform

This toolbox was developed during the Digital Globe GBDX for Sustainability Challange.
Global Green City Watch aimed at using Very High Resolution Imagery for the assessment of quality green space in urban environments.
Tools that were developed were used on jupyter notebooks on the [GBDX platform](https://notebooks.geobigdata.io) but can also be executed on regular Python installations when the GBDX API is installed.

The toolbox contians three notebooks that run trough a approach using Openstreetmap polygons as training data for sklearn classifiers. 

![alt text][flowchart]

[flowchart]: https://github.com/krakchris/GGCW_GBDX_tools/blob/master/GGCW_tools_flowchart.PNG "GGCW_GBDX flowchart"

## Website
For actual information on the status of the project please visit [Our Website](http://www.globalgreencitywatch.org)

## Folder Structure

### Functions
This folder contains the functions used within the main script.

**classification_tools.py**   -   This function queries the gbdx.vector service for OSM objects within each selected park. It returns a 
                              dataframe with the available amenities within the park.

**get_classifier_rt.py**      -   This function was used for the classification of different land coves within each park


**get_OSM_Amenities.py**      -   This function queries the gbdx.vector service for OSM objects within each selected park. It returns a 
                              dataframe with the available amenities within the park.

**get_OSM_polygons.py**       -   This function queries the gbdx.vector service for OSM objects within each selected city. It returns  
                              shapes for all the parks within the city bounding box.

**nice_functions.py**         -   This function contains some checks that were needed for projections and metadata.

**Somefunctions.py**          -   This function is a group of fuctions used to query and load imagery for the calculation of NDVI values within                               each park for summer and winter 

**Watertools.py**             -    This function is a group of functions used to identify and deliniate water objects within parks and find the 
                               riparian zone around these water bodies.

### Pickle
This folder contains the pickled classifiers trained for each study area.

### Scripts
This folder contains the main script that was used for the calculation

### Wkt_files
This folder contains the wkt files containing the outline of the city borders for Tokyo, Rio de Janeiro, Amsterdam and Houston


