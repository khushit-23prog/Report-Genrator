import pandas as pd
import matplotlib.pyplot as plt
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Image,
    Table,
    TableStyle,
    PageBreak
)
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime
import os

# Read sales data
base_dir = os.path.dirname(os.path.abspath(__file__))
csv_file = os.path.join(base_dir, "sales_data.csv")

df = pd.read_csv(csv_file)

# Revenue calculations
df["Revenue"] = df["Quantity"] * df["Price"]

total_products = len(df)
total_quantity = df["Quantity"].sum()
total_revenue = df["Revenue"].sum()
average_revenue = df["Revenue"].mean()

best_product = df.loc[df["Revenue"].idxmax(), "Product"]
highest_revenue = df["Revenue"].max()
most_quantity_product = df.loc[df["Quantity"].idxmax(), "Product"]

# Create revenue chart
chart_file = os.path.join(base_dir, "sales_chart.png")

plt.figure(figsize=(8, 5))
plt.bar(df["Product"], df["Revenue"])

plt.title("Revenue by Product")
plt.xlabel("Products")
plt.ylabel("Revenue (₹)")
plt.grid(axis="y")

plt.tight_layout()
plt.savefig(chart_file)
plt.close()

# Generate PDF report
pdf_file = os.path.join(base_dir, "Sales_Report.pdf")

pdf = SimpleDocTemplate(pdf_file)
styles = getSampleStyleSheet()

elements = []

# Cover page
elements.append(
    Paragraph(
        "CODTECH IT SOLUTIONS",
        styles["Title"]
    )
)

# ... your existing cover page code ...

# Executive summary
summary = f"""
<b>Total Products:</b> {total_products}<br/><br/>
<b>Total Quantity Sold:</b> {total_quantity}<br/><br/>
<b>Total Revenue:</b> ₹{total_revenue:,.2f}<br/><br/>
<b>Average Revenue:</b> ₹{average_revenue:,.2f}<br/><br/>
<b>Best Product:</b> {best_product}
"""

# Sales data table
table_data = [
    ["Product", "Quantity", "Price", "Revenue"]
]

# ... your existing table code ...

# Revenue chart page
elements.append(
    Image(chart_file, width=450, height=280)
)

# Insights and conclusion
insights = f"""
<b>Key Insights</b><br/><br/>

• {best_product} generated the highest revenue
of ₹{highest_revenue:,.2f}.<br/><br/>

• Total revenue reached
₹{total_revenue:,.2f}.<br/><br/>

• {most_quantity_product} achieved the
highest sales quantity.<br/><br/>

• Sales performance indicates strong
business growth potential.
"""

pdf.build(elements)

print("PDF REPORT GENERATED SUCCESSFULLY")
print("File:", pdf_file)