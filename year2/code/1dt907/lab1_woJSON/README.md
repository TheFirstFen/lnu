# Lab 1

## Problem 4

Notes: Analys av UF, Vanlig bör gå mot linjär tid medans de andra går mot konstant tid

Den vanliga UnionFind verkar gå mot en linjär tidkomplexitet medans den andra verkar gå mot en konstant tidskomplexitet. Vi vet dock att den inte är konstant.

## Problem 7

Notes: Formel och värden för computed bör gå mot exponent av 3 för brute

B values (exponenten):

fitted Bf: `3.156849570357424` TP: `2.589666968918421`

computed Bf: `2.7555222203420464` TP: `1.622885880852076`

A values:

fitted Bf: `9.620923278880196e-11` TP: `3.1106785891057227e-11`

computed Bf: `-27.930453063895982` TP: `-21.89939875613408`

Formler för computed:

B values = (bC): `(log2(y(x1)) - log2(y(x0))) / (log2(x1) - log2(x0))`

A values = (aC): `log2(y(x)) - cB * log2(x)`

Funktioner:

Fitted: `a * x^b`

Computed: `(x * 2^(aC / bC))^bC`

## Problem 8

Notes: antal exp, matris storlek, threshhold värde går vi mot?

Antal experiment: `100`
Matris storleken n för nxn matris: `100`

ger de följande värdena:
Mean time taken: `3.3357 ms`
Mean percolation threshold: `0.5924300000000001 ± 0.017041437910593284`
Standard deviation: `0.017041437910593284`

Detta ger oss att threshold:et går mot ca `0.5924`.
