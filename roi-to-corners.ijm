// Clear any existing data in the Results Table
run("Clear Results");

// Get the number of ROIs in the ROI Manager
n = roiManager("count");

// Get image calibration
getPixelSize(unit, pixelWidth, pixelHeight);

// Loop through each ROI and populate the Results Table
for (i = 0; i < n; i++) {
    roiManager("select", i);

    // Get the x and y coordinates of the selection
    getSelectionCoordinates(xpoints, ypoints);

    // Number of points
    n_points = xpoints.length;

    // Initialize arrays to hold calibrated coordinates
    x_cal = newArray(n_points);
    y_cal = newArray(n_points);

    // Convert pixel coordinates to calibrated units
    for (j = 0; j < n_points; j++) {
        x_cal[j] = xpoints[j] * pixelWidth;
        y_cal[j] = ypoints[j] * pixelHeight;
    }

    // Compute centroid of the ROI
    x_centroid = 0;
    y_centroid = 0;
    for (j = 0; j < n_points; j++) {
        x_centroid += xpoints[j];
        y_centroid += ypoints[j];
    }
    x_centroid /= n_points;
    y_centroid /= n_points;

    // Compute angles from centroid to each point
    angles = newArray(n_points);
    for (j = 0; j < n_points; j++) {
        dx = xpoints[j] - x_centroid;
        dy = ypoints[j] - y_centroid;
        angles[j] = atan2(dy, dx);
        // Adjust angles to range from 0 to 2*PI
        if (angles[j] < 0) {
            angles[j] += 2 * PI;
        }
    }

    // Define corner labels and corresponding angles
    corner_labels = newArray("Top-left", "Top-right", "Bottom-right", "Bottom-left");
    corner_angles = newArray(3*PI/4, PI/4, 7*PI/4, 5*PI/4);

    // Map each corner to the closest angle
    corner_indices = newArray(4); // To store indices of points corresponding to corners
    for (k = 0; k < 4; k++) {
        min_diff = 2*PI;
        min_index = -1;
        for (j = 0; j < n_points; j++) {
            diff = abs(angles[j] - corner_angles[k]);
            if (diff > PI) {
                diff = 2*PI - diff;
            }
            if (diff < min_diff) {
                min_diff = diff;
                min_index = j;
            }
        }
        corner_indices[k] = min_index;
    }

    // Add entries to the Results Table
    roiIndex = i; // Results Table rows start from 0
    setResult("ROI", roiIndex, i + 1); // ROI numbering starts from 1 for display

    // For each corner, add the coordinates
    for (k = 0; k < 4; k++) {
        index = corner_indices[k];
        label = corner_labels[k];
        x_coord = x_cal[index];
        y_coord = y_cal[index];
        setResult(label + " X (" + unit + ")", roiIndex, x_coord);
        setResult(label + " Y (" + unit + ")", roiIndex, y_coord);
    }
}

// Update and display the Results Table
updateResults();
