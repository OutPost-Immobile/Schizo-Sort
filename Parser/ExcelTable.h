#ifndef SCHIZO_SORT_EXCELTABLE_H
#define SCHIZO_SORT_EXCELTABLE_H
#include <string>
#include <vector>

template <class T>
class ExcelTable
{
    private:
        std::string ArraySizeColHeader = "Array size";
        std::string TimeColHeader = "Time";
        std::vector<T> rows;

public:
    ExcelTable(std::vector<T> rows)
    {
       this->rows = rows;
    }

    std::string GetArraySizeColHeader()
    {
        return ArraySizeColHeader;
    }

    std::string GetTimeColHeader()
    {
        return TimeColHeader;
    }

    std::vector<T> GetRows()
    {
        return rows;
    }
};

#endif //SCHIZO_SORT_EXCELTABLE_H