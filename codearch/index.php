<html>
<head></head>
<body>
<?PHP
 
//define the path as relative
$path = ".";
 
//using the opendir function
$dir_handle = @OPENDIR($path) or DIE("Unable to open $path");
 
ECHO "Directory Listing of $path<br/>";
 
//running the while loop
WHILE ($file = READDIR($dir_handle)) {
	if($file != "." && $file != "..") {
		ECHO "<a href=$file>$file</a><br/>";
	}
}
 
//closing the directory
CLOSEDIR($dir_handle);
 
?> 
</body>
</html>
