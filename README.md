# Catwalk Stock Picker

An academic MIS project that simulates stock selection and analyzes daily performance using rule-based logic.

This application allows users to manually select stocks or automatically generate selections using a custom “Catwalk” algorithm, then summarizes performance metrics such as price changes and returns.

---

## Project Overview

The application simulates a 10x10 grid of 100 stocks. Each stock has:
- A ticker symbol
- An opening price
- A closing price
- A dollar change
- A percentage change
- An up/down indicator

Users can:
- Manually select up to 8 stocks
- Reset selections
- Use the **Catwalk algorithm** to automatically select stocks
- View a summary table of selected stock performance

---

## What is the Catwalk Algorithm?

The **Catwalk algorithm** is a rule-based stock selection method designed to simulate a “path” across the stock grid.

### Catwalk Rules:
1. **Starting Position**
   - The first stock is selected from the outer two rows or columns of the grid (the perimeter).
2. **Movement Logic**
   - Each subsequent stock must be:
     - Different from previously selected stocks
     - Not positioned too close to the last selected stock
3. **Selection Limit**
   - The algorithm selects exactly **8 stocks**.

This logic prevents clustered selections and simulates movement across different regions of the dataset rather than random sampling.

---

## Why This Matters

This project demonstrates:
- Data generation and simulation
- Rule-based selection logic
- Data filtering and aggregation
- Performance metric calculation
- Translating raw data into summarized insights

The Catwalk algorithm models how constraints can influence data selection, which is common in real-world analytical decision-making.

---

## Technologies Used

- Python
- Django
- HTML / CSS
- Git / GitHub

---

## Features

- Interactive 10x10 stock grid
- Manual and automated stock selection
- Rule-based “Catwalk” selection algorithm
- Performance summary table
- Reset functionality
- Visual indicators for gains and losses

---

## Use Case

This project was developed as part of an MIS course to demonstrate how business rules and logic can be applied to data selection and analysis within a web-based system.

---

## Future Improvements

- Export selected stock data to CSV
- Add basic charts or visualizations
- Incorporate real stock market data
- Improve selection constraints and analytics

---
<img width="2559" height="1403" alt="image" src="https://github.com/user-attachments/assets/dd31848b-b9bd-45bd-87e2-46428dd0687e" />

## Author

Developed by Vu Pham & Dylan Diaz
