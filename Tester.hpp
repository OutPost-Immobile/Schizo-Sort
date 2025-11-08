#pragma once
#ifndef TESTER_H
#define TESTER_H

#include <chrono>
#include <iostream>
#include <map>

#include "QuickSort.h"
#include "RandomArrayGenerator.h"
#include "Parser/CsvParser.h"
#include "Parser/ExcelTable.h"
#include "Results/TimeResult.h"

inline void TestRandomArraysWithThreads(int iterations)
{
    const std::vector<int> sizes = { 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000 };
    const std::vector<int> threadsBottleNecks = { 10, 20, 30, 40, 50, 60, 70, 80, 90, 100 };

    auto randomArrays = GenerateRandomArrayCollection(sizes);

    std::map<int, std::vector<TimeResult>> resultsMap;

    for (auto threadBottleNeck : threadsBottleNecks)
    {
        std::vector<TimeResult> results;
        for (auto array : randomArrays)
        {
            std::vector<double> tempArray;
            for (int i = 0; i < iterations; ++i)
            {
                std::shuffle(array.begin(), array.end(), std::default_random_engine(std::chrono::system_clock::now().time_since_epoch().count()));

                auto start = std::chrono::high_resolution_clock::now();
                quickSortThreaded(array, 0, array.size() - 1, threadBottleNeck);
                auto end = std::chrono::high_resolution_clock::now();

                tempArray.push_back(std::chrono::duration<double, std::milli>(end - start).count());
            }

            auto averageTime = std::accumulate(tempArray.begin(), tempArray.end(), 0.0) / tempArray.size();

            std::cout << "Array size: " << array.size() << std::endl;
            std::cout << "Average time: " << averageTime << std::endl;

            auto temp_result = std::make_unique<TimeResult>();

            temp_result->SetArraySize(array.size());
            temp_result->SetTime(averageTime);
            results.push_back(*temp_result);
        }

        resultsMap[threadBottleNeck] = results;
    }

    for (const auto& result : resultsMap)
    {
        auto tableToWrite = std::make_unique<ExcelTable<TimeResult>>(result.second);

        std::string fileName = "../Python/" + std::to_string(result.first) + "results.csv";

        parseResultToCsv(*tableToWrite, fileName);
    }
}


#endif // TESTER_H