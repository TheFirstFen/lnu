cmake_minimum_required(VERSION 3.27)

include(pico_sdk_import.cmake)

project(taskTwo C CXX ASM)
set(CMAKE_C_STANDARD 11)
set(CMAKE_CXX_STANDARD 17)

pico_sdk_init()

include_directories(${CMAKE_SOURCE_DIR})

add_executable(taskTwo
  main.c
)

pico_enable_stdio_uart(taskTwo 1)
pico_enable_stdio_usb(taskTwo 1)

pico_add_extra_outputs(taskTwo)

target_link_libraries(taskTwo pico_stdlib)
