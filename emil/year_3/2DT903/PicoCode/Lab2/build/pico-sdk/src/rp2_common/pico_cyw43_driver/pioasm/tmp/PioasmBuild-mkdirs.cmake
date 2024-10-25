# Distributed under the OSI-approved BSD 3-Clause License.  See accompanying
# file Copyright.txt or https://cmake.org/licensing for details.

cmake_minimum_required(VERSION 3.5)

file(MAKE_DIRECTORY
  "/home/emil/Documents/schoolfolder/year_2/2dt901/Pico_code/pico-sdk/tools/pioasm"
  "/home/emil/Documents/schoolfolder/year_3/2DT903/PicoCode/Lab2/build/pioasm"
  "/home/emil/Documents/schoolfolder/year_3/2DT903/PicoCode/Lab2/build/pico-sdk/src/rp2_common/pico_cyw43_driver/pioasm"
  "/home/emil/Documents/schoolfolder/year_3/2DT903/PicoCode/Lab2/build/pico-sdk/src/rp2_common/pico_cyw43_driver/pioasm/tmp"
  "/home/emil/Documents/schoolfolder/year_3/2DT903/PicoCode/Lab2/build/pico-sdk/src/rp2_common/pico_cyw43_driver/pioasm/src/PioasmBuild-stamp"
  "/home/emil/Documents/schoolfolder/year_3/2DT903/PicoCode/Lab2/build/pico-sdk/src/rp2_common/pico_cyw43_driver/pioasm/src"
  "/home/emil/Documents/schoolfolder/year_3/2DT903/PicoCode/Lab2/build/pico-sdk/src/rp2_common/pico_cyw43_driver/pioasm/src/PioasmBuild-stamp"
)

set(configSubDirs )
foreach(subDir IN LISTS configSubDirs)
    file(MAKE_DIRECTORY "/home/emil/Documents/schoolfolder/year_3/2DT903/PicoCode/Lab2/build/pico-sdk/src/rp2_common/pico_cyw43_driver/pioasm/src/PioasmBuild-stamp/${subDir}")
endforeach()
if(cfgdir)
  file(MAKE_DIRECTORY "/home/emil/Documents/schoolfolder/year_3/2DT903/PicoCode/Lab2/build/pico-sdk/src/rp2_common/pico_cyw43_driver/pioasm/src/PioasmBuild-stamp${cfgdir}") # cfgdir has leading slash
endif()
