# Images Folder

This folder contains visualization screenshots and charts generated from the analysis.

## Expected Files

- `dashboard_preview.png` - Screenshot of the Power BI dashboard
- `funnel_chart.png` - Visualization of the user conversion funnel
- `category_revenue.png` - Bar chart showing revenue by product category

## Usage

These images can be used for:
- Project documentation
- Presentation slides
- Portfolio showcases
- Reports and summaries

## Generating Images

To generate these images:
1. Run the EDA notebook to create visualizations
2. Save plots using `plt.savefig()` in the notebooks
3. Take screenshots of the Power BI dashboard
4. Place images in this folder

## Example Code to Save Plots

```python
# In your notebook
plt.figure(figsize=(10, 6))
# ... your plotting code ...
plt.savefig('../Images/category_revenue.png', dpi=300, bbox_inches='tight')
plt.show()
```

