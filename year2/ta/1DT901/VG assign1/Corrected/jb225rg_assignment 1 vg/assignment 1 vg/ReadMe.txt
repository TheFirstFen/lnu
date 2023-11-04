
sumofthree.py - Jag valde att dela upp det tresiffriga talet i tre olika variabler. en för
                100 - talet, en för 10 - talet och en för entalet. Det gjorde jag genom att 
                dela det jämnt med 100 och 10 och även använda modulus för att få fram talen.
                Sen var det bara att addera dem tillsammans.

change.py - Jag började med att subtrahera priset med betalningamängden för att få fram vad 
            man ska få tillbaka. Därefter delade jag jämnt (//) med de olika mängderna (1000, 
            500, 200, m.m.) för att få fram hur många av vadera sedel/ mynt man skulle få 
            tillbaka. Efter den större sedelns antal var beräknat så använde jag modulus för 
            att få fram den resterande summan växel. Sen var det bara att skriva ut resultatet.

tax.py - Det finns definitivs mer effektiva lösningar till problemet än vad jag gjorde. Jag
         löste det med en if-sats. Om det är lägre än 38000kr beräknas den skatten. Om det är
         mellan 38000 och 50000kr så räknas den skatten på de första 38000 kronorna och sedan
         på resterande. Och om det var över 50000kr så räknades de första två skattegrupperna 
         ut flrst och sen den resterande mängden över 50000.

squarecolour.py - Jag valde att skapa nya variaber, en för bokstaven och en för siffran. 
                  Därefter valde jag att först kolla på bokstaven för att se om det var en rad
                  som började med en svart eller vit ruta. Sen kolla siffran för att se om den
                  var sjämn eller udda för att bestämma färgen på platsen på just den raden.