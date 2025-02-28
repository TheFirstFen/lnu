# Distributed under the OSI-approved BSD 3-Clause License.  See accompanying
# file Copyright.txt or https://cmake.org/licensing for details.

cmake_minimum_required(VERSION 3.5)

file(MAKE_DIRECTORY
  "/home/voldemort/sdk-pico/pico-sdk/tools/elf2uf2"
  "/home/voldemort/lnu/y2/code/2dt901/labs/lab3/t1/build/elf2uf2"
  "/home/voldemort/lnu/y2/code/2dt901/labs/lab3/t1/build/elf2uf2"
  "/home/voldemort/lnu/y2/code/2dt901/labs/lab3/t1/build/elf2uf2/tmp"
  "/home/voldemort/lnu/y2/code/2dt901/labs/lab3/t1/build/elf2uf2/src/ELF2UF2Build-stamp"
  "/home/voldemort/lnu/y2/code/2dt901/labs/lab3/t1/build/elf2uf2/src"
  "/home/voldemort/lnu/y2/code/2dt901/labs/lab3/t1/build/elf2uf2/src/ELF2UF2Build-stamp"
)

set(configSubDirs )
foreach(subDir IN LISTS configSubDirs)
    file(MAKE_DIRECTORY "/home/voldemort/lnu/y2/code/2dt901/labs/lab3/t1/build/elf2uf2/src/ELF2UF2Build-stamp/${subDir}")
endforeach()
if(cfgdir)
  file(MAKE_DIRECTORY "/home/voldemort/lnu/y2/code/2dt901/labs/lab3/t1/build/elf2uf2/src/ELF2UF2Build-stamp${cfgdir}") # cfgdir has leading slash
endif()
