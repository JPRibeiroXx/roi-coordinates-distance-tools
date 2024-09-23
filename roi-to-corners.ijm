// Clear any existing data in the Results Table
run("Clear Results");

// Get the number of ROIs in the ROI Manager
n = roiManager("count");

// Get image calibration
getPixelSize(unit, pixelWidth, pixelHeight);

// Loop through each ROI and populate the Results Table
for (i = 0; i < n; i++) {
    roiManager("select", i);
    getSelectionBounds(x, y, width, height);

    // Calculate corner coordinates in pixel units
    x1 = x;           // Top-left X
    y1 = y;           // Top-left Y
    x2 = x + width;   // Top-right X
    y2 = y + height;  // Bottom Y (same for bottom-left and bottom-right)

    // Convert pixel coordinates to micrometer units
    x1_cal = x1 * pixelWidth;
    y1_cal = y1 * pixelHeight;
    x2_cal = x2 * pixelWidth;
    y2_cal = y2 * pixelHeight;

    // Add entries to the Results Table
    roiIndex = i; // Results Table rows start from 0

    setResult("ROI", roiIndex, i + 1); // ROI numbering starts from 1 for display

    // Top-left corner
    setResult("Top-left X (" + unit + ")", roiIndex, x1_cal);
    setResult("Top-left Y (" + unit + ")", roiIndex, y1_cal);

    // Top-right corner
    setResult("Top-right X (" + unit + ")", roiIndex, x2_cal);
    setResult("Top-right Y (" + unit + ")", roiIndex, y1_cal);

    // Bottom-left corner
    setResult("Bottom-left X (" + unit + ")", roiIndex, x1_cal);
    setResult("Bottom-left Y (" + unit + ")", roiIndex, y2_cal);

    // Bottom-right corner
    setResult("Bottom-right X (" + unit + ")", roiIndex, x2_cal);
    setResult("Bottom-right Y (" + unit + ")", roiIndex, y2_cal);
}

// Update and display the Results Table
updateResults();