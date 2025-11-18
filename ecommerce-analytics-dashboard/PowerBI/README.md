# Power BI Dashboard

## Overview
This folder contains the Power BI dashboard file (`ecommerce_dashboard.pbix`) for visualizing e-commerce analytics.

## Setup Instructions

1. **Open Power BI Desktop**
   - Download from [Microsoft Power BI](https://powerbi.microsoft.com/desktop/) if not already installed

2. **Connect to Data**
   - Open `ecommerce_dashboard.pbix`
   - The dashboard should connect to `../Data/cleaned_ecommerce_dataset.csv`
   - If the connection fails, update the data source path in Power BI

3. **Refresh Data**
   - Click "Refresh" to load the latest cleaned dataset
   - Ensure the cleaned dataset exists in the `Data/` folder

## Dashboard Components

### KPIs (Top Section)
- Total Revenue
- Total Orders
- Conversion Rate
- Cart Abandonment Rate
- Average Order Value (AOV)
- Revenue per User (RPU)

### Visualizations
- **Funnel Chart**: User journey from homepage to purchase
- **Bar Chart**: Top product categories by revenue
- **Line Chart**: Monthly revenue trends
- **Demographic Breakdowns**: Revenue by age, gender, location
- **Heatmap**: Activity patterns (if time data available)

## Customization

To customize the dashboard:
1. Modify visualizations in Power BI Desktop
2. Add new measures using DAX formulas
3. Adjust filters and slicers as needed
4. Update color schemes to match your brand

## Data Refresh

To refresh data:
1. Ensure `cleaned_ecommerce_dataset.csv` is up to date
2. In Power BI, go to Home → Refresh
3. Or set up automatic refresh schedule in Power BI Service

## Notes
- The dashboard is designed to work with the cleaned dataset from the data cleaning notebook
- Column names should match those in the cleaned dataset
- If column names differ, update the field mappings in Power BI

