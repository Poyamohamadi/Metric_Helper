# Metric Helper

Metric Helper is a simple desktop application built using **CustomTkinter** that allows users to convert values between different metric prefixes (e.g., femto, nano, kilo, mega, etc.). This tool is designed for ease of use and provides a clean, modern interface.

---

## Table of Contents

1. [Features](#features)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Structure](#structure)
5. [Dependencies](#dependencies)
6. [Contributing](#contributing)
7. [License](#license)

---

## Program Demo

![Metric Helper](https://github.com/Poyamohamadi/Metric_Helper/blob/main/demo.gif)

---

## Features

- **Metric Conversion**: Convert values between various metric prefixes ranging from `femto` (10⁻¹⁵) to `peta` (10¹⁵).
- **User-Friendly Interface**:
  - Input and output fields for entering and displaying values.
  - Dropdown menus (`ComboBox`) to select metric prefixes for both input and output.
- **Real-Time Conversion**: Click the "Convert" button to instantly calculate and display the converted value.
- **Modern Design**: Built with **CustomTkinter**, ensuring a sleek and professional look.

---

## Installation

### Prerequisites

- Python 3.7 or higher installed on your system.
- Install the required dependencies by running:

```bash
pip install customtkinter
```

### Clone the Repository

To get started, clone this repository to your local machine:

```bash
git clone https://github.com/Poyamohamadi/metric_helper.git
cd metric_helper
```

---

## Usage

1. Run the application by executing the Python script:

   ```bash
   python main.py
   ```

2. Enter a numeric value in the **Input Field**.
3. Select the metric prefix for the input value from the **Input ComboBox**.
4. Select the desired metric prefix for the output value from the **Output ComboBox**.
5. Click the **Convert** button to see the converted value in the **Output Field**.

---

## Structure

The code is organized into the following components:

1. **Main Application Class (`MyApp`)**:
   - Inherits from `customtkinter.CTk` to create the main application window.
   - Initializes the GUI elements such as input/output fields, comboboxes, and buttons.

2. **GUI Elements**:
   - **Input Field**: For entering the numerical value.
   - **Comboboxes**: Dropdown menus for selecting metric prefixes.
   - **Convert Button**: Triggers the conversion logic.
   - **Output Field**: Displays the converted value.

3. **Conversion Logic (`convert` Method)**:
   - Uses a dictionary (`metric_values`) to map metric prefixes to their respective powers of 10.
   - Converts the input value to its base unit and then to the desired output prefix.

4. **Main Execution Block**:
   - Ensures the application runs only when executed directly.

---

## Dependencies

- **Python**: Version 3.6 or higher.
- **customtkinter**: A modern GUI library for Python. Install it using:
  ```bash
  pip install customtkinter
  ```

---

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push them to your fork.
4. Submit a pull request detailing your changes.

Please ensure your code adheres to the existing style and includes appropriate documentation.

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](https://github.com/Poyamohamadi/Metric_Helper/blob/main/LICENSE.md) file for more details.

---

## Acknowledgments

- **CustomTkinter Library**: Thanks to the developers of `customtkinter` for creating a modern and customizable GUI toolkit.

- **Python Community**: Special thanks to the Python community for their support and resources.

---

## Contact

For questions or feedback, feel free to reach out:

- **GitHub**: [Poyamohamadi](https://github.com/Poyamohamadi)

---

Thank you for using **Metric Helper**! 😊
