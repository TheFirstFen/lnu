cmake_minimum_required(VERSION 3.13)

include(pico_sdk_import.cmake)
project(taskFive C CXX ASM)

set(CMAKE_C_STANDARD 11)
set(CMAKE_CXX_STANDARD 17)

pico_sdk_init()

include_directories(${CMAKE_SOURCE_DIR})

add_executable(taskFive
  taskFive.S
)

pico_enable_stdio_uart(taskFive 1)
pico_enable_stdio_usb(taskFive 1)

pico_add_extra_outputs(taskFive)

target_link_libraries(taskFive pico_stdlib)
