<?php
$site_title = 'CSS';
include "../assets/layout/header.php";
?>
<div class="wrapper">
    <h2>Einführung CSS</h2>
    <p>Order of styles is:<br> Inline > Intern > Extern<br> ID > Class</p>

    <h3>Inline Style</h3>
    <div style="background-color: lightgray;">
        <p>Erste DIV</p>
    </div>

    <h3>Internal Style</h3>
    <div>
        <p>Zweite DIV</p>
    </div>

    <h3>Extern Styles</h3>
    <div id="foo">
        <p class="class-1">Dritte DIV</p>
        <p>id="foo"</p>
        <p>#foo{background-color: aquamarine;}</p>
    </div>
</div>

<?php
include "../assets/layout/footer.php"
?>