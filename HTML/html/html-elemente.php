<?php
$site_title = 'htlm-elemente';
include "../assets/layout/header.php";
?>
<div class="wrapper">
    <h2>Übersicht HTML-Elemente</h2>
    <h1>Headline h1</h1>
    <h2>Headline h2</h2>
    <h3>Headline h3</h3>
    <h4>Headline h4</h4>
    <h5>Headline h5</h5>
    <h6>Headline h6</h6>
    <p>paragraph</p>
    <a href="https://www.tutorialgarage.com/html5-css3-kurs/html-grundlagen" target="_target">Link zu TuT</a>
    <div class="image-wrapper">
        <img src="/assets/media/html-elemente-erklaert.jpg" alt="html-elemente-erklaert">
    </div>
    <p><b>Bold</b></p>
    <p><strong>Strong</strong></p>
    <p><i>Italic</i></p>
    <p><em>Emphasized</em></p>
    <p><del>Done</del></p>
    <blockquote cite="https://www.google.de">
        <p>Zitat</p>
        <cite>
            <a href="https://www.google.de">Zitat Link</a>
        </cite>
    </blockquote>
    <button><a href="https://google.de">Button</a></button>
</div>
<?php
include "../assets/layout/footer.php";
?>