# Data Folder

This folder contains the datasets used in the analysis.

## Files

### Input Files
- `ecommerce_user_segmentation.csv` - **REQUIRED**: Raw dataset to be cleaned
  - Place your raw e-commerce dataset here before running the data cleaning notebook

### Output Files (Generated)
- `cleaned_ecommerce_dataset.csv` - Cleaned dataset (output from `data_cleaning.ipynb`)
  - This file is generated automatically when you run the data cleaning notebook
  - Used as input for EDA and funnel analysis notebooks

- `user_funnel_report.csv` - Funnel analysis report (output from `user_funnel_analysis.ipynb`)
  - Contains step-by-step user counts and drop-off percentages
  - Generated automatically when you run the funnel analysis notebook

## Usage

1. **Before running notebooks:**
   - Place your raw dataset as `ecommerce_user_segmentation.csv` in this folder

2. **After running notebooks:**
   - The cleaned dataset and reports will be saved here automatically
   - These files can be used for Power BI dashboard connections

## Data Format

The raw dataset should contain columns such as:
- User/Customer ID
- Age, Gender, Location
- Product Category
- Revenue/Amount/Price
- Timestamp/Date
- Action/Event type
- Session ID (optional)

The notebooks will auto-detect these columns based on naming patterns.

