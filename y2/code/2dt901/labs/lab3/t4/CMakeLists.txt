cmake_minimum_required(VERSION 3.13)

include(pico_sdk_import.cmake)
project(t4 C CXX ASM)

set(CMAKE_C_STANDARD 11)
set(CMAKE_CXX_STANDARD 17)

pico_sdk_init()

include_directories(${CMAKE_SOURCE_DIR})

add_executable(t4
  t4.S
)

pico_enable_stdio_uart(t4 1)
pico_enable_stdio_usb(t4 1)

pico_add_extra_outputs(t4)

target_link_libraries(t4 pico_stdlib)
