# **Stock Selection Tool**

The Stock Selection Tool is a Python program designed to analyze historical stock closing prices for the Malaysian stock market. It includes features such as user registration, stock data retrieval, basic analysis, and interaction history storage.

---

## **Features**
- **User Registration and Login**: Secure authentication using email and password.
- **Stock Data Retrieval**: Fetch historical stock closing prices using YFinance.
- **Basic Analysis**:
  - Average Closing Price
  - Percentage Change
  - Highest and Lowest Closing Prices
- **Data Storage**: Save user interactions (email, stock ticker, and analysis results) in a CSV file.
- **View History**: Display previously saved data.

---

## **Setup Instructions**

### **1. Install Python**
1. Download and install **Python 3.8 or later** from [https://www.python.org/downloads/](https://www.python.org/downloads/).
2. During installation, ensure you check the box for **"Add Python to PATH"**.

### **2. Install Visual Studio Code**
1. Download and install **Visual Studio Code** from [https://code.visualstudio.com/](https://code.visualstudio.com/).

### **3. Clone the Repository**
1. Open a terminal or command prompt.
2. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/Karson719/stock-selection-tool.git
   cd stock-selection-tool

## **Enviroonment Setup**
1.  Open a terminal in the project directory.
2.  Install the necessary libraries:
     ```bash
        pip install pandas yfinance

Pandas: For data manipulation and CSV file operations.
YFinance: For fetching historical stock market data.

## **Project Structure**
The project consists of the following files:
 ```bash
    .
    ├── main.py              # Main script to run the program
    ├── functions.py         # Helper functions for registration, authentication, and analysis
    ├── user_credentials.csv # File to store user credentials (created automatically)
    ├── user_data.csv        # File to store user interaction data (created automatically)
    └── README.md            # Instructions for setup and usage

