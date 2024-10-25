# Distributed under the OSI-approved BSD 3-Clause License.  See accompanying
# file Copyright.txt or https://cmake.org/licensing for details.

cmake_minimum_required(VERSION 3.5)

file(MAKE_DIRECTORY
  "/home/voldemort/sdk-pico/pico-sdk/tools/pioasm"
  "/home/voldemort/lnu/y2/code/2dt901/labs/lab4/t3/build/pioasm"
  "/home/voldemort/lnu/y2/code/2dt901/labs/lab4/t3/build/pico-sdk/src/rp2_common/pico_cyw43_driver/pioasm"
  "/home/voldemort/lnu/y2/code/2dt901/labs/lab4/t3/build/pico-sdk/src/rp2_common/pico_cyw43_driver/pioasm/tmp"
  "/home/voldemort/lnu/y2/code/2dt901/labs/lab4/t3/build/pico-sdk/src/rp2_common/pico_cyw43_driver/pioasm/src/PioasmBuild-stamp"
  "/home/voldemort/lnu/y2/code/2dt901/labs/lab4/t3/build/pico-sdk/src/rp2_common/pico_cyw43_driver/pioasm/src"
  "/home/voldemort/lnu/y2/code/2dt901/labs/lab4/t3/build/pico-sdk/src/rp2_common/pico_cyw43_driver/pioasm/src/PioasmBuild-stamp"
)

set(configSubDirs )
foreach(subDir IN LISTS configSubDirs)
    file(MAKE_DIRECTORY "/home/voldemort/lnu/y2/code/2dt901/labs/lab4/t3/build/pico-sdk/src/rp2_common/pico_cyw43_driver/pioasm/src/PioasmBuild-stamp/${subDir}")
endforeach()
if(cfgdir)
  file(MAKE_DIRECTORY "/home/voldemort/lnu/y2/code/2dt901/labs/lab4/t3/build/pico-sdk/src/rp2_common/pico_cyw43_driver/pioasm/src/PioasmBuild-stamp${cfgdir}") # cfgdir has leading slash
endif()
