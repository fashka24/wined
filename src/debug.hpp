#pragma once

#include <iostream>

#define WINED_VERSION "1.0 C++"

// d = debug

void dvoid(std::string text) {
    std::cout << "[wined] " <<
    text
    << "\n";
}
void dinfo(std::string text) {
    std::cout << "[INFO] " <<
    text
    << "\n";
}
void derror(std::string text) {
    std::cerr << "[ERROR] " <<
    text
    << "\n";
}
void dwarn(std::string text) {
    std::cerr << "[WARN] " <<
    text
    << "\n";
}