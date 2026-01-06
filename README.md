# Frequency Response Plotter (Bode & Nyquist)

A Python-based graphical tool for analyzing the frequency response of linear time-invariant (LTI) control systems. This application allows users to generate **Bode plots** and **Nyquist plots** through a simple and interactive GUI, making control system analysis more accessible for students, educators, and engineers.

---

## 📌 Overview

The Frequency Response Plotter enables users to define a transfer function using numerator and denominator coefficients and instantly visualize its frequency-domain behavior. In addition to plotting, the tool calculates and displays important stability metrics such as gain margin, phase margin, and crossover frequencies.

The project is designed to reduce the complexity of frequency response analysis while maintaining accuracy and educational value.

---

## ✨ Features

- Interactive GUI built with Tkinter  
- Supports Bode and Nyquist plots  
- Accepts arbitrary transfer function coefficients  
- Computes gain margin and phase margin  
- Displays gain and phase crossover frequencies  
- Uses industry-standard Python control libraries  

---

## 🛠️ Tech Stack

- **Python 3**
- **Tkinter** – GUI development  
- **NumPy** – numerical computations  
- **SciPy** – signal processing  
- **Python Control Systems Library** – control analysis  
- **Matplotlib** – plotting and visualization  

---

## 📂 Project Structure

frequency-response-plotter-gui/
│
├── controlfinal.py # Main application source code
├── README.md # Project documentation



---

## 🚀 Getting Started

### Prerequisites

Ensure you have Python 3.8 or higher installed on your system.

### Installation

Clone the repository:
git clone https://github.com/Demonking-13/frequency-response-plotter-gui.git
cd frequency-response-plotter-gui


Install the required dependencies:
pip install numpy scipy matplotlib control

---

## ▶️ Running the Application

Start the GUI application by running:

python controlfinal.py


The Frequency Response Plotter window will open.

---

## 🧪 Usage Guide

1. Enter the **numerator coefficients** of the transfer function (comma-separated).
2. Enter the **denominator coefficients** (comma-separated).
3. Provide a **system title**.
4. Select the plot type:
   - Bode Plot
   - Nyquist Plot
5. Click **Plot Frequency Response** to generate the output.

The console will display:
- Gain Margin (dB)
- Phase Margin (degrees)
- Gain Crossover Frequency
- Phase Crossover Frequency

---

## 📈 Example

For the transfer function:

G(s) = 1 / (s² + 3s + 2)

**Numerator Input**
1

**Denominator Input**
1,3,2

---

## 🎓 Use Cases

- Control systems education and labs  
- Frequency-domain system analysis  
- Stability analysis of LTI systems  
- Mini-project or academic demonstrations  
- Base application for advanced control tools  

---

## 🔮 Future Enhancements

- Root locus plotting  
- Step and impulse response analysis  
- Export plots as image files  
- Improved GUI error handling  
- Support for state-space models  

---

## 🤝 Contributing

Contributions are welcome. If you would like to improve this project, feel free to fork the repository and submit a pull request. Bug reports and feature requests can be opened as issues.

---

## 📄 License

This project is open-source and available under the MIT License.

---

## 👤 Author

**Devit Chowdhury**  
Aspiring Software Engineer 

---

⭐ If you find this project helpful, consider giving it a star on GitHub!



