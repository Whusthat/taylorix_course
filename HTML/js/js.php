<?php
$site_title = 'js einführung';
include "../assets/layout/header.php";
?>
<div class="wrapper js">
    <h1>JavaScript</h1>
    <div id="myDiv">
        <button class="btn" onclick="document.getElementById('myDiv').innerHTML = 'x'">Button</button>
        <p>onlick event Button</p>
    </div>
    <div id="myDiv2">
        <button class="btn" id="myBtn" onclick="foo();">Button</button>
        <p>Inline Script</p>
    </div>
    <div id="myDiv3">
        <button class="btn" id="myBtn">Button</button>
        <p>Extern js File</p>
    </div>
    <div id="myDiv4">
        
    </div>
</div>

<?php
include "../assets/layout/footer.php"
?>