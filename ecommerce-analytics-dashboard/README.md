# E-commerce User Behavior Analytics & Dashboard

A comprehensive analytics project for analyzing user behavior, segmentation, and conversion funnels in e-commerce data. This project includes data cleaning, exploratory data analysis, funnel analysis, and Power BI dashboard recommendations.

## 📁 Project Structure

```
ecommerce-analytics-dashboard/
│
├─ README.md                          # Project documentation
├─ PowerBI/
│   └─ ecommerce_dashboard.pbix       # Power BI dashboard file
├─ Data/
│   ├─ cleaned_ecommerce_dataset.csv  # Cleaned dataset (output from data_cleaning.ipynb)
│   ├─ ecommerce_user_segmentation.csv  # Raw dataset (input)
│   └─ user_funnel_report.csv        # Funnel analysis report
├─ Notebooks/
│   ├─ data_cleaning.ipynb            # Data cleaning and preprocessing
│   ├─ EDA.ipynb                      # Exploratory Data Analysis
│   └─ user_funnel_analysis.ipynb    # User funnel & drop-off analysis
├─ Scripts/
│   └─ helper_functions.py            # Utility functions (if any)
└─ Images/
    ├─ dashboard_preview.png          # Dashboard preview screenshot
    ├─ funnel_chart.png               # Funnel visualization
    └─ category_revenue.png           # Category revenue chart
```

## 🚀 Getting Started

### Prerequisites

- Python 3.7+
- Jupyter Notebook or JupyterLab
- Required Python packages:
  ```bash
  pip install pandas numpy matplotlib seaborn jupyter
  ```

### Installation

1. Clone or download this repository
2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Place your raw dataset in the `Data/` folder as `ecommerce_user_segmentation.csv`

## 📊 Workflow

### Step 1: Data Cleaning
Run `Notebooks/data_cleaning.ipynb` to:
- Load and inspect the raw dataset
- Handle missing values (mean for numerical, mode for categorical)
- Convert date/time columns to datetime format
- Strip whitespace from text columns
- Standardize column names (lowercase with underscores)
- Remove duplicate rows
- Detect outliers using IQR method (without removal)
- Export cleaned dataset to `Data/cleaned_ecommerce_dataset.csv`

### Step 2: Exploratory Data Analysis
Run `Notebooks/EDA.ipynb` to:
- Perform basic statistical summaries
- Analyze user behavior patterns
- Segment users by demographics (age, gender, location)
- Analyze revenue by product categories and segments
- Generate visualizations (histograms, bar charts, pie charts, line plots)
- Auto-generate insights

### Step 3: Funnel Analysis
Run `Notebooks/user_funnel_analysis.ipynb` to:
- Track user journey through conversion funnel:
  - Homepage/Browse → Product View → Add to Cart → Checkout → Payment Success
- Calculate drop-off rates at each step
- Identify the step with highest drop-off
- Generate actionable recommendations
- Export funnel report to `Data/user_funnel_report.csv`

## 📈 Power BI Dashboard Recommendations

### Key Performance Indicators (KPIs)

| KPI | Description | Tooltip |
|-----|-------------|---------|
| **Total Revenue** | Total money generated from all completed purchases | "Total amount earned from customer purchases." |
| **Total Orders / Purchases** | Count of successful transactions | "Number of successful transactions completed." |
| **Conversion Rate (%)** | % of website visitors who completed a purchase | "Percentage of visits that ended in a purchase." |
| **Cart Abandonment Rate (%)** | % of users who added items to cart but did not purchase | "Percentage of users who added items to cart but did not buy." |
| **Average Order Value (AOV)** | Average revenue generated per purchase | "Average revenue generated each time a user completes a purchase." |
| **Revenue per User (RPU)** | Average revenue generated per unique customer | "Average amount spent by each unique customer." |
| **Returning Customer Rate (%)** | % of customers who placed more than one order | "Percentage of customers who ordered more than once." |

### Recommended Visualizations

1. **Bar Chart** - Top Product Categories by Revenue
   - Shows which products drive business

2. **Line Chart** - Monthly Revenue Trend
   - Reveals growth patterns and seasonality

3. **Funnel Chart** - User Journey
   - Homepage → Product → Cart → Checkout → Purchase
   - Clearly shows where drop-offs happen

4. **Stacked Column / Tree Map** - Revenue by Region/Gender/Age
   - Demographic breakdown of sales

5. **Heatmap** (Optional) - Day × Hour Activity
   - Helps find peak traffic times

### Dashboard Layout

| Section | Content |
|---------|---------|
| **Top** | KPIs (Revenue, Conversion Rate, Cart Abandonment, AOV, etc.) |
| **Left Panel** | Funnel chart + Conversion flow insights |
| **Right Panel** | Sales breakdown visual (Top categories, demographics, devices) |
| **Bottom Full-width** | Revenue over time (monthly trend line) + insights note |

**Design Tip:** Use a fixed color palette - highlight positive metrics in green and drop-offs in orange/red.

## 📝 Key Features

- **Generic & Auto-Detecting**: The code automatically detects columns like user_id, age, gender, location, product category, revenue, and timestamps based on column name patterns
- **Robust Error Handling**: Skips missing columns gracefully with helpful messages
- **Comprehensive Cleaning**: Handles missing values, duplicates, outliers, and data type conversions
- **Actionable Insights**: Auto-generates business insights from the analysis
- **Visualization Ready**: Creates publication-ready charts and graphs

## 🔍 Analysis Outputs

1. **Cleaned Dataset** (`Data/cleaned_ecommerce_dataset.csv`)
   - No missing values
   - Standardized column names
   - Duplicates removed
   - Outliers identified (not removed)

2. **Funnel Report** (`Data/user_funnel_report.csv`)
   - Step-by-step user counts
   - Drop-off percentages
   - Highest drop-off step identification

3. **Visualizations** (from EDA notebook)
   - Distribution plots
   - Revenue analysis charts
   - Demographic segmentation charts
   - Time series trends

## 💡 Business Insights

The analysis provides insights on:
- Most profitable product categories
- Highest spending customer segments (age, gender, location)
- Conversion funnel bottlenecks
- User behavior patterns
- Revenue trends over time

## 🛠️ Customization

The notebooks are designed to be generic and work with various e-commerce datasets. If your dataset has different column names, you can:

1. Modify the auto-detection logic in the notebooks
2. Manually specify column names in the code
3. Rename your columns to match expected patterns

## 📄 License

This project is open source and available for educational and portfolio purposes.

## 👤 Author

Created as part of an e-commerce analytics project for user behavior analysis and UI redesign.

## 📞 Support

For questions or issues, please refer to the notebook comments or create an issue in the repository.

---

**Note:** Make sure to place your raw dataset (`ecommerce_user_segmentation.csv`) in the `Data/` folder before running the notebooks.

