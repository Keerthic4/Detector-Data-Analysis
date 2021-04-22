# Detector_Data_ Analysis & Reporting_Web_App_Project:
This project deals with new kinds of detector data, namely, motion detection data. The app mainly focus on displaying certain key graphs of the data and providing short blurbs describing the data and providing some analysis.

## Dataset
3 motion detection data sets, each with their own format as follows:

1. Detector 1: Each time this detector is triggered the detection is saved as a file with the date & time recorded as part of the file name. The dataset provided is an index file containing a list of all detection files' details. The size of each file is also included. Note that the files with sizes less than 50KB are false detection and should be removed.Detector 1 is in the form txt file. The columns of the dataset are as follows:

          • size: the size, in bytes, of the detection file

          • month: the month of detection

          • day: the day of detection

          • time: the time of day of detection

          • filename: the name of the detection file it's referring to (contains the  timestamp in format # - ## - YYYYMMDDHHMMSS)

2. Detector 2: Each time this detector is triggered it records a timestamp record of the event. Detector 2 is in the form txt file. The dataset columns are as follows:

          • date:  the date of detection in YYYY-MM-DD format

          • time:  the time of detection in HH:MM:SS format

3. Detector 3: This is the most interesting. Each time this detector is triggered it stores the detection data in a new txt file. The name of each file is the date of detection (with varying degrees of precision). The first line of each txt file may also contain a more precise date than that in the filename. Within each file you'll find the values corresponding to the time, in seconds, that have passed since the detector was triggered.

## Detector data analysis:

Converted the datasets into data frames with a uniform format (data wrangling, data cleaning etc.). Plotting the hourly distribution for each detector shows us that, in general, the detectors peak in the afternoon and are much less likely to be triggered during the night and early morning which may implicate that the triggering objects are biological in nature (or tied to the day-night cycle). Through Hourly analysis we find that data sets overlap in counts per datetime bucket.So identifed that there are correlations by Pearson's method, it means that the detectors are detecting in the same area. We understand visualization is generally easier to understand than reading tabular data, so here we use heatmaps to visualize correlation matrices. Here we are mainly using four libraries- pandas, numpy, seaborn and matplotlib.pyplot. For finding lowest time resolution, we can study further the detection in the pairs.

## Application of Dash to create a dashboard from Plotly graphs and deployment on GCP

1. Detector data was analyzed and Plotly was used to create dynamic charts. The complete analysis can be found in notebooks.
2. Dash enabled us to view few selected Plotly graphs in a web page.
3. Finally, Dash web page was Deployed on Google Cloud Platform (GCP).
