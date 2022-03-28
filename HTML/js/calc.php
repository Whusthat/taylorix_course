<?php
$site_title = 'Uebung Taschenrechner';
include "../assets/layout/header.php";
?>
<div class="wrapper">
    <div id="calc-frame">
        <div id="calc-result">
            0
        </div>
        <div class="calc-btns">
            <button class="calc-btn" value="1" onclick="calc(this)" type="number">1</button>
            <button class="calc-btn" value="2" onclick="calc(this)" type="number">2</button>
            <button class="calc-btn" value="3" onclick="calc(this)" type="number">3</button>
            <button class="calc-btn" value="4" onclick="calc(this)" type="number">4</button>
            <button class="calc-btn" value="5" onclick="calc(this)" type="number">5</button>
            <button class="calc-btn" value="6" onclick="calc(this)" type="number">6</button>
            <button class="calc-btn" value="7" onclick="calc(this)" type="number">7</button>
            <button class="calc-btn" value="8" onclick="calc(this)" type="number">8</button>
            <button class="calc-btn" value="9" onclick="calc(this)" type="number">9</button>
            <button class="calc-btn" value="0" onclick="calc(this)" type="number">0</button>
            <button class="calc-btn" value="+" onclick="calc(this)" type="operator">+</button>
            <button class="calc-btn" value="-" onclick="calc(this)" type="operator">-</button>
            <button class="calc-btn" value="*" onclick="calc(this)" type="operator">*</button>
            <button class="calc-btn" value="/" onclick="calc(this)" type="operator">/</button>
            <button class="calc-btn" value="=" onclick="calc(this)" type="return">=</button>
            <button class="calc-btn" value="=" onclick="clearScreen()">clear</button>
        </div>
        <div id="history">

        </div>
    </div>
</div>

<?php
include "../assets/layout/footer.php"
?>