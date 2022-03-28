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

    for (i = 1; i <= 10; i++) {
      for (j = 1; j <= 10; j++) {
        let div4 = document.getElementById("myDiv4");
        div4.innerHTML += `${i} * ${j} = ` + i * j + "<br>";
      }
    }
  } else {
    console.log("no js wrapper");
  }
};
