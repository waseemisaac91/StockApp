Part 1: HTML and CSS

1. Create a webpage with the following elements:
- A form with fields for entering a stock ticker symbol, start date, and end date.
- A button to submit the form.
- A section to display the stock data and a chart (to be added later).
2. Use CSS to style the page:
- Apply a consistent layout to the form and result sections.
- Use a responsive design that adjusts for different screen sizes.
- Style the form inputs, button, and result section to improve readability.
- 
- Part 2: Python
3. Write a Python program that uses the `yfinance` library to fetch real stock data from Yahoo Finance. The program should:
- Accept user input for a stock ticker symbol, start date, and end date.
- - Use `yfinance` to fetch the stock's open and close prices for the specified dates.
- Print the stock data to the console.
Part 3: Django
4. Create a Django project with a single app called "stockapp".
- Define a model called "StockData" with fields for ticker symbol, date, open price, and close price.
- Create a view to display the form for entering stock data (ticker symbol, start date, and end date).
- Create a view to process the form submission, fetch the stock data using `yfinance`, and display the results on the webpage.
- Plot a chart of the stock's open and close prices for the specified dates.
