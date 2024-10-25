cmake_minimum_required(VERSION 3.13)

include(pico_sdk_import.cmake)
project(taskThree C CXX ASM)

set(CMAKE_C_STANDARD 11)
set(CMAKE_CXX_STANDARD 17)

pico_sdk_init()

include_directories(${CMAKE_SOURCE_DIR})

add_executable(taskThree
  taskThree.S
  sdklink.c
)

pico_enable_stdio_uart(taskThree 1)
pico_enable_stdio_usb(taskThree 1)

pico_add_extra_outputs(taskThree)

target_link_libraries(taskThree pico_stdlib)
