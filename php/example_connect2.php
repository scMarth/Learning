<?php
$serverName = "server_name";
$connectionInfo = array("Database"=>"database_name");
$conn = sqlsrv_connect($serverName, $connectionInfo);
if( $conn ) {
    # connection established
    $sql = 'SELECT * FROM table_name';
    $stmt = sqlsrv_query( $conn, $sql );
    if( $stmt === false) {
        die( print_r( sqlsrv_errors(), true) );
    }

    while($row = sqlsrv_fetch_array($stmt, SQLSRV_FETCH_ASSOC)) {
        print_r($row);
        echo '<br><br>';
    }

    sqlsrv_close($conn);
}else{
     echo "Connection could not be established.<br />";
     die( print_r( sqlsrv_errors(), true));
}
?>