import yfinance as yf
import pandas as pd
from functions import register_user, authenticate_user, get_closing_prices, analyze_closing_prices, save_to_csv, read_from_csv

CREDENTIALS_FILE = "user_credentials.csv"
USER_DATA_FILE = "user_data.csv"

def main():

    print("Welcome to the Stock Selection Tool!")

    while True:
        print("\nOptions:")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Please choose an option (1/2/3): ")

        if choice == '1':
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            if register_user(email, password, CREDENTIALS_FILE):
                print("Registration successful!")
            else:
                print("This email is already registered.")

        elif choice == '2':
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            if authenticate_user(email, password, CREDENTIALS_FILE):
                print("Login successful!")

                while True:
                    # After successful login, show additional options
                    print("\nOptions:")
                    print("1. Stock Data Retrieval and Analysis")
                    print("2. View Saved Data")
                    print("3. Logout")
                    choice = input("Please choose an option (1/2/3): ")

                    if choice == '1':
                        # Stock data retrieval and analysis
                        print("\nPlease input the stock ticker, start date, and end date to perform the analysis.")
                        ticker = input("Enter the stock ticker (e.g. 1155.KL): ")
                        start_date = input("Enter the start date (YYYY-MM-DD): ")
                        end_date = input("Enter the end date (YYYY-MM-DD): ")

                        # Get closing prices for the given stock and period
                        closing_prices = get_closing_prices(ticker, start_date, end_date)

                        if closing_prices.empty:
                            print(f"Could not retrieve data for {ticker}. Please try again.")
                            continue

                        # Perform analysis
                        analysis_results = analyze_closing_prices(closing_prices)

                        # Display results
                        print("\nAnalysis Results:")
                        for key, value in analysis_results.items():
                            print(f"{key}: {value}")

                        # Save interaction to CSV
                        save_data = {
                            "email": email,
                            "ticker": ticker,
                            "start_date": start_date,  
                            "end_date": end_date,      
                            "Average Closing Price": analysis_results["Average Closing Price"],
                            "Percentage Change": analysis_results["Percentage Change"],
                            "Highest Closing Price": analysis_results["Highest Closing Price"],
                            "Lowest Closing Price": analysis_results["Lowest Closing Price"]
                        }
                        save_to_csv(save_data, USER_DATA_FILE)

                        # Ask if the user wants to explore more stocks
                        cont = input("\nDo you want to explore another stock? (yes/no): ").lower()
                        if cont != 'yes':
                            break


                    elif choice == '2':
                        # Option to display previously saved data
                        print("\nPreviously saved data:")
                        saved_data = read_from_csv(USER_DATA_FILE)
                        print(saved_data)

                    elif choice == '3':
                        print("Logging out.")
                        break

                    else:
                        print("Invalid option. Please try again.")

            else:
                print("Invalid email or password.")

        elif choice == '3':
            print("Exiting the program.")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
