<?php 
global $mysqli;
$mysqli = mysqli_connect("127.0.0.1", "root", "", "xml6");

$file = "data.xml"; 
$xml = new DOMDocument(); 
$xml->load($file); 

//Walidacja poprawności .xml z .xds
if (!$xml->schemaValidate('data.xsd')) {
    echo '<h1>Dokument niepoprawny</h1>';
}else{
	echo '<h1>Dokument poprawny</h1>';
}

//info o poprawności
echo "<h2>".$file."</h2>\n"; 
echo "<pre>"; 

global $inTag; 
$inTag = ""; 

//ustawienie parsera
$xml_parser = xml_parser_create(); 
xml_parser_set_option($xml_parser, XML_OPTION_CASE_FOLDING, 0); 
xml_set_element_handler($xml_parser, "startElement", "endElement"); 

//odczyt pliku fragmentami do parsera
$fp = fopen($file, "r");
while ($data = fread($fp, 4096)) { 
   xml_parse($xml_parser, $data, feof($fp));
}

//zakończenie parsera
xml_parser_free($xml_parser); 

//wyświetla start tagi i attrybuty
function startElement($parser, $name, $attrs) { 
    global $inTag; 
    global $depth;  
	//jeżeli tag za który mamy coś podstawić
	if (substr($name,0,3) == 'jt:'){
		if (!($inTag == "")) { 
			echo "&gt;"; 
		} 
		$inTag = $name; 
		$depth++; 
		handleJSelement(substr($name,3), $attrs,str_repeat(str_pad(" ", 3), $depth));
	}
	//jeżeli zwykły tag
	else {
		$padTag = str_repeat(str_pad(" ", 3), $depth); 
		if (!($inTag == "")) { 
			echo "&gt;"; 
		} 
		echo "\n$padTag&lt;$name"; 
		foreach ($attrs as $key => $value) { 
			echo "\n$padTag".str_pad(" ", 3); 
			echo " $key=\"$value\""; 
		} 
		$inTag = $name; 
		$depth++; 
	}
}

//tagi zakańczające
function endElement($parser, $name) { 
    global $depth; 
    global $inTag; 
    global $closeTag;     
    $depth--; 
	if( substr($name,0,3) == 'jt:'){
		$inTag = ""; 
	}
	else{
	    if ($closeTag == TRUE) { 
		    echo "&lt/$name&gt;"; 
		    $inTag = ""; 
	    } elseif ($inTag == $name ) { 
		    echo " /&gt;"; 
		    $inTag = ""; 
	    } else { 
			$padTag = str_repeat(str_pad(" ", 3), $depth); 
		    echo "\n$padTag&lt/$name&gt;"; 
		} 
	}	
} 



function handleJSelement($type, $attrs,$padd){
	global $mysqli;
	if ($type=='title'){
		$result = $mysqli->query("SELECT * FROM title where page = '".$attrs['page']."' limit 10 ");
		while ($row = $result->fetch_assoc()) {
			echo "\n$padd&lt;p&gt;" . $row['title'] . "&lt;/p&gt;";
		}
	}elseif($type=='menu'){
		$result = $mysqli->query("SELECT * FROM menu where type = '".$attrs['type']."' ");
		while ($row = $result->fetch_assoc()) {
			echo "\n$padd&lt;a href=\"".$row['link']."\"&gt;" . $row['label'] . "&lt;/a&gt;";
		}
	}elseif($type=='content'){
		$result = $mysqli->query("SELECT * FROM article limit ".$attrs['limit']);
		while ($row = $result->fetch_assoc()) {
			echo "\n$padd&lt;div>&lt;div class=\"title\">" . $row['title'] . "&lt;/div>&lt;div class=\"article\">" . $row['content'] . "&lt;/div>&lt;div class=\"footer\">featured: ".$row['featured']."&lt;/div>&lt;/div>";
		}
	}elseif($type=='footer'){
		$result = $mysqli->query("SELECT * FROM footer where type='".$attrs['page']."' ");
		while ($row = $result->fetch_assoc()) {
			echo "\n$padd&lt;p&gt;" . $row['title'] . "&lt;/p&gt;";
		}
	}
	//echo "\n+++++++$type++++++++++++\n";
	//var_dump($attrs);
}


echo "</pre>"; 
mysqli_close($mysqli);
?>