<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
	<xsl:template match="/">
<html>
	<body style="font-family:calibri;">
		<h2><img src="s4.png"/>Informacje drogowe</h2>
		<xsl:for-each select="INFORMATIONS/INFO">
		<xsl:sort select="CREATE_DATE"/>
			<article>
				<header>
					<h2 style="padding:0px; margin:0px;"><a href="info.xml"><img src="s2.png"/></a><strong style="padding-left:10px;"><xsl:value-of select="HEADER"/></strong><xsl:if test="CONFIRMED='false'">&#160;<img src="s1.png"/></xsl:if></h2>
					<details style="font-size:13px;">
						<strong>Autor: </strong><xsl:value-of select="CREATE_ID"/> - <xsl:value-of select="CREATE_DATE"/><br/>
						<strong>Ostatnia aktualizacja: </strong><xsl:value-of select="UPDATE_DATE"/>
					</details>
					<br/><br/>
					<a href="#">[Edytuj info]</a>
					<br/><br/>
				</header>
				
				<section maxlength="20">
					<xsl:value-of select="TEXT"/>
				</section>
			</article><br/>
		</xsl:for-each>
	</body>
</html>
	</xsl:template>
</xsl:stylesheet>
