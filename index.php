<!DOCTYPE html>
<html>
    <head>
	<title>Guardian</title>
        <meta charset="UTF-8"/>
        <meta http-equiv="refresh" content="5"/>
        <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
	<link href="static/style.css" rel="stylesheet" type="text/css"/>
        <script src="static/js_changer.js" language="javascript"/>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>GUARDIAN</h1>
                <h2>Home Automation System</h2>
            </div>
            <div class="block">
            <?php
                $pins = array(0,1,2,3,4,5,6,29);
                for($i=0; $i<8; $i++){
                    system("gpio mode ".$pins[$i]." out");
                    exec("gpio read ".$pins[$i], $status);
                    if($status[$i] == 0){
                        echo "<img src='static/off.png' alt='on/off' id='$i' onclick='process($i)'/>";
                    }
                    elseif($status[$i] == 1){
                        echo "<img src='static/on.png' alt='on/off' id='$i' onclick='process($i)'/>";
                    }
                }
            ?>
            </div>
        </div>
    </body>
</html>
