<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
	<xsl:template match="/">
<html>
<head><meta charset="UTF-8"/></head>
	<body style="font-family:calibri">
		<h2><img src="s4.png"/>Informacje drogowe</h2>
		<xsl:for-each select="INFORMATIONS/INFO">
		<xsl:sort select="CREATE_DATE"/>
			<article>
				<header>
					<strong>
						<a href="infoE.xml"><xsl:value-of select="HEADER"/></a>
					</strong> 
					<details style="font-size:11px; padding-left:10px;">
						<xsl:value-of select="CREATE_DATE"/>
					</details>
				</header>
				
				<section maxlength="20">
					<xsl:value-of select="substring(TEXT, 1, 200)"/>...
				</section>
			</article><br/>
		</xsl:for-each>
	</body>
</html>
	</xsl:template>
</xsl:stylesheet>

