import time
import tracemalloc
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from collections import deque
    
# --- Functiion Iterative ---
def fifo_iterative(input_data):
    # deque untuk O(1) pops dari kiri
    queue = deque(input_data)

    results = []
    while queue:
        # Proses simulasi
        item = queue.popleft()
        results.append(item)
    return results


# --- Function Rekursif ---
def fifo_recursive(input_data):
    # Cek input kosong
    if not input_data:
        return []

    # Proses head/kepala (First In/Masuk pertama)
    current_item = input_data[0]

    # Recurse on the tail (Rest of the list)
    # Slicing [1:] untuk menghilangkan head
    return [current_item] + fifo_recursive(input_data[1:])
def opsi():
    # input inventori
    inventori = []
    print("Gunakan q untuk keluar atau d untuk default data (10, 200, 300, 400, 500, 600)")
    
    # Logika input
    while True:
        kasus = input("Masukkan 6 Input : ")
        if kasus.lower() == "q":
            quit()
        # Kasus Default
        elif kasus.lower() == "d":
            inventori = [10, 200, 300, 400, 500, 600]
            break
        # Pengecekkan input angka
        elif not kasus.isdigit():
            print("Input harus berupa angka")
            continue
        
        # Pengecekkan jumlah input
        if len(inventori) <= 5:
            inventori.append(int(kasus))
            print(inventori)
            continue
        elif len(inventori) > 5:
            break
    return inventori

# --- Eksekusi ---
if __name__ == "__main__":
    # input inventori barang
    data_source = opsi()

    iterative_times = []
    recursive_times = []
    
    for n in data_source:
        data = list(range(n))
        
        # 1. Mengukur Iterative
        tracemalloc.start()
        start = time.perf_counter()
        fifo_iterative(data)
        iterative_times.append(time.perf_counter() - start)
        
        # Memori yang digunakan iteratif
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        iterative_memory = peak / 1024
        print(f"Iterative Memory Usage: {iterative_memory:.2f} KB")
        
    for n in data_source:
        data = list(range(n))
        
        # 2. Mengukur Recursive
        tracemalloc.start()
        start = time.perf_counter()
        fifo_recursive(data)
        recursive_times.append(time.perf_counter() - start)
        
        # Memori yang digunakan rekursif
        current, peak = tracemalloc.get_traced_memory()
        recursive_memory = peak / 1024
        print(f"Recursive Memory Usage: {recursive_memory:.2f} KB")
        tracemalloc.stop()

    
    plt.figure(figsize=(10, 6))

    # Garis Plot Iterative 
    plt.plot(data_source, iterative_times, label='Iteratif (Deque)', marker='o', linewidth=2)

    # Garis Plot Recursive 
    plt.plot(data_source, recursive_times, label='Rekursiif (List Slicing)', marker='x', linewidth=2)

    plt.title('Time Complexity: Iteratif vs Rekursif FIFO')
    plt.xlabel('Input Size (N)')
    plt.ylabel('Time (seconds)')
    plt.legend()
    plt.grid(True)

    # Save or Show
    plt.savefig('perbandingan_kompleksitas_fifo.png')
    