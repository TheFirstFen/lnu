# Readme

## s

### l

#### If problems ocure

If path needes to be set, run:

``` Powershell

export PICO_SDK_PATH=~/Documents/schoolfolder/year_2/2dt901/Pico_code/pico-sdk

echo $PICO_SDK_PATH

```

Enter the  and then into build. In build run

```Powershell

cmake ..

make

```

View the output in the terminal.

```Powershell

minicom -b 115200 -o -D /dev/ttyACM0

```

Exit with ctrl x and then a .
