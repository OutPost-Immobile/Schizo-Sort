#ifndef SCHIZO_SORT_ALGORITHMS_H
#define SCHIZO_SORT_ALGORITHMS_H
#include <thread>

//Quick sort algorithm with multithreading where the amount of threads is limited by a parameter
inline void quickSortThreaded(std::vector<int>& arr, int left, int right, int maxThreads) {
    if (left < right) {
        int pivot = arr[right];
        int i = left - 1;
        for (int j = left; j < right; j++) {
            if (arr[j] <= pivot) {
                i++;
                std::swap(arr[i], arr[j]);
            }
        }
        std::swap(arr[i + 1], arr[right]);
        int pivotIndex = i + 1;
        if (maxThreads > 1) {
            std::thread leftThread(quickSortThreaded, std::ref(arr), left, pivotIndex - 1, maxThreads / 2);
            quickSortThreaded(arr, pivotIndex + 1, right, maxThreads / 2);
            leftThread.join();
        } else {
            quickSortThreaded(arr, left, pivotIndex - 1, maxThreads);
            quickSortThreaded(arr, pivotIndex + 1, right, maxThreads);
        }
    }
}

//Quick sort single threaded
inline void quickSort(std::vector<int>& arr, int left, int right) {
    if (left < right) {
        int pivot = arr[right];
        int i = left - 1;
        for (int j = left; j < right; j++) {
            if (arr[j] <= pivot) {
                i++;
                std::swap(arr[i], arr[j]);
            }
        }
        std::swap(arr[i + 1], arr[right]);
        int pivotIndex = i + 1;
        quickSort(arr, left, pivotIndex - 1);
        quickSort(arr, pivotIndex + 1, right);
    }
}

#endif //SCHIZO_SORT_ALGORITHMS_H