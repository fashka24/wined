#include <iostream>

// lib
#include "src/debug.hpp"
#include "src/wmain.hpp"

int main(int argc, char const *argv[])
{
    dvoid("version " WINED_VERSION);

    wined_main();

    return 0;
}
