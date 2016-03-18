<?php
    if(isset($_GET['pin'])){
        $pins = array(0,1,2,3,4,5,6,29);
        $pin_change = htmlspecialchars(strip_tags($_GET['pin']));
        exec("gpio read ".$pins[$pin_change], $status);
        if($status[0] === "0"){
            $status[0] = 1;
            system("gpio write ".$pins[$pin_change]." ".$status[0]);
            echo "static/on.png";
        }
        elseif($status[0] === "1"){
            $status[0] = 0;
            system("gpio write ".$pins[$pin_change]." ".$status[0]);
            echo "static/off.png";
        }
    }
?>
