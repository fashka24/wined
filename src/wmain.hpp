#pragma once

#include <iostream>
#include <vector>

// lib
#include "debug.hpp"

// config
std::string inputer = "> ", inp;

void wined_main() {
    while (true)
    {
        try
        {
            printf(inputer.c_str());
            getline(std::cin, inp);
        }
        catch(const std::exception& e)
        {
            std::cerr << e.what() << '\n';
        }
        
    }
    

    return;
}