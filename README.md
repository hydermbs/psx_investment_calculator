# 📈 PSX Investment Calculator

A Streamlit web application that helps investors allocate their capital across top-performing companies in the **Pakistan Stock Exchange (PSX) KSE-100 Index** based on real-time index weightage data.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## ✨ Features

- **Real-time Data Scraping** — Fetches live KSE-100 index data from PSX website
- **Smart Allocation** — Distributes investment proportionally based on index weightage
- **Customizable** — Choose your investment amount and number of companies
- **Beautiful UI** — Dark financial-themed interface with gold accents
- **Instant Results** — View company names, allocation percentages, and PKR amounts

## 🖥️ Screenshot

| Company Name | Percentage | Amount (PKR) |
|--------------|------------|--------------|
| United Bank Limited | 28.81% | 28,812.10 |
| Lucky Cement Limited | 18.62% | 18,617.71 |
| Engro Holdings Limited | 18.06% | 18,056.16 |
| Hub Power Company | 17.67% | 17,667.39 |
| Meezan Bank Limited | 16.85% | 16,846.65 |

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/psx-investment-calculator.git
   cd psx-investment-calculator
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Open your browser** and navigate to `http://localhost:8501`

## 📁 Project Structure

```
psx_analysis/
├── app.py              # Streamlit web application
├── file.py             # Data scraping and calculation logic
├── styles.css          # Custom financial-themed CSS
├── main.ipynb          # Jupyter notebook for exploration
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

## 🔧 How It Works

1. **Data Fetching** — Scrapes the KSE-100 index table from [PSX website](https://dps.psx.com.pk/indices/KSE100)
2. **Top Companies Selection** — Sorts companies by index weightage and selects top N
3. **Investment Calculation** — Applies a 1.5x multiplier to index weights, then normalizes to 100%
4. **Amount Distribution** — Calculates exact PKR amount for each company based on your total investment

### Calculation Formula

```
Investment % = Index Weight × 1.5
Normalized % = (Investment % / Sum of all Investment %) × 100
Amount (PKR) = (Normalized % / 100) × Total Investment
```

## 🎨 Customization

### Modify the CSS Theme

Edit `styles.css` to customize colors:

```css
:root {
    --navy-primary: #1a365d;    /* Background */
    --gold-primary: #d69e2e;    /* Headers */
    --green-profit: #38a169;    /* Positive values */
}
```

### Change Number of Companies

In the app, use the "Number of Companies" input to select 1-100 companies.

## 📊 Data Source

- **Source**: Pakistan Stock Exchange (PSX)
- **Index**: KSE-100
- **URL**: https://dps.psx.com.pk/indices/KSE100
- **Data**: Real-time index weightage, prices, and market cap

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| **Streamlit** | Web application framework |
| **Pandas** | Data manipulation and analysis |
| **Requests** | HTTP requests for web scraping |
| **BeautifulSoup4** | HTML parsing |

## ⚠️ Disclaimer

This tool is for **educational and informational purposes only**. It does not constitute financial advice. Always conduct your own research and consult with a qualified financial advisor before making investment decisions. Past performance is not indicative of future results.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📧 Contact

For questions or feedback, please open an issue on GitHub.

---

<p align="center">
  Made with ❤️ for Pakistani investors
</p>

