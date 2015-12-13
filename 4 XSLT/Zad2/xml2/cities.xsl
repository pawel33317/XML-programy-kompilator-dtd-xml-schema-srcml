<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
	<xsl:template match="/">
		<nav>
		<xsl:for-each select="CITIES/CITY">
			&#187;<a href="index.php?id={./@id}" style="font-size:20px; font-weight:bold;" onclick="showE()"><xsl:value-of select="NAME"/></a>
			<br/>
		</xsl:for-each>
		</nav>
	</xsl:template>
</xsl:stylesheet>

