import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import glob
import os

# Set Polish font for matplotlib (optional, for better Polish character support)
plt.rcParams['font.family'] = ['DejaVu Sans', 'Liberation Sans', 'Arial']

def create_performance_chart():
    # Find all results CSV files
    csv_files = glob.glob('*results.csv')
    csv_files = [f for f in csv_files if f != 'results.csv']  # Exclude the original results.csv

    if not csv_files:
        print("Nie znaleziono plików CSV z wynikami!")
        return

    # Sort files by thread count
    csv_files.sort(key=lambda x: int(x.replace('results.csv', '')))

    plt.figure(figsize=(15, 10))

    colors = plt.cm.tab10(np.linspace(0, 1, len(csv_files)))

    for i, csv_file in enumerate(csv_files):
        try:
            df = pd.read_csv(csv_file)
            thread_count = csv_file.replace('results.csv', '')

            # Assuming CSV structure: Rozmiar Tablicy, Czas
            if len(df.columns) >= 2:
                x = df.iloc[:, 0]  # Rozmiar tablicy
                y = df.iloc[:, 1]  # Czas

                plt.plot(x, y, 'o-', linewidth=2, markersize=6,
                         color=colors[i], label=f'{thread_count} wątków',
                         markerfacecolor=colors[i], markeredgecolor='black',
                         markeredgewidth=0.5)

        except Exception as e:
            print(f"Błąd odczytu {csv_file}: {e}")

    # Customize the chart
    plt.title('Analiza Wydajności algorytmu sortowania szybkiego\nCzas Wykonania vs Rozmiar Tablicy dla Różnych Liczb Wątków',
              fontsize=16, fontweight='bold', pad=20)
    plt.xlabel('Rozmiar Tablicy', fontsize=14, fontweight='bold')
    plt.ylabel('Średni Czas (milisekundy)', fontsize=14, fontweight='bold')

    # Add grid and legend
    plt.grid(True, alpha=0.3, linestyle='--')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=10)

    # Format axes
    plt.ticklabel_format(style='plain', axis='x')
    plt.xticks(rotation=45)

    # Adjust layout
    plt.tight_layout()

    # Save as JPG
    plt.savefig('porownanie_wydajnosci_quicksort.jpg', dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')

    print("Wykres zapisano jako 'porownanie_wydajnosci_quicksort.jpg'")
    plt.show()

def create_individual_charts():
    """Twórz indywidualne wykresy dla każdej liczby wątków"""
    csv_files = glob.glob('*results.csv')
    csv_files = [f for f in csv_files if f != 'results.csv']
    csv_files.sort(key=lambda x: int(x.replace('results.csv', '')))

    for csv_file in csv_files:
        try:
            df = pd.read_csv(csv_file)
            thread_count = csv_file.replace('results.csv', '')

            if len(df.columns) >= 2:
                x = df.iloc[:, 0]
                y = df.iloc[:, 1]

                plt.figure(figsize=(10, 6))
                plt.plot(x, y, 'b-o', linewidth=2, markersize=8,
                         markerfacecolor='red', markeredgecolor='darkred',
                         markeredgewidth=2)

                # Add value labels
                for xi, yi in zip(x, y):
                    plt.annotate(f'{yi}ms', (xi, yi), textcoords="offset points",
                                 xytext=(0,10), ha='center', fontsize=9,
                                 bbox=dict(boxstyle="round,pad=0.3",
                                           facecolor="yellow", alpha=0.7))

                plt.title(f'Wydajność algorytmu sortowania szybkiego - {thread_count} Wątków\nCzas Wykonania vs Rozmiar Tablicy',
                          fontsize=14, fontweight='bold')
                plt.xlabel('Rozmiar Tablicy', fontsize=12, fontweight='bold')
                plt.ylabel('Średni Czas (milisekundy)', fontsize=12, fontweight='bold')
                plt.grid(True, alpha=0.3, linestyle='--')
                plt.ticklabel_format(style='plain', axis='x')
                plt.xticks(rotation=45)
                plt.tight_layout()

                plt.savefig(f'quicksort_{thread_count}watkow.jpg', dpi=300,
                            bbox_inches='tight', facecolor='white')
                print(f"Wykres zapisano jako 'quicksort_{thread_count}watkow.jpg'")
                plt.close()

        except Exception as e:
            print(f"Błąd przetwarzania {csv_file}: {e}")

def print_comprehensive_statistics():
    """Wyświetl statystyki dla wszystkich konfiguracji wątków"""
    csv_files = glob.glob('*results.csv')
    csv_files = [f for f in csv_files if f != 'results.csv']
    csv_files.sort(key=lambda x: int(x.replace('results.csv', '')))

    print("\n=== Kompleksowe Statystyki Wydajności ===")

    best_times = {}

    for csv_file in csv_files:
        try:
            df = pd.read_csv(csv_file)
            thread_count = csv_file.replace('results.csv', '')

            if len(df.columns) >= 2:
                sizes = df.iloc[:, 0]
                times = df.iloc[:, 1]

                print(f"\n--- {thread_count} Wątków ---")
                print(f"Średni czas dla wszystkich rozmiarów: {times.mean():.2f}ms")
                print(f"Najlepszy czas: {times.min()}ms (rozmiar: {sizes[times.idxmin()]:,})")
                print(f"Najgorszy czas: {times.max()}ms (rozmiar: {sizes[times.idxmax()]:,})")

                # Store best performance for comparison
                best_times[thread_count] = times.min()

        except Exception as e:
            print(f"Błąd odczytu {csv_file}: {e}")

    if best_times:
        best_config = min(best_times.items(), key=lambda x: x[1])
        print(f"\n=== Najlepsza Ogólna Wydajność ===")
        print(f"Najlepsza konfiguracja: {best_config[0]} wątków z czasem {best_config[1]}ms")

def main():
    """Główna funkcja z menu użytkownika"""
    while True:
        print("\n=== Generator Wykresów Wydajności sortowania szybkiego ===")
        print("1. Utwórz wykres porównawczy (wszystkie liczby wątków)")
        print("2. Utwórz indywidualne wykresy dla każdej liczby wątków")
        print("3. Pokaż statystyki")
        print("4. Wykonaj wszystko powyżej")
        print("5. Wyjście")

        choice = input("\nWprowadź swój wybór (1-5): ").strip()

        if choice == '1':
            create_performance_chart()
        elif choice == '2':
            create_individual_charts()
        elif choice == '3':
            print_comprehensive_statistics()
        elif choice == '4':
            create_performance_chart()
            create_individual_charts()
            print_comprehensive_statistics()
        elif choice == '5':
            print("Do widzenia!")
            break
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")

if __name__ == "__main__":
    main()