package javaapplication2;
import java.io.File;
import java.io.IOException;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.swing.table.DefaultTableModel;
import javax.xml.XMLConstants;
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;
import javax.xml.transform.Transformer;
import javax.xml.transform.TransformerConfigurationException;
import javax.xml.transform.TransformerException;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamResult;
import javax.xml.transform.stream.StreamSource;
import javax.xml.validation.Schema;
import javax.xml.validation.SchemaFactory;
import javax.xml.validation.Validator;
import org.w3c.dom.Attr;
import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.NamedNodeMap;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;
import org.xml.sax.ErrorHandler;
import org.xml.sax.SAXException;
import org.xml.sax.SAXParseException;

public class XMLApp {
    XMLJFrame f;
    DocumentBuilder dBuilder;
    DocumentBuilderFactory dbFactory;
    File fXmlFile;
    DefaultTableModel tableModel;
    Document doc;
    public String searchText;

    public void delete(){
        Element element = (Element) doc.getElementsByTagName("film").item(f.getDeleteID()-1);
        System.out.print(f.getDeleteID());
	element.getParentNode().removeChild(element);
        showTable(false);
    }
    public void safeToFile() {
        try {
            TransformerFactory transformerFactory = TransformerFactory.newInstance();
            Transformer transformer = transformerFactory.newTransformer();
            DOMSource source = new DOMSource(doc);
            StreamResult result = new StreamResult(new File("zad3.xml"));
            transformer.transform(source, result);
        } catch (TransformerConfigurationException ex) {
            Logger.getLogger(XMLApp.class.getName()).log(Level.SEVERE, null, ex);
        } catch (TransformerException ex) {
            Logger.getLogger(XMLApp.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
    public void showTable(boolean limit) {
        tableModel.setRowCount(0);
        NodeList nList = doc.getElementsByTagName("film");
        for (int temp = 0; temp < nList.getLength(); temp++) {
            Node nNode = nList.item(temp);
            if (nNode.getNodeType() == Node.ELEMENT_NODE) {
                Element eElement = (Element) nNode;
                String type = eElement.getAttribute("type");
                String lang = eElement.getAttribute("lang");
                String tytul = eElement.getElementsByTagName("tytul").item(0).getTextContent();
                String pobr = eElement.getElementsByTagName("ilosc_pobran").item(0).getTextContent();
                String cena = eElement.getElementsByTagName("srednia_cena").item(0).getTextContent();
                String ogl = eElement.getElementsByTagName("ogladalnosc").item(0).getTextContent();
                String ocena = eElement.getElementsByTagName("srednia_ocen").item(0).getTextContent();
                Element rElement = (Element) eElement.getElementsByTagName("rok_produkcji").item(0);
                String rok = rElement.getAttribute("nr");
                System.out.println("---"+searchText+"---"+type+"---");
                if(!limit 
                        ||(f.getSelectedIndexComboBox()==0 && searchText.equals(type))
                        ||(f.getSelectedIndexComboBox()==1 && searchText.equals(rok))
                        ||(f.getSelectedIndexComboBox()==2 && searchText.equals(tytul)))
                tableModel.addRow(new Object[]{temp + 1, type, lang, tytul, pobr, cena, ogl, ocena, rok});
            }
        }
    }
    public void addNewEmptyItem() {
        
        tableModel.addRow(new Object[]{doc.getElementsByTagName("film").getLength() + 1});
        Element e = doc.createElement("film");
        Element e1 = doc.createElement("tytul");
        Element e2 = doc.createElement("ilosc_pobran");
        Element e3 = doc.createElement("srednia_cena");
        Element e4 = doc.createElement("ogladalnosc");
        Element e5 = doc.createElement("srednia_ocen");
        Element e6 = doc.createElement("rok_produkcji");
        e1.appendChild(doc.createTextNode(""));
        e1.appendChild(doc.createTextNode(""));
        e2.appendChild(doc.createTextNode(""));
        e3.appendChild(doc.createTextNode(""));
        e4.appendChild(doc.createTextNode(""));
        e5.appendChild(doc.createTextNode(""));
        Attr attr = doc.createAttribute("type");
        e.setAttributeNode(attr);
        Attr attr1 = doc.createAttribute("lang");
        e.setAttributeNode(attr1);
        Attr attr2 = doc.createAttribute("nr");
        e6.setAttributeNode(attr2);
        e.appendChild(e1);
        e.appendChild(e2);
        e.appendChild(e3);
        e.appendChild(e4);
        e.appendChild(e5);
        e.appendChild(e6);
        doc.getDocumentElement().appendChild(e);
        showTable(false);
    }
    public void readXMLFile() {
        tableModel = f.getModel();
        try {
            System.out.println("Wczytuję plik");
            fXmlFile = new File("zad3.xml");
            f.enableElements();
            dbFactory = DocumentBuilderFactory.newInstance();
            dBuilder = dbFactory.newDocumentBuilder();
            doc = dBuilder.parse(fXmlFile);
            doc.getDocumentElement().normalize();
            f.setRootElement("Element główny: " + doc.getDocumentElement().getNodeName());
        } catch (ParserConfigurationException parserConfigurationException) {
            System.out.println(parserConfigurationException.toString());
        } catch (SAXException sAXException) {
            System.out.println(sAXException.toString());
        } catch (IOException iOException) {
            System.out.println(iOException.toString());
        }
        showTable(false);
    }
    public boolean validateXML() {
        try {
            SchemaFactory factory = SchemaFactory.newInstance(XMLConstants.W3C_XML_SCHEMA_NS_URI);
            Schema schema = factory.newSchema(new StreamSource("zad3.xsd"));
            Validator validator = schema.newValidator();
            validator.validate(new StreamSource(fXmlFile));
            f.showValidateState("Walidacja: poprawny");
            return true;
        } catch (SAXException | IOException ex) {
            f.showValidateState("Walidacja: niepoprawny");
            return false;
        }
    }
    public static void main(String[] args) {
        XMLApp a = new XMLApp();
        a.f = new XMLJFrame(a);
        a.f.setVisible(true);
    }
    public void updateElement(){
        Element element = (Element) doc.getElementsByTagName("film").item(f.getSelectedIndex());
        element.setAttribute("type", f.getRowItemValue(1));
        element.setAttribute("lang", f.getRowItemValue(2));
        element.getElementsByTagName("tytul").item(0).getFirstChild().setNodeValue(f.getRowItemValue(3));
        element.getElementsByTagName("ilosc_pobran").item(0).getFirstChild().setNodeValue(f.getRowItemValue(4));
        element.getElementsByTagName("srednia_cena").item(0).getFirstChild().setNodeValue(f.getRowItemValue(5));
        element.getElementsByTagName("ogladalnosc").item(0).getFirstChild().setNodeValue(f.getRowItemValue(6));
        element.getElementsByTagName("srednia_ocen").item(0).getFirstChild().setNodeValue(f.getRowItemValue(7));
        Element element2 = (Element) element.getElementsByTagName("rok_produkcji").item(0);
        element2.setAttribute("nr", f.getRowItemValue(8));
    }
 
    
    /*public void validateXMLDTD() {
     try {
     File fXmlFile = new File("zad3.xml");
     DocumentBuilderFactory f
     = DocumentBuilderFactory.newInstance();
     f.setValidating(true); // Default is false
     DocumentBuilder b = f.newDocumentBuilder();
     // ErrorHandler h = new DefaultHandler();
     ErrorHandler h = new MyErrorHandler();
     b.setErrorHandler(h);
     Document d = b.parse(fXmlFile);
     } catch (ParserConfigurationException e) {
     System.out.println(e.toString());
     } catch (SAXException e) {
     System.out.println(e.toString());
     } catch (IOException e) {
     System.out.println(e.toString());
     }
     }
     private class MyErrorHandler implements ErrorHandler {
     @Override
     public void warning(SAXParseException e) throws SAXException {
     System.out.println("Warning: ");
     printInfo(e);
     }
     @Override
     public void error(SAXParseException e) throws SAXException {
     System.out.println("Error: ");
     printInfo(e);
     }
     @Override
     public void fatalError(SAXParseException e)
     throws SAXException {
     System.out.println("Fattal error: ");
     printInfo(e);
     }

     private void printInfo(SAXParseException e) {
     System.out.println("   Public ID: " + e.getPublicId());
     System.out.println("   System ID: " + e.getSystemId());
     System.out.println("   Line number: " + e.getLineNumber());
     System.out.println("   Column number: " + e.getColumnNumber());
     System.out.println("   Message: " + e.getMessage());
     }
     }*/
}
