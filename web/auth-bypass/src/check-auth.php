<?php
session_start();

$username = $_POST['username'];
$userPass = $_POST['password'];

$hash = hash('sha256', $userPass);

//credentiels jerry
$hashJerry = 'dbbeabb62778ade84ff87a8bc39165ca83299d9475b53ef0e4020d91d0c21b01';
$jerryUsrName = 'jerry';

//credentiels tom
$hashTom = '2baa7bd4ad4e1f7ae308e217d2f881438b79956a9be6292beba7d32de48581d7';
$tomUsrName = 'tom';

//Verification
if($username==$tomUsrName && $hash==$hashTom){
    echo "goo!!";
    header("Refresh: 1.5; url=tom.php");
    exit;
}

elseif($username==$jerryUsrName && $hash==$hashJerry){
    echo "goo!!";
    header("Refresh: 1.5; url=jerry.php");
    exit;
}

else{
    echo "Username ou Mot de passe incorrect. Essayez encore";

    exit;
}

?>