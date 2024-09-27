# Parallel Image Processing

This project implements both serial and parallel convolution of images using the Sobel filter. It allows users to process images either one by one (serially) or in batches (in parallel) and compares the performance of both methods. This can be particularly useful in understanding the speedup achieved through parallel processing in image analysis tasks.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Running the Project](#running-the-project)
- [Input Instructions](#input-instructions)
- [Output](#output)
- [License](#license)

## Prerequisites

Before you begin, ensure you have Python 3.x installed on your system. Additionally, you will need to install the following libraries:

- OpenCV: For image processing tasks.
- NumPy: For numerical operations.

You can install these libraries using pip. Open your terminal or command prompt and run:

pip install opencv-python numpy

## Project Structure
Parallel_PrelimExam_Lisondato/
├── main.py                  # Main script to run the image processing
├── parallel_convolution.py   # Module for parallel image processing
├── serial_convolution.py     # Module for serial image processing
└── dog_train/               # Folder containing images for processing

## Getting Started
1. Clone the Repository: Open your terminal and run the following command to clone the repository to your local machine:
   git clone https://github.com/ejieboy134201/Parallel_PrelimExam_Lisondato.git
2. cd Parallel_PrelimExam_Lisondato
3. pip install opencv-python numpy

## Running the project
### You can run this on terminal by:
python main.py


### Input Instructions
You will first be prompted to enter the number of iterations you want to perform. This allows you to test the processing with different configurations.
For each iteration, you will be asked to specify how many images to process from the specified folder.

### Output
The program will display a results table in the console with the following columns:

**Iteration**: The number of the current iteration.<br>
**Images**: The number of images processed in that iteration.<br>
**Serial Time (ms)**: The time taken to process the images serially (in milliseconds).<br>
**Parallel Time (ms)**: The time taken to process the images in parallel (in milliseconds).<br>
**Speedup**: The factor by which parallel processing is faster than serial processing, calculated as serial time divided by parallel time.<br>

# License
### Summary of the README

1. **Project Title and Description**: Clearly states the project's purpose and functionality.
2. **Table of Contents**: Provides quick navigation links to sections of the document.
3. **Prerequisites**: Lists software requirements and installation instructions.
4. **Project Structure**: Outlines the directory and file structure for clarity.
5. **Getting Started**: Detailed steps for cloning the repository and installing dependencies.
6. **Running the Project**: Instructions on how to execute the main script.
7. **Input Instructions**: Guidance on what the user will be prompted to enter.
8. **Output**: Explanation of the results displayed after processing.
9. **License**: Information regarding the project's licensing.

### Next Steps

1. **Create a `README.md` file**: Use the text above to create the file in your project directory.
2. **Commit and Push Changes**: Run the following commands to add and push your `README.md` to your GitHub repository:

```bash
git add README.md
git commit -m "Add README file with detailed instructions"
git push origin master
