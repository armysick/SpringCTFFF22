<?php
if ($_POST['usernamefld'] == "admin" && $_POST['passwordfld'] == "pfsense"){
  echo "flag{Default?_More_Like_Badfault}";
} else {
  echo "wrong username / password combination";
}

?>


