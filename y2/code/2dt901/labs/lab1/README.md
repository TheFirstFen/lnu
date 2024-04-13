# Lab 1

## Samuel Berg &

### Task 1

```LEGv8
movz x0, #5
movz x1, #10
addi x1, x1, #2
add x2, x0, x1
```

Value in `x2` = 17

### Task 2

```Binary || Hex : LEGv8
11010010100 0000000010000000 00010 : movz x2, #0x80

11010010100 0000000011100111 00100 : movz x4, #0xe7

11001011000 00010 000000 00100 00101 : sub x5, x4, x2

D360 0CA5 : 11010011011 00000 000011 00101 00101 : lsl x5, x5, 3
```

Resulting in following exectution:

```LEGv8
movz x2, #0x80
movz x4, #0xe7
sub x5, x4, x2
lsl x5, x5, 3
```

### Task 3

```LEGv8

```

### Task 4

### Task 5

### Task 6

### Task 7
