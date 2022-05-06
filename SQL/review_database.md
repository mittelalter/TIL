# About how to review the database

contents
> * common concepts
> * common functions, sentences
> * useful method

## Common concepts

### Wie werden Primary Key und Natural Key, Surrogate Key definiert?
-Primary ist, womit man das einzelne Data unterscheiden kann. Eine Reihe hat eignes Primary key. Damit verhindert DBMS gleiche Daten zu speichern was schon gespeichert ist.
-Natural Key ist, womit es sich unterscheidet z.B email Adresse oder Personal Nummer hat man nur eignes. Aber diese können auch geändert werden. Deswegen wird es häufig Surrogate Key benutzt um Primary Key set up zu machen.


### Wie funktioniert SQL?
-Nach der Rehinfolge. Also FROM, WHERE, GROUP BY, HAVING, SELECT, ORDER BY, LIMIT
-Erst mit FROM kann man das Datatable rufen, was man haben will
-Mit WHERE kann man die bestimmte Daten haben mit den Vorraussetzungen, die man geschreiben haben.
-Und mit GROUP BY werden die Daten grouppiert z.B Mann und Frau
-Mit HAVING kann man die Datengruppen bestimmt auswählen, die zu den Vorraussetzungen passen.
-ORDER BY sortiert die Daten 
-Zum Schuluss wenn man nur bestimmt Daten Menge sehen will, kann man das mit LIMIT erfolgen. Z.b nur 10 Reihe 


### Was ist der Unterschied zwischen JOIN UND UNION?
-LEFT, RIGHT, INNER JOIN funktionieren nach horizontale Richtung quasie nach Reihe. (assoziative Operation, der Standard ist Reihe)
Aber UNION ist andersrum. Nach vertikale Richtung also nach Column. Damit kann man mehere Data Table zusammen vereinigen und wenn es Daten gibt die sich uberschneidet, wird nur eine Reihe gezeight. Man kann das mit UNION ALL verhindern. 
Und wichtig ist, man kann UNION benutzen nur wenn das Struktur von den Table gleich sind.