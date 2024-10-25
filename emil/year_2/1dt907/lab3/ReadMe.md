# Programmerings uppgift 3

## 1dt907 Algoritmer

### Emil Ulvagården (eu222dq)

#### Run the program

```Powershell
cd .\Algoritmer\

javac *.java

cd ..

javac *.java 

java Main.java
```

#### Uppgift 4

| Vertices\Time  | edges     | Dijkstra time | Bellman-Ford time |
|----------------|-----------|---------------|-------------------|
| 1000           | 2000      | 9.059 ms      | 32.085 ms         |
| 2000           | 4000      | 8.430 ms      | 87.537 ms         |
| 3000           | 6000      | 12.561 ms     | 213.942 ms        |
| 4000           | 8000      | 16.443 ms     | 288.837 ms        |
| 5000           | 10000     | 24.473 ms     | 581.353 ms        |
| 6000           | 12000     | 43.394 ms     | 1125.275 ms       |
| 7000           | 14000     | 55.067 ms     | 1157.870 ms       |
| 8000           | 16000     | 52.969 ms     | 1562.318 ms       |
| 9000           | 18000     | 63.308 ms     | 1521.032 ms       |
| 10000          | 20000     | 85.927 ms     | 3233.905 ms       |

| Algoritm  | Dijkstra  | Bellman-Ford |
|-----------|-----------|--------------|
| times won |   10      |     10       |

Som syns ovan är Dijkstras algoritm efferktivare på att hitta den lättaste vägen från 1 vertex till alla andra sammankopplade vertices. Dijkstra är en girig algoritm som utgår ifrån att den lättaste vägen i första alternativet alltid är den lättaste vägen till den vertexen. Bellman-Ford gör inte denna antagelse utan går igenom alla vertices och kollar alla deras edges för att se om det finns lättare vägar att markera. När Bellman-Ford väl har kollat alla vertices en gång så börjar den om på nytt och gör detta tills den inte längre hittare en lättare väg eller fastnar i en oändligt negativ loop och då avslutar den. Bellman-Ford tar därför längre tid på sig än vad dijkstras algoritm gör.

Trots att Bellman-Fords algoritm är långsammare än Dijkstras algoritm finns det fortfarande anledningar till dess användning. En anledning är att den kan hantera grafer med negativa vikter och den hittar den absolut kortaste vägen från en start vertex till alla andra vertices till skillnad från Dijkstra som kan hitta den absolut kortaste vägen men det är inte en garanti.
