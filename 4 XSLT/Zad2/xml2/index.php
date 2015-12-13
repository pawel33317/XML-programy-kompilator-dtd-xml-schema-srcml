 <html>
<head>
<script>
function loadXMLDoc(filename){
	xhttp = new XMLHttpRequest();
	xhttp.open("GET", filename, false);
	try {xhttp.responseType = "msxml-document"} catch(err) {}
	xhttp.send("");
	return xhttp.responseXML;
}
function displayResult(){
xml1 = loadXMLDoc("cities.xml");
xsl1 = loadXMLDoc("cities.xsl");

	if (document.implementation && document.implementation.createDocument){
		xsltProcessor = new XSLTProcessor();
		xsltProcessor.importStylesheet(xsl1);
		resultDocument = xsltProcessor.transformToFragment(xml1, document);
		document.getElementById("menuu").appendChild(resultDocument);
	}
	<?php
	if(isset($_GET['id'])){
		echo 'showOne('.$_GET['id'].');';	
	}
	?>
}
/*function showE(){
	xml2 = loadXMLDoc("citiesE.xml");
	xsl2 = loadXMLDoc("citiesE.xsl");
	if (document.implementation && document.implementation.createDocument){
		xsltProcessor = new XSLTProcessor();
		xsltProcessor.importStylesheet(xsl2);
		xsltProcessor
		resultDocument2 = xsltProcessor.transformToFragment(xml2, document);
		document.getElementById("content").appendChild(resultDocument2);
	}
}*/
function showOne(par){
	xml2 = loadXMLDoc("citiesE.xml");
	xsl2 = loadXMLDoc("citiesE.xsl");
	if (document.implementation && document.implementation.createDocument){
		xsltProcessor = new XSLTProcessor();
		xsltProcessor.setParameter(null, "cityID", par);
		xsltProcessor.importStylesheet(xsl2);
		xsltProcessor.setParameter(null, "cityID", par);
		resultDocument2 = xsltProcessor.transformToFragment(xml2, document);
		document.getElementById("content").appendChild(resultDocument2);
	}

}
</script>
</head>
<body onload="displayResult()">
<p><img src="s3.png"/><a>Wybierz interesujace Cie miasto aby zobaczyc szerszy opis drogowy</a></p>
	<div id="menuu" style="width:10%; float:left;"> </div>
	<div id="content" style="width:70%; float:left;"></div>
</body>
</html>