<?php
$site_title = 'Bootstrap-Einführung';
include "../assets/layout/header.php"
?>
<!-- Content -->
  <div class="row" style="background-color: red">
    <div class="col-12">col-12</div>
  </div>
  <div class="row">
    <div class="col-3" style="background-color: yellow">col-3</div>
    <div class="col-9">
      <div class="row">
        <div class="col-6" style="background-color: blue; height:200px;">col-6</div>
        <div class="col-6" style="background-color: green">col-6</div>
      </div>
      <div class="row" style="background-color: rgb(216, 212, 212);">
        <div class="col-12">
          col-12
        </div>
      </div>
    </div>
    <div class="row" style="background-color: rgb(131, 78, 78);">
      <div class="col-12">
        col-12
      </div>
    </div>
<!-- Footer -->
<?php include "../assets/layout/footer.php"?>