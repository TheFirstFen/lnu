cmake_minimum_required(VERSION 3.13)

SET(FREERTOS_KERNEL_PATH ${CMAKE_CURRENT_SOURCE_DIR}/lib/FreeRTOS-Kernel)

include(pico_sdk_import.cmake)
include(${FREERTOS_KERNEL_PATH}/portable/ThirdParty/GCC/RP2040/FreeRTOS_Kernel_import.cmake)
include_directories(${CMAKE_SOURCE_DIR})

project(Project C CXX ASM)

set(CMAKE_C_STANDARD 11)
set(CMAKE_CXX_STANDARD 17)

# Initialize the Pico SDK
pico_sdk_init()

add_subdirectory(dht)

# Add the C source file
add_executable(Project
    Project.c
)

# Enable UART and USB for stdio
pico_enable_stdio_uart(Project 1)
pico_enable_stdio_usb(Project 1)

# Create map/bin/hex/uf2 files
pico_add_extra_outputs(Project)

# Link with the Pico SDK libraries and FreeRTOS
target_link_libraries(Project
    pico_stdlib           # For standard Pico SDK functionality
    FreeRTOS-Kernel       # For the FreeRTOS kernel
    FreeRTOS-Kernel-Heap4 # For heap memory management in FreeRTOS (or choose another heap type)
    dht
)
