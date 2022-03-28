// Init on pageload
let before_loadtime = new Date().getTime();
window.onload = () => {
  let page_load_container = document.getElementById("page-load");
  let after_loadtime = new Date().getTime();
  let time_to_load_page = (after_loadtime - before_loadtime) / 1000;
  page_load_container.innerHTML = "Buildtime: " + time_to_load_page + " sek";
};

window.onload = () => {
  let wrapper = document.querySelector(".wrapper.js");
  if (wrapper) {
    let btn = document.querySelector("#myDiv3 .btn");
    let div = document.getElementById("myDiv3");
    btn.addEventListener("click", function () {
      div.innerHTML = "x";
    });

    function foo3() {
      document.write("Hallo Welt!");
    }

    let btn1 = document.querySelector("#myDiv4 .btn");

    btn1.addEventListener("click", small1x1);
  } else {
    console.log("no js wrapper");
  }
};

const small1x1 = () => {
  for (i = 1; i <= 10; i++) {
    for (j = 1; j <= 10; j++) {
      let btn1 = document.querySelector("#myDiv4 .btn");
      let div2 = document.getElementById("content");
      div2.innerHTML += `${i} * ${j} = ` + i * j + "<br>";
    }
  }
};

// Uebung 1
/*
window.onload = () => {
  let container = document.getElementById('test');
  let erg = document.getElementById('ergebnis');
  const create_buttons = (n) =>{
    for (i=1; i<n ; i++){
      container.innerHTML += `<button class="btn-test">${i}</button>`
    }
    let buttons = document.querySelectorAll('.btn-test');
    
    for (let i = 0, len = buttons.length; i < len; i++){
      buttons[i].addEventListener('click', function(){
            let number = buttons[i].innerHTML
            erg.innerHTML = number **2
      });
    }

  }
  create_buttons(100)
};
*/

// Uebung 2

const get_op = (str, num1, num2) => {
  if (str == "-") {
    console.log(str);
    return num1 - num2;
  } else if (str == "+") {
    return num1 + num2;
  } else if (str == "*") {
    return num1 * num2;
  } else {
    return num1 / num2;
  }
};
/*
let current_erg = 0;
let number1 = 0;
let number2 = 0;
let math_op = "";
let flag = false
const calc = (elem) => {
  let btn_type = elem.getAttribute("type");
  let btn_value = elem.getAttribute("value");
  let calc_erg = document.getElementById("calc-result");
 

  if (current_erg == 0 && btn_type == "number") {
    current_erg = btn_value;
    calc_erg.innerHTML = current_erg;
    console.log(current_erg);
  } else if (btn_type == "number") {
    current_erg += btn_value;
    calc_erg.innerHTML += btn_value;
    console.log(current_erg);
  } else if (btn_type == "operator" && !flag) {
    number1 = current_erg;
    math_op = btn_value;
    current_erg = 0;
    calc_erg.innerHTML = 0;

  }else if (btn_type == 'operator' && flag){
    math_op = btn_value
    let result = get_op(math_op, number1, number2);
    calc_erg.innerHTML = result;
    number1 = result
    current_erg = 0
    number2 = 0
  } 
  else if (btn_type == "return") {
    number2 = current_erg;
    let result = get_op(math_op, number1, number2);
    calc_erg.innerHTML = result;
    flag = true
    number1 = result
    current_erg = 0
    number2 = 0
  }
};
*/

const updateScreen = (btn_value, override) => {
  let calc_erg = document.getElementById("calc-result");
  if (calc_erg.innerHTML == 0 || !override) {
    calc_erg.innerHTML = btn_value;
  } else {
    calc_erg.innerHTML += btn_value;
  }

};

const clearScreen = () => {
  calc_erg = document.getElementById("calc-result").innerHTML = 0;
};

const calc = (ele) => {
  btn_value = ele.getAttribute("value");
  btn_type = ele.getAttribute("type");

  if (btn_type == "number" || btn_type == "operator") {
    updateScreen(btn_value, true);
  }

  if (btn_type == "return") {
    let erg = document.getElementById("calc-result").innerHTML;
    let history = document.getElementById("history");
    let historyItem = document.createElement("span");
    historyItem.innerHTML = erg + " = " + eval(erg);
    history.append(historyItem);
    erg = eval(erg);
    history.style.display = "block";
    updateScreen(erg, false);
  }
};
