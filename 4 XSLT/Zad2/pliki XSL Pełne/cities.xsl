<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
	<xsl:template match="/">
<html>
	<body style="font-family:calibri">
		<p><img src="s3.png"/>Wybierz interesujęce Cię miasto aby zobaczyć szerszy opis drogowy</p>
		<nav>
		<xsl:for-each select="CITIES/CITY">
			&#187;<a href="index.php" style="font-size:20px; font-weight:bold;"><xsl:value-of select="NAME"/></a>
			<br/>
		</xsl:for-each>
		</nav>
	</body>
</html>
	</xsl:template>
</xsl:stylesheet>

