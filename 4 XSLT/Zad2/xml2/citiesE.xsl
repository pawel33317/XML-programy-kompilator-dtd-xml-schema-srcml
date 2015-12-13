<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:param name="cityID"/>
	<xsl:template match="/">
	
<html>
	<body style="font-family:calibri;">
		<xsl:for-each select="CITIES/CITY[./@id=$cityID]">
		<xsl:sort select="CREATE_DATE"/>
			<article  style="clear:both; padding-bottom:20px;">
				<header>
					<h2 style="padding:0px; margin:0px;"><img src="s2.png"/><strong>&#160;&#160;<xsl:value-of select="NAME"/></strong><xsl:if test="CONFIRMED='false'">&#160;<img src="s1.png"/></xsl:if></h2>
					<details style="font-size:13px;">
						<strong>Autor: </strong><xsl:value-of select="CREATE_ID"/> - <xsl:value-of select="CREATE_DATE"/><br/>
						<strong>Ostatnia aktualizacja: </strong><xsl:value-of select="UPDATE_DATE"/>
					</details>
					<br/><br/>
					<a href="#">[Edytuj opis]</a>
					<br/><br/>
				</header>
				
				<section maxlength="20" style="float:left; width:40%;">
					<xsl:value-of select="TEXT"/>
				</section>
				<section maxlength="20" style="float:left;">
				<table style="border:1px solid grey;">
				<tr style="background-color:grey;"><td>Najbliższy stadion: </td><td><xsl:value-of select="STADIUM"/></td></tr>
				<tr><td>Szacowana odległość: </td><td><xsl:value-of select="KM_STADIUM"/>km</td></tr>
				<tr style="background-color:grey;"><td>Dojazd: </td><td><xsl:value-of select="APPROACH"/></td></tr>
				<tr><td>Komunikacja Miejska: </td><td><xsl:value-of select="PUBLICTRANS"/></td></tr>
				<tr style="background-color:grey;"><td>Przydatne Linki: </td><td><xsl:value-of select="LINKS"/></td></tr>
				</table>
				</section>
			</article><br/>
		</xsl:for-each>
	</body>
</html>
	</xsl:template>
	
</xsl:stylesheet>
