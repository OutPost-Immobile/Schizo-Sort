import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def create_performance_chart():
    # Read the CSV file
    try:
        df = pd.read_csv('../results.csv')
    except FileNotFoundError:
        print("Error: results.csv file not found!")
        return

    # Assuming the CSV has columns for array size and time
    # Adjust column names based on your actual CSV structure
    if 'ArraySize' in df.columns and 'Time' in df.columns:
        x = df['ArraySize']
        y = df['Time']
    elif len(df.columns) >= 2:
        # Use first two columns if column names are different
        x = df.iloc[:, 0]
        y = df.iloc[:, 1]
    else:
        print("Error: CSV file doesn't have enough columns!")
        return

    # Create the figure and axis
    plt.figure(figsize=(12, 8))

    # Create the plot
    plt.plot(x, y, 'b-o', linewidth=2, markersize=8, markerfacecolor='red',
             markeredgecolor='darkred', markeredgewidth=2)

    # Customize the chart
    plt.title('QuickSort Performance Analysis\nExecution Time vs Array Size',
              fontsize=16, fontweight='bold', pad=20)
    plt.xlabel('Array Size', fontsize=14, fontweight='bold')
    plt.ylabel('Average Time (milliseconds)', fontsize=14, fontweight='bold')

    # Add grid for better readability
    plt.grid(True, alpha=0.3, linestyle='--')

    # Format x-axis to show values in a readable format
    plt.ticklabel_format(style='plain', axis='x')
    plt.xticks(rotation=45)

    # Add value labels on data points
    for i, (xi, yi) in enumerate(zip(x, y)):
        plt.annotate(f'{yi}ms', (xi, yi), textcoords="offset points",
                     xytext=(0,10), ha='center', fontsize=10,
                     bbox=dict(boxstyle="round,pad=0.3", facecolor="yellow", alpha=0.7))

    # Adjust layout to prevent label cutoff
    plt.tight_layout()

    # Save as JPG
    plt.savefig('quicksort_performance_chart.jpg', dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')

    print("Chart saved as 'quicksort_performance_chart.jpg'")

    # Optionally display the chart
    plt.show()

def print_statistics():
    """Print some basic statistics about the performance data"""
    try:
        df = pd.read_csv('results.csv')

        if 'ArraySize' in df.columns and 'Time' in df.columns:
            sizes = df['Rozmiar tablicy']
            times = df['Czas sortowania']
        else:
            sizes = df.iloc[:, 0]
            times = df.iloc[:, 1]

        print("\n=== Performance Statistics ===")
        print(f"Smallest array size: {sizes.min():,}")
        print(f"Largest array size: {sizes.max():,}")
        print(f"Fastest time: {times.min()}ms")
        print(f"Slowest time: {times.max()}ms")
        print(f"Average time: {times.mean():.2f}ms")

        # Calculate time complexity approximation
        if len(sizes) > 1:
            time_ratio = times.iloc[-1] / times.iloc[0]
            size_ratio = sizes.iloc[-1] / sizes.iloc[0]
            print(f"\nTime scaling factor: {time_ratio:.2f}x")
            print(f"Size scaling factor: {size_ratio:.2f}x")

    except Exception as e:
        print(f"Error reading statistics: {e}")

if __name__ == "__main__":
    create_performance_chart()
    print_statistics()