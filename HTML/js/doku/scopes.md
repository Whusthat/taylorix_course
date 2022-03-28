## Scopes

```javascript
x = 3;

const foo = () => {
  x = 5;
  console.log(x); // 5
};

const foo2 = () => {
  console.log(x); // 3
};
```
