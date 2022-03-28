## JavaScript

#### JavaScript einbinden

Direkt in Eventlistener vom Dokument
<button onlick="function();"></button>

Inline JavaScript

<script>
console.log('Hello World!')
</script>

Einbinden von JavaScript.js file

<script type="text/javascript" src="/pfad/zum/skript.js"></script>

#### JavaScript print

Printet in DevTools in die Konsole

<script>
console.log('Hello World!')
</script>

Öffnet Popup

<script>
aleart('Hello World!')
</script>

#### Deklarieren Variable

```javascript
var a = 3;
let b = 4;
const d = 5;
```

#### Kommentieren

```javascript
// kommentar

/* kommentar */

/*
 * Multi Line
 */
```

Schau dir mal JSDoc an ! bezüglich Dokumentation

#### Operatoren

##### Arithmentische Operatoren (Rechenzeichen)

Remainder (%)
Increment (++)
Decrement (--)
Unary negation ( - )
Unary plus ( + )
Hoch (\*\*)

##### Logische Operatoren

Logical AND ( && )
Logical OR ( || )
Logical NOT ( ! )

##### String Operatoren

```javascript
console.log("my" + "string");
```

##### Vergleichsoperatoren

Equal (==)
Not equal (!=)
Strict equal (===)
Srict not equal (!==)
Greather than (>)
Greather than or equal (>=)
Less than (<)
Less than or equal (<=)

##### Type operators

in operator

```javascript
objectName instanceof objectType;
```

```javascript
var myFun = new Function("5 + 2");
var shape = "round";
var size = 1;
var today = new Date();

typeof myFun; // returns "function"
typeof shape; // returns "string"
typeof size; // returns "number"
typeof today; // returns "object"
typeof dontExist; // returns "undefined"
```

##### Bitweise Operatoren

Bitwise AND (a & b) 
=> Returns a one in each bit position for which the corresponding bits of both operands are ones

| Ausdruck | Ergebnis | Binäre Darstellung |
|----------|----------|--------------------|
| 15 & 9   | 9        | 1111 & 1001 = 1001 |

Bitwise OR (a | b)
=> Returns a zero in each bit position for which the corresponding bits of both operands are zeros

| Ausdruck | Ergebnis | Binäre Darstellung |
|----------|----------|--------------------|
| 15 | 9   | 15       | 1111 | 1001 = 1111 |


Bitwse XOR (a ^ b)
=> Returns a zero in each bit position for which the corresponding bits are the same.
[Returns a one in each bit position for which the corresponding bits are different.]

| Ausdruck | Ergebnis | Binäre Darstellung |
|----------|----------|--------------------|
| 15 ^ 9   | 6        | 1111 ^ 1001 = 0110 |

