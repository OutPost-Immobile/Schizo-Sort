cmake_minimum_required(VERSION 3.31)
project(Schizo_Sort)

set(CMAKE_CXX_STANDARD 26)

add_executable(Schizo_Sort main.cpp
        Results/TimeResult.h
        Parser/CsvParser.h
        Parser/ExcelTable.h
        Tester.hpp
        RandomArrayGenerator.h
        QuickSort.h)
