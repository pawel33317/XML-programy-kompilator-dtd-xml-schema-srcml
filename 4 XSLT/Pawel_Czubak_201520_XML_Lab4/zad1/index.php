<?php
// Added function for  Example #1 

/** Load an XML file and create a DOMDocument.
Handles arbitrary entities, even undefined ones.
*/
function fileToDOMDoc($filename) {
    $dom= new DOMDocument;
    $xmldata = file_get_contents($filename);
    $xmldata = str_replace("&", "&amp;", $xmldata);  // disguise &s going IN to loadXML()

    $dom->substituteEntities = true;  // collapse &s going OUT to transformToXML()
    $dom->loadXML($xmldata);
    return $dom;
}

// Compare with  Example #1 Transforming to a string

// Load the XML sources
$xml = fileToDOMDoc('info.xml');
$xsl = fileToDOMDoc('info.xsl');

// Configure the transformer
$proc = new XSLTProcessor;
$proc->importStyleSheet($xsl);

// transform $xml according to the stylesheet $xsl
file_put_contents('info.html', $proc->transformToXML($xml));
echo $proc->transformToXML($xml); // transform the data

?>