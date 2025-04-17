import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_pdf import PdfPages

df = pd.read_csv("cleaned_perfume_data.csv") 

sns.set(style='whitegrid', palette='pastel')
color = "#7EB6FF"

numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns

with PdfPages('perfume_visualizations.pdf') as pdf:

    plt.figure(figsize=(18, 12))
    for i, col in enumerate(numeric_cols):
        plt.subplot(3, 2, i+1)
        sns.histplot(df[col], kde=True, color=color, edgecolor='black', linewidth=1.2, bins=20)
        plt.title(f'Distribution of {col}', fontsize=14, fontweight='bold')
        plt.xlabel(col)
        plt.ylabel('Count')
        plt.grid(True, linestyle='--', alpha=0.5)

    plt.tight_layout(pad=2.0)
    plt.suptitle('📊 Histograms of Numeric Features', fontsize=18, fontweight='bold', y=1.02)
    pdf.savefig()
    plt.close()
    plt.figure(figsize=(18, 12))

    for i, col in enumerate(numeric_cols):
        plt.subplot(3, 2, i+1)
        sns.boxplot(data=df, y=col, color=color)
        plt.title(f'Boxplot of {col}', fontsize=14, fontweight='bold')
        plt.ylabel(col)
        plt.grid(True, linestyle='--', alpha=0.5)
        plt.xticks([])

    plt.tight_layout(pad=2.0)
    plt.suptitle('📦 Boxplots of Numeric Features', fontsize=18, fontweight='bold', y=1.02)
    pdf.savefig()
    plt.close()

    plt.figure(figsize=(18, 12))
    for i, col in enumerate(numeric_cols):
        plt.subplot(3, 2, i+1)
        sns.stripplot(data=df, x=[col]*len(df), y=col, color=color, alpha=0.6, jitter=True)
        plt.title(f'Strip Plot of {col}', fontsize=14, fontweight='bold')
        plt.ylabel(col)
        plt.grid(True, linestyle='--', alpha=0.5)
        plt.xticks([])

    plt.tight_layout(pad=2.0)
    plt.suptitle('🔵 Dot Plots of Numeric Features', fontsize=18, fontweight='bold', y=1.02)
    pdf.savefig()
    plt.close()

print("✅ PDF 'perfume_visualizations.pdf' has been created!")
