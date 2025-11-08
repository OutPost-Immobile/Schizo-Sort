#ifndef SCHIZO_SORT_CSVPARSER_H
#define SCHIZO_SORT_CSVPARSER_H
#include <fstream>

#include "ExcelTable.h"

template <class T>
inline void parseResultToCsv(ExcelTable<T>& table, std::string fileName)
{
    std::ofstream file (fileName);

    file << table.GetArraySizeColHeader() << "," << table.GetTimeColHeader() << std::endl;

    for (auto row : table.GetRows())
    {
        file << row.GetArraySize() << "," << row.GetTime() << std::endl;
    }
}

#endif //SCHIZO_SORT_CSVPARSER_H