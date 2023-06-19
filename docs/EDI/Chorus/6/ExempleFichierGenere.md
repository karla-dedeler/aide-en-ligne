# Exemple de fichier généré
<?xml version="1.0" encoding="UTF-8"?>


<Invoice xmlns="urn:oasis:names:specification:ubl:schema:xsd:Invoice-2" 
 xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" 
 xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">


   <cbc:UBLVersionID>2.1</cbc:UBLVersionID>


   <cbc:ID>12549810</cbc:ID>


   <cbc:IssueDate>2019-11-27</cbc:IssueDate>


   <cbc:InvoiceTypeCode>380</cbc:InvoiceTypeCode>


   <cbc:Note 
 />


   <cbc:DocumentCurrencyCode>EUR</cbc:DocumentCurrencyCode>


   <cac:BillingReference>


      <cac:InvoiceDocumentReference>


         <cbc:ID />


      </cac:InvoiceDocumentReference>


   </cac:BillingReference>


   <cac:ContractDocumentReference>


      <cbc:ID>1234894</cbc:ID>


      <cbc:DocumentTypeCode>Marché Public</cbc:DocumentTypeCode>


   </cac:ContractDocumentReference>


   <cac:AccountingSupplierParty>


      <cac:Party>


         <cac:PartyIdentification>


            <cbc:ID schemeName="1">00000000033834</cbc:ID>


         </cac:PartyIdentification>


         <cac:PartyName>


            <cbc:Name>25889910FOURNISSEUR</cbc:Name>


         </cac:PartyName>


         <cac:PostalAddress>


            <cbc:StreetName>1 
 rue Test Batiment A - Etage 
 1</cbc:StreetName>


            <cbc:CityName>Test</cbc:CityName>


            <cbc:PostalZone>75000</cbc:PostalZone>


            <cac:Country>


               <cbc:IdentificationCode>FR</cbc:IdentificationCode>


            </cac:Country>


         </cac:PostalAddress>


         <cac:PartyTaxScheme>


            <cbc:CompanyID>FR49377685488</cbc:CompanyID>


            <cac:TaxScheme>


               <cbc:TaxTypeCode>TVA 
 DEBIT</cbc:TaxTypeCode>


            </cac:TaxScheme>


         </cac:PartyTaxScheme>


         <cac:PartyLegalEntity>


            <cbc:RegistrationName>25889910FOURNISSEUR</cbc:RegistrationName>


            <cac:RegistrationAddress>


               <cbc:StreetName>1 
 rue Test Batiment A - Etage 
 1</cbc:StreetName>


               <cbc:CityName>Test</cbc:CityName>


               <cbc:PostalZone>75000</cbc:PostalZone>


               <cac:Country>


                  <cbc:IdentificationCode>FR</cbc:IdentificationCode>


               </cac:Country>


            </cac:RegistrationAddress>


         </cac:PartyLegalEntity>


      </cac:Party>


      <cac:AccountingContact>


         <cbc:Name>25889910FOURNISSEUR</cbc:Name>


         <cbc:Telephone>01 34 
 84 09 94</cbc:Telephone>


         <cbc:Telefax>01 30 41 
 77 81</cbc:Telefax>


         <cbc:ElectronicMail>contact@gestimum.com</cbc:ElectronicMail>


      </cac:AccountingContact>


   </cac:AccountingSupplierParty>


   <cac:AccountingCustomerParty>


      <cac:Party>


         <cac:PartyIdentification>


            <cbc:ID schemeName="1">00000000033974</cbc:ID>


         </cac:PartyIdentification>


         <cac:PartyName>


            <cbc:Name>Destinataire Partenaire</cbc:Name>


         </cac:PartyName>


         <cac:PostalAddress>


            <cbc:StreetName>10 
 rue du test</cbc:StreetName>


            <cbc:CityName>TEST</cbc:CityName>


            <cbc:PostalZone>75000</cbc:PostalZone>


            <cac:Country>


               <cbc:IdentificationCode>FR</cbc:IdentificationCode>


            </cac:Country>


         </cac:PostalAddress>


         <cac:PartyTaxScheme>


            <cbc:CompanyID />


            <cac:TaxScheme>


               <cbc:TaxTypeCode>TVA 
 DEBIT</cbc:TaxTypeCode>


            </cac:TaxScheme>


         </cac:PartyTaxScheme>


         <cac:PartyLegalEntity>


            <cbc:RegistrationName>Destinataire 
 Partenaire</cbc:RegistrationName>


            <cac:RegistrationAddress>


               <cbc:StreetName>10 
 rue du test</cbc:StreetName>


               <cbc:CityName>TEST</cbc:CityName>


               <cbc:PostalZone>75000</cbc:PostalZone>


               <cac:Country>


                  <cbc:IdentificationCode>FR</cbc:IdentificationCode>


               </cac:Country>


            </cac:RegistrationAddress>


         </cac:PartyLegalEntity>


      </cac:Party>


      <cac:AccountingContact>


         <cbc:ID>SERVICE\_DESTINATAIRE25889910</cbc:ID>


         <cbc:Name />


         <cbc:Telephone />


         <cbc:Telefax />


      </cac:AccountingContact>


   </cac:AccountingCustomerParty>


   <cac:Delivery>


      <cac:DeliveryLocation>


         <cbc:Description>Destinataire Partenaire 016-bureau25</cbc:Description>


         <cac:Address>


            <cbc:StreetName>10 
 rue du test</cbc:StreetName>


            <cbc:CityName>TEST</cbc:CityName>


            <cbc:PostalZone>75000</cbc:PostalZone>


            <cac:Country>


               <cbc:IdentificationCode>FR</cbc:IdentificationCode>


            </cac:Country>


         </cac:Address>


      </cac:DeliveryLocation>


   </cac:Delivery>


   <cac:PaymentMeans>


      <cbc:PaymentMeansCode listID="UN/ECE 4461 Subset" listAgencyID="NES" 
 listAgencyName="Northern European 
 Subset" listName="Payment Means">30</cbc:PaymentMeansCode>


      <cbc:PaymentDueDate>2019-11-27</cbc:PaymentDueDate>


      <cbc:PaymentChannelCode>IBAN</cbc:PaymentChannelCode>


      <cac:PayeeFinancialAccount>


         <cbc:ID>FR7611931911801164075960700</cbc:ID>


         <cac:FinancialInstitutionBranch>


            <cbc:ID>SOGEFRPPPSZ</cbc:ID>


         </cac:FinancialInstitutionBranch>


      </cac:PayeeFinancialAccount>


   </cac:PaymentMeans>


   <cac:PaymentTerms>


      <cbc:Note>Pénalités 
 de retard : taux d'intérêt légal + 5%</cbc:Note>


   </cac:PaymentTerms>


   <cac:AllowanceCharge>


      <cbc:ChargeIndicator>true</cbc:ChargeIndicator>


      <cbc:Amount currencyID="EUR">5</cbc:Amount>


      <cbc:BaseAmount currencyID="EUR">383.13</cbc:BaseAmount>


   </cac:AllowanceCharge>


   <cac:TaxTotal>


      <cbc:TaxAmount currencyID="EUR">77.63</cbc:TaxAmount>


      <cac:TaxSubtotal>


         <cbc:TaxableAmount 
 currencyID="EUR">147.3</cbc:TaxableAmount>


         <cbc:TaxAmount currencyID="EUR">29.46</cbc:TaxAmount>


         <cbc:Percent>20</cbc:Percent>


         <cac:TaxCategory>


            <cac:TaxScheme>


               <cbc:TaxTypeCode>TVA</cbc:TaxTypeCode>


            </cac:TaxScheme>


         </cac:TaxCategory>


      </cac:TaxSubtotal>


      <cac:TaxSubtotal>


         <cbc:TaxableAmount currencyID="EUR">240.83</cbc:TaxableAmount>


         <cbc:TaxAmount currencyID="EUR">48.17</cbc:TaxAmount>


         <cbc:Percent>20</cbc:Percent>


         <cac:TaxCategory>


            <cac:TaxScheme>


               <cbc:TaxTypeCode>TVA</cbc:TaxTypeCode>


            </cac:TaxScheme>


         </cac:TaxCategory>


      </cac:TaxSubtotal>


   </cac:TaxTotal>


   <cac:LegalMonetaryTotal>


      <cbc:TaxExclusiveAmount currencyID="EUR">388.13</cbc:TaxExclusiveAmount>


      <cbc:TaxInclusiveAmount currencyID="EUR">465.76</cbc:TaxInclusiveAmount>


      <cbc:AllowanceTotalAmount currencyID="EUR">0</cbc:AllowanceTotalAmount>


      <cbc:ChargeTotalAmount currencyID="EUR">5</cbc:ChargeTotalAmount>


      <cbc:PrepaidAmount currencyID="EUR">0</cbc:PrepaidAmount>


      <cbc:PayableAmount currencyID="EUR">465.76</cbc:PayableAmount>


   </cac:LegalMonetaryTotal>


   <cac:InvoiceLine>


      <cbc:ID>00016</cbc:ID>


      <cbc:InvoicedQuantity>0</cbc:InvoicedQuantity>


      <cbc:LineExtensionAmount currencyID="EUR">0</cbc:LineExtensionAmount>


      <cac:Item>


         <cbc:Name>BLC 19000070 / 31/12/2018 
 / Réf. 18/BO3221657- FE - NOUVEAU HALL MAIRIE</cbc:Name>


         <cac:AdditionalItemProperty>


            <cbc:Name>TYPE\_LIGNE</cbc:Name>


            <cbc:Value>INFORMATION</cbc:Value>


         </cac:AdditionalItemProperty>


      </cac:Item>


      <cac:Price>


         <cbc:PriceAmount 
 currencyID="EUR">0</cbc:PriceAmount>


         <cbc:BaseQuantity>0</cbc:BaseQuantity>


      </cac:Price>


   </cac:InvoiceLine>


   <cac:InvoiceLine>


      <cbc:ID>00032</cbc:ID>


      <cbc:InvoicedQuantity>0</cbc:InvoicedQuantity>


      <cbc:LineExtensionAmount 
 currencyID="EUR">0</cbc:LineExtensionAmount>


      <cac:Item>


         <cbc:Name>-EN 
 REPONSE A VOTRE DEMANDE -</cbc:Name>


         <cac:AdditionalItemProperty>


            <cbc:Name>TYPE\_LIGNE</cbc:Name>


            <cbc:Value>INFORMATION</cbc:Value>


         </cac:AdditionalItemProperty>


      </cac:Item>


      <cac:Price>


         <cbc:PriceAmount 
 currencyID="EUR">0</cbc:PriceAmount>


         <cbc:BaseQuantity>0</cbc:BaseQuantity>


      </cac:Price>


   </cac:InvoiceLine>


   <cac:InvoiceLine>


      <cbc:ID>00048</cbc:ID>


      <cbc:InvoicedQuantity>0</cbc:InvoicedQuantity>


      <cbc:LineExtensionAmount 
 currencyID="EUR">0</cbc:LineExtensionAmount>


      <cac:Item>


         <cbc:Name>- 
 FOURNITURE EXTINCTEURS -</cbc:Name>


         <cac:AdditionalItemProperty>


            <cbc:Name>TYPE\_LIGNE</cbc:Name>


            <cbc:Value>INFORMATION</cbc:Value>


         </cac:AdditionalItemProperty>


      </cac:Item>


      <cac:Price>


         <cbc:PriceAmount 
 currencyID="EUR">0</cbc:PriceAmount>


         <cbc:BaseQuantity>0</cbc:BaseQuantity>


      </cac:Price>


   </cac:InvoiceLine>


   <cac:InvoiceLine>


      <cbc:ID>00064</cbc:ID>


      <cbc:InvoicedQuantity>0</cbc:InvoicedQuantity>


      <cbc:LineExtensionAmount 
 currencyID="EUR">0</cbc:LineExtensionAmount>


      <cac:Item>


         <cbc:Name 
 />


         <cac:AdditionalItemProperty>


            <cbc:Name>TYPE\_LIGNE</cbc:Name>


            <cbc:Value>INFORMATION</cbc:Value>


         </cac:AdditionalItemProperty>


      </cac:Item>


      <cac:Price>


         <cbc:PriceAmount 
 currencyID="EUR">0</cbc:PriceAmount>


         <cbc:BaseQuantity>0</cbc:BaseQuantity>


      </cac:Price>


   </cac:InvoiceLine>


   <cac:InvoiceLine>


      <cbc:ID>00080</cbc:ID>


      <cbc:InvoicedQuantity>0</cbc:InvoicedQuantity>


      <cbc:LineExtensionAmount 
 currencyID="EUR">0</cbc:LineExtensionAmount>


      <cac:Item>


         <cbc:Name>HALL 
 MAIRIE :</cbc:Name>


         <cac:AdditionalItemProperty>


            <cbc:Name>TYPE\_LIGNE</cbc:Name>


            <cbc:Value>INFORMATION</cbc:Value>


         </cac:AdditionalItemProperty>


      </cac:Item>


      <cac:Price>


         <cbc:PriceAmount 
 currencyID="EUR">0</cbc:PriceAmount>


         <cbc:BaseQuantity>0</cbc:BaseQuantity>


      </cac:Price>


   </cac:InvoiceLine>


   <cac:InvoiceLine>


      <cbc:ID>00096</cbc:ID>


      <cbc:Note>Ext.eau pulvérisée 6L+additif AND</cbc:Note>


      <cbc:InvoicedQuantity 
 unitCode="EA">2</cbc:InvoicedQuantity>


      <cbc:LineExtensionAmount 
 currencyID="EUR">79.8</cbc:LineExtensionAmount>


      <cac:Delivery>


         <cbc:ActualDeliveryDate>2019-11-27</cbc:ActualDeliveryDate>


      </cac:Delivery>


      <cac:Item>


         <cbc:Name>Non 
 géré</cbc:Name>


         <cac:StandardItemIdentification>


            <cbc:ID>NON0000001</cbc:ID>


         </cac:StandardItemIdentification>


         <cac:ClassifiedTaxCategory>


            <cbc:Percent>20</cbc:Percent>


            <cac:TaxScheme>


               <cbc:TaxTypeCode>TVA 
 DEBIT</cbc:TaxTypeCode>


            </cac:TaxScheme>


         </cac:ClassifiedTaxCategory>


      </cac:Item>


      <cac:Price>


         <cbc:PriceAmount 
 currencyID="EUR">39.9</cbc:PriceAmount>


         <cbc:BaseQuantity 
 unitCode="EA">2</cbc:BaseQuantity>


      </cac:Price>


   </cac:InvoiceLine>


   <cac:InvoiceLine>


      <cbc:ID>00112</cbc:ID>


      <cbc:Note>Ext.CO2 
 2 kg AND</cbc:Note>


      <cbc:InvoicedQuantity 
 unitCode="EA">1</cbc:InvoicedQuantity>


      <cbc:LineExtensionAmount 
 currencyID="EUR">53</cbc:LineExtensionAmount>


      <cac:Delivery>


         <cbc:ActualDeliveryDate>2019-11-27</cbc:ActualDeliveryDate>


      </cac:Delivery>


      <cac:Item>


         <cbc:Name>Non 
 géré</cbc:Name>


         <cac:StandardItemIdentification>


            <cbc:ID>NON0000001</cbc:ID>


         </cac:StandardItemIdentification>


         <cac:ClassifiedTaxCategory>


            <cbc:Percent>20</cbc:Percent>


            <cac:TaxScheme>


               <cbc:TaxTypeCode>TVA 
 DEBIT</cbc:TaxTypeCode>


            </cac:TaxScheme>


         </cac:ClassifiedTaxCategory>


      </cac:Item>


      <cac:Price>


         <cbc:PriceAmount 
 currencyID="EUR">53</cbc:PriceAmount>


         <cbc:BaseQuantity 
 unitCode="EA">1</cbc:BaseQuantity>


      </cac:Price>


   </cac:InvoiceLine>


   <cac:InvoiceLine>


      <cbc:ID>00128</cbc:ID>


      <cbc:Note>Pose 
 Extincteur</cbc:Note>


      <cbc:InvoicedQuantity 
 unitCode="EA">3</cbc:InvoicedQuantity>


      <cbc:LineExtensionAmount 
 currencyID="EUR">3</cbc:LineExtensionAmount>


      <cac:Delivery>


         <cbc:ActualDeliveryDate>2019-11-27</cbc:ActualDeliveryDate>


      </cac:Delivery>


      <cac:Item>


         <cbc:Name>Non 
 géré</cbc:Name>


         <cac:StandardItemIdentification>


            <cbc:ID>NON0000001</cbc:ID>


         </cac:StandardItemIdentification>


         <cac:ClassifiedTaxCategory>


            <cbc:Percent>20</cbc:Percent>


            <cac:TaxScheme>


               <cbc:TaxTypeCode>TVA 
 DEBIT</cbc:TaxTypeCode>


            </cac:TaxScheme>


         </cac:ClassifiedTaxCategory>


      </cac:Item>


      <cac:Price>


         <cbc:PriceAmount 
 currencyID="EUR">1</cbc:PriceAmount>


         <cbc:BaseQuantity 
 unitCode="EA">3</cbc:BaseQuantity>


      </cac:Price>


   </cac:InvoiceLine>


   <cac:InvoiceLine>


      <cbc:ID>00144</cbc:ID>


      <cbc:Note>Forfait 
 déplacement (hors vérification annuelle)</cbc:Note>


      <cbc:InvoicedQuantity 
 unitCode="EA">1</cbc:InvoicedQuantity>


      <cbc:LineExtensionAmount 
 currencyID="EUR">6.5</cbc:LineExtensionAmount>


      <cac:Delivery>


         <cbc:ActualDeliveryDate>2019-11-27</cbc:ActualDeliveryDate>


      </cac:Delivery>


      <cac:Item>


         <cbc:Name>Non 
 géré</cbc:Name>


         <cac:StandardItemIdentification>


            <cbc:ID>NON0000001</cbc:ID>


         </cac:StandardItemIdentification>


         <cac:ClassifiedTaxCategory>


            <cbc:Percent>20</cbc:Percent>


            <cac:TaxScheme>


               <cbc:TaxTypeCode>TVA 
 DEBIT</cbc:TaxTypeCode>


            </cac:TaxScheme>


         </cac:ClassifiedTaxCategory>


      </cac:Item>


      <cac:Price>


         <cbc:PriceAmount 
 currencyID="EUR">6.5</cbc:PriceAmount>


         <cbc:BaseQuantity 
 unitCode="EA">1</cbc:BaseQuantity>


      </cac:Price>


   </cac:InvoiceLine>


   <cac:InvoiceLine>


      <cbc:ID>00160</cbc:ID>


      <cbc:InvoicedQuantity>7</cbc:InvoicedQuantity>


      <cbc:LineExtensionAmount 
 currencyID="EUR">142.3</cbc:LineExtensionAmount>


      <cac:Item>


         <cbc:Name>Sous-Total</cbc:Name>


         <cac:AdditionalItemProperty>


            <cbc:Name>TYPE\_LIGNE</cbc:Name>


            <cbc:Value>REGROUPEMENT</cbc:Value>


         </cac:AdditionalItemProperty>


      </cac:Item>


      <cac:Price>


         <cbc:PriceAmount 
 currencyID="EUR">0</cbc:PriceAmount>


         <cbc:BaseQuantity>0</cbc:BaseQuantity>


      </cac:Price>


   </cac:InvoiceLine>


   <cac:InvoiceLine>


      <cbc:ID>00176</cbc:ID>


      <cbc:Note>LUNETTE 
 DE SOLEIL</cbc:Note>


      <cbc:InvoicedQuantity 
 unitCode="BX">1</cbc:InvoicedQuantity>


      <cbc:LineExtensionAmount 
 currencyID="EUR">240.83</cbc:LineExtensionAmount>


      <cac:Delivery>


         <cbc:ActualDeliveryDate>2019-11-27</cbc:ActualDeliveryDate>


      </cac:Delivery>


      <cac:Item>


         <cbc:Name>LUNETTE 
 DE SOLEIL</cbc:Name>


         <cac:StandardItemIdentification>


            <cbc:ID>ELS</cbc:ID>


         </cac:StandardItemIdentification>


         <cac:ClassifiedTaxCategory>


            <cbc:Percent>20</cbc:Percent>


            <cac:TaxScheme>


               <cbc:TaxTypeCode>TVA 
 DEBIT</cbc:TaxTypeCode>


            </cac:TaxScheme>


         </cac:ClassifiedTaxCategory>


      </cac:Item>


      <cac:Price>


         <cbc:PriceAmount 
 currencyID="EUR">240.83</cbc:PriceAmount>


         <cbc:BaseQuantity 
 unitCode="BX">1</cbc:BaseQuantity>


      </cac:Price>


   </cac:InvoiceLine>


   <cac:InvoiceLine>


      <cbc:ID>00192</cbc:ID>


      <cbc:InvoicedQuantity>1</cbc:InvoicedQuantity>


      <cbc:LineExtensionAmount 
 currencyID="EUR">240.83</cbc:LineExtensionAmount>


      <cac:Item>


         <cbc:Name>Sous-Total</cbc:Name>


         <cac:AdditionalItemProperty>


            <cbc:Name>TYPE\_LIGNE</cbc:Name>


            <cbc:Value>REGROUPEMENT</cbc:Value>


         </cac:AdditionalItemProperty>


      </cac:Item>


      <cac:Price>


         <cbc:PriceAmount 
 currencyID="EUR">0</cbc:PriceAmount>


         <cbc:BaseQuantity>0</cbc:BaseQuantity>


      </cac:Price>


   </cac:InvoiceLine>


</Invoice>


