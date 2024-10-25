cmake_minimum_required(VERSION 3.5)
project(OneArmedBandit)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# List all source files explicitly
set(SOURCES 
    src/main.cpp
    src/core/bettingFunctions.cpp
    src/core/boardFunctions.cpp
    src/core/gameHistory.cpp
    src/core/helpers.cpp
    src/core/gameManager.cpp
)

# Include directories for header files
include_directories(src/headers)

# Create executable
add_executable(oneArmedBandit ${SOURCES})