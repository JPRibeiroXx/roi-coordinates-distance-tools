# Rectangle ROI Distance Tools

This repository contains two main tools:

1. A **Python script** for calculating the minimum Euclidean distance between points and the perimeter of rectangular Regions of Interest (ROIs).
2. A **Fiji/ImageJ macro** for extracting the corner coordinates of selected rectangular ROIs.

## Table of Contents
- [Introduction](#introduction)
- [Python Script](#python-script)
  - [Requirements](#requirements)
  - [Usage](#usage)
  - [How It Works](#how-it-works)
- [Fiji Macro](#fiji-macro)
  - [How It Works](#how-it-works-1)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project aims to facilitate the extraction of coordinates from rectangular ROIs and compute the minimum distance between a set of points and the perimeter of the rectangular ROIs. The workflow is split between two components: a Python script and a Fiji macro.

- **Python Script**: Reads CSV files containing the ROIs and point coordinates, calculates the minimum Euclidean distance from each point to the perimeter of the rectangles, and outputs the results in a new CSV file.
- **Fiji Macro**: Takes selected rectangular ROIs in ImageJ or Fiji and converts them into corner coordinates for further processing.

## Python Script

### Requirements

Ensure you have the following Python packages installed before running the script:

```bash
pip install pandas numpy
```
### Usage

1. Create two separate CSV files for the point and the rectangle corner coordinates (see examples). If using the Fiji macro, these are automatically generated for you.
2. Run the script as follows:

```bash
python distance-tools.py
```
3. When prompted, select the required files containing the coordinates. A message will appear in the console stating which file you should select.
4. Select a name and save location for the output file.
5. The script will output the minimum distances between the points and the rectangle perimeter in a new CSV file, containing the point coordinates and the distance to the closest rectangle perimeter. If the point is inside a rectangle, distance is assumed as zero (0).

### How It Works

The Python script follows this flow:

1. **Read Input**: Uses Pandas to read an .csv file. It then extracts the coordinates for the rectangular ROIs and the points.
2. **Check Location**: For each point, the script detects whether it is located inside any of the given rectangles. If so, it returns a distance value of zero (0).
3. **Calculate Euclidean Distance**: For each point not inside a rectangle, the script computes the Euclidean distance to the perimeter of each rectangle, then stores the minimum distance for each point.
4. **Save Results**: The script saves the computed minimum distances to a new CSV file for further analysis.

**CSV File Structure**

To run the Python script correctly, the input CSV files must follow specific structures for both the **Rectangle Corners** and the **Points Coordinates**.

**Rectangle Corners CSV Structure**

The CSV file for rectangle corners should contain the following columns, where each row represents the coordinates of the four corners of a rectangle:

| ROI_X1 | ROI_Y1 | ROI_X2 | ROI_Y2 | ROI_X3 | ROI_Y3 | ROI_X4 | ROI_Y4 |
|--------|--------|--------|--------|--------|--------|--------|--------|
|   10   |   20   |   50   |   20   |   50   |   70   |   10   |   70   |
|   ...  |   ...  |   ...  |   ...  |   ...  |   ...  |   ...  |   ...  |

**Points Coordinates CSV Structure**

The CSV file for points coordinates should contain the following columns, where each row represents the X and Y coordinates of a point for which the distance to the rectangle perimeter will be calculated:

| Point_X | Point_Y |
|---------|---------|
|    15   |    25   |
|    ...  |    ...  |

You can find examples here:

- **Rectangle Corners CSV**: [Rectangle Corners CSV](RectangleCorner_Coordinates.csv)
- **Points Coordinates CSV**: [Points Coordinates CSV](Points_Coordinates.csv)

Both CSV files should be placed in the same directory as the Python script for processing. You can use these as templates.
The script will extract these columns and calculate the minimum distance from each point to its corresponding rectangle.

**Output CSV structure**

The CSV file containing the calculated distances contains the coordinate of a given point followed by its distance to the nearest rectangle, as such:

| Point_X | Point_Y | Distance |
|---------|---------|----------|
|    10   |    20   |   0.201  |
|   ...   |   ...   |    ...   |

## Fiji Macro

### How It Works

1. **ROI Selection**: The macro takes the selected rectangular ROIs within Fiji/ImageJ.
2. **Corner Extraction**: It converts each ROI into the coordinates of its four corners (X1, Y1, X2, Y2, X3, Y3, X4, Y4).
3. **Output**: The corner coordinates are printed or exported for use in the Python script.

To use the macro:
1. Open your image in Fiji.
2. Select the rectangular ROIs you wish to process.
3. Run the macro (`roi-to-corners.ijm`), and it will output the corner coordinates of the selected ROIs.

## Project Structure

```bash
.
├── distance-tools.py        # Python script for distance calculations
├── roi-to-corners.ijm       # Fiji macro for extracting corner coordinates
└── README.md                # This README file
```
## Contributing

This project was contributed to in equal parts by:
- **JPRibeiroXx** (ORCID: [0000-0002-1206-6774](https://orcid.org/0000-0002-1206-6774))
- **DavidLFRodrigues** (ORCID: [0000-0001-5459-5052](https://orcid.org/0000-0001-5459-5052))

Contributions from others are welcome! Please fork the repository and submit a pull request for any improvements or new features. Ensure that your contributions are well-documented.

## License and Usage

This project is licensed under the MIT License, with the following additional requirement:

Usage of this code is permitted as long as:
1. The repository is mentioned and linked.
2. The authors' ORCIDs are credited:
   - JPRibeiroXx (ORCID: [0000-0002-1206-6774](https://orcid.org/0000-0002-1206-6774))
   - DavidLFRodrigues (ORCID: [0000-0001-5459-5052](https://orcid.org/0000-0001-5459-5052))

For more details, see the [LICENSE](LICENSE) file.




