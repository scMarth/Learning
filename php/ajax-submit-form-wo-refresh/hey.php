<html>
    <head>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
        <script>
            function chk()
            {
                var fname = document.getElementById('fname').value;
                var lname = document.getElementById('lname').value;
                var dataString = 'fname=' + fname + "&lname=" + lname;
                $.ajax({
                    type: "post",
                    url: "hi.php",
                    data: dataString,
                    cache: false,
                    success: function(html){
                        $('#msg').html(html);
                    }
                });
                return false;
            }
        </script>
    </head>
    <body>
        <form>
            <input type="text" id="fname">
            <br><br>
            <input type="text" id="lname">
            <br><br>
            <input type="submit" id="submit" value="submit" onclick="return chk()">
        </form>
        <p id="msg"></p>
    </body>
</html>