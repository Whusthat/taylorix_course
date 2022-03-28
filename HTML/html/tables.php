<?php
$site_title = 'tabellen';
include "../assets/layout/header.php";
?>
<div class="wrapper">
    <h2 style="padding:10px 0;">Tabellen</h2 style="padding:10px 0;">
    <table>
        <tr>
            <th>Erste Spalte</th>
            <th>Zweite Spalte</th>
        </tr>
        <tr>
            <td>1/2</td>
            <td>2/2</td>
        </tr>
        <tr>
            <td>1/2</td>
            <td>2/2</td>
        </tr>
    </table>

    <h2 style="padding:10px 0;">Tabellen Colspan</h2 style="padding:10px 0;">
    <table>
        <tr>
            <th colspan="2">Verbundene Table-Header</th>
        </tr>
        <tr>
            <td>1/2</td>
            <td>2/2</td>
        </tr>
        <tr>
            <td>1/2</td>
            <td>2/2</td>
        </tr>
    </table>

    <h2 style="padding:10px 0;">Tabellen Rowspan</h2 style="padding:10px 0;">
    <table>
        <tr>
            <th>Erste Spalte</th>
            <th>Zweite Spalte</th>
        </tr>
        <tr>
            <td rowspan="2">1/2</td>
            <td>2/2</td>
        </tr>
        <tr>
            <td>2/2</td>
        </tr>
    </table>

    <h2 style="padding:10px 0;">Tabellen Row Zebra Muster</h2 style="padding:10px 0;">
    <table id="zebra-table">
        <tr>
            <th>Erste Spalte</th>
            <th>Zweite Spalte</th>
        </tr>
        <tr>
            <td>1/2</td>
            <td>2/2</td>
        </tr>
        <tr>
            <td>1/2</td>
            <td>2/2</td>
        </tr>
        <tr>
            <td>1/2</td>
            <td>2/2</td>
        </tr>
    </table>

</div>
<?php
include "../assets/layout/footer.php";
?>