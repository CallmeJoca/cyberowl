
 <div id='top'></div>

# CyberOwl

 > Last Updated 21/08/2022 21:09:50 UTC
 
 A daily updated summary of the most frequent types of security incidents currently being reported from different sources.
 
 For more information, please check out the documentation [here](./docs/README.md).
 
 ---
 |CyberOwl Sources|Description|
 |---|---|
 |[US-CERT](#us-cert-arrow_heading_up)|United States Computer Emergency and Readiness Team.|
 |[MA-CERT](#ma-cert-arrow_heading_up)|Moroccan Computer Emergency Response Team.|
 |[CERT-FR](#cert-fr-arrow_heading_up)|The French national government Computer Security Incident Response Team.|
 |[IBM X-Force Exchange](#ibmcloud-arrow_heading_up)|A cloud-based threat intelligence platform that allows to consume, share and act on threat intelligence.|
 |[ZeroDayInitiative](#zerodayinitiative-arrow_heading_up)|An international software vulnerability initiative that was started in 2005 by TippingPoint.|
 |[OBS Vigilance](#obs-vigilance-arrow_heading_up)|Vigilance is an initiative created by OBS (Orange Business Services) since 1999 to watch public vulnerabilities and then offer security fixes, a database and tools to remediate them.|
 |[VulDB](#vuldb-arrow_heading_up)|Number one vulnerability database documenting and explaining security vulnerabilities, threats, and exploits since 1970.|
 
 > Suggest a source by opening an [issue](https://github.com/karimhabush/cyberowl/issues)! :raised_hands:
 ---

## US-CERT [:arrow_heading_up:](#cyberowl)

 |Title|Description|Date|
 |---|---|---|
 |[CISA releases 5 Industrial Control Systems Advisories](https://www.cisa.gov/uscert/ncas/current-activity/2022/08/18/cisa-releases-5-industrial-control-systems-advisories)|<p class="MsoNormal">CISA has released 5 Industrial Control Systems (ICS) advisories on August 18, 2022. These advisories provide timely information about current security issues, vulnerabilities, and exploits surrounding ICS.</p>|Thursday, August 18, 2022|
 |[Cisco Releases Security Update for Cisco Secure Web Appliance](https://www.cisa.gov/uscert/ncas/current-activity/2022/08/18/cisco-releases-security-update-cisco-secure-web-appliance)|<p>Cisco has released security updates to address vulnerabilities in Cisco Secure Web Appliance. A remote attacker could exploit some of these vulnerabilities to take control of an affected system. For updates addressing lower severity vulnerabilities, see the <a href="https://tools.cisco.com/security/center/publicationListing.x">Cisco Security Advisories</a> page. <br> </p>|Thursday, August 18, 2022|
 |[CISA Adds Seven Known Exploited Vulnerabilities to Catalog](https://www.cisa.gov/uscert/ncas/current-activity/2022/08/18/cisa-adds-seven-known-exploited-vulnerabilities-catalog)|<p>CISA has added seven new vulnerabilities to its <a href="https://www.cisa.gov/known-exploited-vulnerabilities-catalog">Known Exploited Vulnerabilities Catalog</a>, based on evidence of active exploitation. These types of vulnerabilities are a frequent attack vector for malicious cyber actors and pose significant risk to the federal enterprise. Note: to view the newly added vulnerabilities in the catalog, click on the arrow in the “Date Added to Catalog” column, which will sort by descending dates. <br> </p>|Thursday, August 18, 2022|
 |[Apple Releases Security Updates for Multiple Products](https://www.cisa.gov/uscert/ncas/current-activity/2022/08/18/apple-releases-security-updates-multiple-products)|<p>Apple has released security updates to address vulnerabilities in macOS Monterey, iOS and iPadOS, and Safari. An attacker could exploit one of these vulnerabilities to take control of an affected device.</p>|Thursday, August 18, 2022|
 |[Threat Actors Exploiting Multiple Vulnerabilities Against Zimbra Collaboration Suite](https://www.cisa.gov/uscert/ncas/current-activity/2022/08/16/threat-actors-exploiting-multiple-vulnerabilities-against-zimbra)|<p>CISA and the Multi-State Information Sharing &amp; Analysis Center (MS-ISAC) have released a <a href="https://www.cisa.gov/uscert/ncas/alerts/aa22-228a">joint Cybersecurity Advisory (CSA)</a> in response to active exploitation of multiple vulnerabilities against Zimbra Collaboration Suite (ZCS), an enterprise cloud-hosted collaboration software and email platform. </p>|Tuesday, August 16, 2022|
 |[CISA Adds Two Known Exploited Vulnerabilities to Catalog ](https://www.cisa.gov/uscert/ncas/current-activity/2022/08/11/cisa-adds-two-known-exploited-vulnerabilities-catalog)|<p>CISA has added two new vulnerabilities to its<a href="https://www.cisa.gov/known-exploited-vulnerabilities-catalog"> Known Exploited Vulnerabilities Catalog</a>, based on evidence of active exploitation. These types of vulnerabilities are a frequent attack vector for malicious cyber actors and pose significant risk to the federal enterprise. Note: to view the newly added vulnerabilities in the catalog, click on the arrow in the "Date Added to Catalog" column, which will sort by descending dates. </p>|Thursday, August 11, 2022|
 
 ---

## OBS-Vigilance [:arrow_heading_up:](#cyberowl)

 |Title|Description|Date|
 |---|---|---|
 |[<a href="https://vigilance.fr/vulnerability/FreeBSD-buffer-overflow-via-9p-Message-Handling-39082" class="noirorange"><b>FreeBSD</b>: buffer overflow via 9p Message Handling</a>](https://vigilance.fr/vulnerability/FreeBSD-buffer-overflow-via-9p-Message-Handling-39082)|An attacker, in a guest system, can trigger a buffer overflow of FreeBSD, via 9p Message Handling, in order to trigger a denial of service, and possibly to run code on the host system...|Visit link for details|
 |[<a href="https://vigilance.fr/vulnerability/FreeBSD-memory-reading-via-Stale-Virtual-Memory-Mapping-39081" class="noirorange"><b>FreeBSD</b>: memory reading via Stale Virtual Memory Mapping</a>](https://vigilance.fr/vulnerability/FreeBSD-memory-reading-via-Stale-Virtual-Memory-Mapping-39081)|An attacker can read a memory fragment of FreeBSD, via Stale Virtual Memory Mapping, in order to obtain sensitive information...|Visit link for details|
 |[<a href="https://vigilance.fr/vulnerability/FreeBSD-reuse-after-free-via-AIO-Credential-39080" class="noirorange"><b>FreeBSD</b>: reuse after free via AIO Credential</a>](https://vigilance.fr/vulnerability/FreeBSD-reuse-after-free-via-AIO-Credential-39080)|An attacker can force the reuse of a freed memory area of FreeBSD, via AIO Credential, in order to trigger a denial of service, and possibly to run code...|Visit link for details|
 |[<a href="https://vigilance.fr/vulnerability/IBM-MQ-external-XML-entity-injection-via-Explorer-Import-Wizard-39077" class="noirorange"><b>IBM MQ</b>: external XML entity injection via Explorer Import Wizard</a>](https://vigilance.fr/vulnerability/IBM-MQ-external-XML-entity-injection-via-Explorer-Import-Wizard-39077)|An attacker can transmit malicious XML data to IBM MQ, via Explorer Import Wizard, in order to read a file, scan sites, or trigger a denial of service...|Visit link for details|
 |[<a href="https://vigilance.fr/vulnerability/schroot-privilege-escalation-via-Session-Names-39076" class="noirorange"><b>schroot</b>: privilege escalation via Session Names</a>](https://vigilance.fr/vulnerability/schroot-privilege-escalation-via-Session-Names-39076)|An attacker can bypass restrictions of schroot, via Session Names, in order to escalate his privileges...|Visit link for details|
 |[<a href="https://vigilance.fr/vulnerability/LibTIFF-integer-overflow-via-tiffcrop-extractContigSamplesShifted16bits-39075" class="noirorange"><b>LibTIFF</b>: integer overflow via tiffcrop <wbr>extractContigSamples<wbr>Shifted16bits()</wbr></wbr></a>](https://vigilance.fr/vulnerability/LibTIFF-integer-overflow-via-tiffcrop-extractContigSamplesShifted16bits-39075)|An attacker can trigger an integer overflow of LibTIFF, via tiffcrop |Visit link for details|
 |[<a href="https://vigilance.fr/vulnerability/LibTIFF-out-of-bounds-memory-reading-via-tiffcrop-computeInputPixelOffsets-39074" class="noirorange"><b>LibTIFF</b>: out-of-bounds memory reading via tiffcrop <wbr>computeInputPixelOff<wbr>sets()</wbr></wbr></a>](https://vigilance.fr/vulnerability/LibTIFF-out-of-bounds-memory-reading-via-tiffcrop-computeInputPixelOffsets-39074)|An attacker can force a read at an invalid memory address of LibTIFF, via tiffcrop |Visit link for details|
 |[<a href="https://vigilance.fr/vulnerability/LibTIFF-integer-overflow-via-tiffcrop-offsets-39073" class="noirorange"><b>LibTIFF</b>: integer overflow via tiffcrop offsets</a>](https://vigilance.fr/vulnerability/LibTIFF-integer-overflow-via-tiffcrop-offsets-39073)|An attacker can trigger an integer overflow of LibTIFF, via tiffcrop offsets, in order to trigger a denial of service, and possibly to run code...|Visit link for details|
 |[<a href="https://vigilance.fr/vulnerability/QEMU-overload-via-xhci-ring-chain-length-39072" class="noirorange"><b>QEMU</b>: overload via <wbr>xhci_ring_chain_leng<wbr>th()</wbr></wbr></a>](https://vigilance.fr/vulnerability/QEMU-overload-via-xhci-ring-chain-length-39072)|An attacker can trigger an overload of QEMU, via |Visit link for details|
 |[<a href="https://vigilance.fr/vulnerability/QEMU-reuse-after-free-via-lsi-do-msgout-39071" class="noirorange"><b>QEMU</b>: reuse after free via lsi_do_msgout()</a>](https://vigilance.fr/vulnerability/QEMU-reuse-after-free-via-lsi-do-msgout-39071)|An attacker, in a guest system, can force the reuse of a freed memory area of QEMU, via lsi_do_msgout(), in order to trigger a denial of service, and possibly to run code on the host system...|Visit link for details|
 |[<a href="https://vigilance.fr/vulnerability/Apple-iOS-macOS-two-vulnerabilities-39070" class="noirorange"><b>Apple iOS/macOS</b>: two vulnerabilities</a>](https://vigilance.fr/vulnerability/Apple-iOS-macOS-two-vulnerabilities-39070)|An attacker can use several vulnerabilities of Apple iOS/macOS...|Visit link for details|
 
 ---

## VulDB [:arrow_heading_up:](#cyberowl)

 |Title|Description|Date|
 |---|---|---|
 |[yetiforcecrm cross site scripting](https://vuldb.com/?id.206877)|Visit link for details|2022-08-21 at 15:44|
 |[Apache Flume JMS Source injection](https://vuldb.com/?id.206876)|Visit link for details|2022-08-21 at 15:44|
 |[NotrinosERP unknown vulnerability](https://vuldb.com/?id.206875)|Visit link for details|2022-08-21 at 15:43|
 |[MA Lighting grandMA2 Light hard-coded credentials](https://vuldb.com/?id.206874)|Visit link for details|2022-08-21 at 15:42|
 |[Rhonabwy JWE Token denial of service](https://vuldb.com/?id.206873)|Visit link for details|2022-08-21 at 08:14|
 |[Delta Electronics Delta Robot Automation Studio XML Document xml external entity reference](https://vuldb.com/?id.206872)|Visit link for details|2022-08-21 at 16:13|
 |[LS Electric PLC/XG5000 inadequate encryption](https://vuldb.com/?id.206871)|Visit link for details|2022-08-21 at 16:03|
 |[Project-Nexus sql injection](https://vuldb.com/?id.206870)|Visit link for details|2022-08-21 at 09:15|
 |[chatwoot cross site scripting](https://vuldb.com/?id.206869)|Visit link for details|2022-08-21 at 09:13|
 |[BPC SmartVista Error Message cross site scripting](https://vuldb.com/?id.206868)|Visit link for details|2022-08-21 at 09:12|
 
 ---

## ZeroDayInitiative [:arrow_heading_up:](#cyberowl)

 |Title|Description|Date|
 |---|---|---|
 |[(Pwn2Own) Apple Safari Out-Of-Bounds Write Remote Code Execution Vulnerability](https://www.zerodayinitiative.com/advisories/ZDI-22-1123/)|Visit link for details|Aug. 18, 2022|
 |[ManageEngine OpManager Plus getUserAPIKey Authentication Bypass Vulnerability](https://www.zerodayinitiative.com/advisories/ZDI-22-1122/)|Visit link for details|Aug. 18, 2022|
 |[ManageEngine NetFlow Analyzer getUserAPIKey Authentication Bypass Vulnerability](https://www.zerodayinitiative.com/advisories/ZDI-22-1121/)|Visit link for details|Aug. 18, 2022|
 |[ManageEngine OpManager getUserAPIKey Authentication Bypass Vulnerability](https://www.zerodayinitiative.com/advisories/ZDI-22-1120/)|Visit link for details|Aug. 18, 2022|
 |[ManageEngine Network Configuration Manager getUserAPIKey Authentication Bypass Vulnerability](https://www.zerodayinitiative.com/advisories/ZDI-22-1119/)|Visit link for details|Aug. 18, 2022|
 |[(Pwn2Own) Linux Kernel nft_object Use-After-Free Privilege Escalation Vulnerability](https://www.zerodayinitiative.com/advisories/ZDI-22-1118/)|Visit link for details|Aug. 18, 2022|
 |[(Pwn2Own) Linux Kernel route4_change Double Free Privilege Escalation Vulnerability](https://www.zerodayinitiative.com/advisories/ZDI-22-1117/)|Visit link for details|Aug. 18, 2022|
 |[Adobe Acrobat Reader DC Font Parsing Out-Of-Bounds Read Information Disclosure Vulnerability](https://www.zerodayinitiative.com/advisories/ZDI-22-1116/)|Visit link for details|Aug. 18, 2022|
 
 ---

## MA-CERT [:arrow_heading_up:](#cyberowl)

 |Title|Description|Date|
 |---|---|---|
 |[37871908/22 - « Zero-Day » affectant le navigateur Apple Safari ](/fr/content/3787190822-zero-day-affectant-le-navigateur-apple-safari.html)|Apple annonce la correction d’une vulnérabilité critique affectant les versions susmentionnées de son navigateur Safari. Selon Apple cette vulnérabilité est activement exploitée et peut permettre à un attaquant distant d’exécuter du code...|19 août 2022|
 |[37861908/22 - Vulnérabilité dans Cisco AsyncOS for Secure Web Appliance](/fr/content/3786190822-vulnerabilite-dans-cisco-asyncos-secure-web-appliance.html)|Une vulnérabilité a été corrigée dans Cisco AsyncOS for Secure Web Appliance. L’exploitation de cette faille pourrait permettre à un attaquant d’exécuter du code arbitraire à distance et de réussir une élévation de privilèges.|19 août 2022|
 |[37841808/22 - Vulnérabilités critiques affectantle navigateur Google Chrome ](/fr/content/3784180822-vulnerabilites-critiques-affectant-le-navigateur-google-chrome.html)|Google vient de publier une mise à jour de sécurité qui permet de corriger plusieursvulnérabilitésaffectant le navigateur Google Chrome. Une de ces vulnérabilités identifiée par «CVE-2022-2856 » est activement exploitéeL’...|18 août 2022|
 |[37851708/22 - Vulnérabilités dans macOS Monterey](/fr/content/3785170822-vulnerabilites-dans-macos-monterey.html)|Deux vulnérabilités ont été corrigées dans macOS Monterey. L’exploitation de ces failles pourrait permettre à un attaquant d’exécuter du code arbitraire à distance. Apple confirme que ces deux vulnérabilités sont activement exploitées.|18 août 2022|
 |[37831708/22 - Vulnérabilités dans Zimbra](/fr/content/3783170822-vulnerabilites-dans-zimbra.html)|Plusieurs vulnérabilités ont été corrigées dans Zimbra. L’exploitation de ces failles pourrait permettre à un attaquant d’exécuter du code arbitraire à distance et de porter atteinte à la confidentialité des données.|17 août 2022|
 |[37821708/22 - Vulnérabilités affectant des produits QNAP ](/fr/content/3782170822-vulnerabilites-affectant-des-produits-qnap.html)|QNAP annonce la disponibilité de mises à jour de sécurité permettant la correctionde plusieurs vulnérabilités affectant ses produits susmentionnés. L'exploitationde ces vulnérabilités peut permettre à un attaquant distant d’...|17 août 2022|
 |[37811608/22 - Vulnérabilités dans Microsoft Windows ](/fr/content/3781160822-vulnerabilites-dans-microsoft-windows.html)|Microsoft annonce la correction de deux vulnérabilités affectant lessystèmes d’exploitation Windows susmentionnés. L’exploitation de ces vulnérabilités peut permettre à un attaquant de réussir une élévation de privilèges ou de contourner...|16 août 2022|
 |[37801608/22 - Vulnérabilités dans les produits de vidéoconférence ZOOM ](/fr/content/3780160822-vulnerabilites-dans-les-produits-de-videoconference-zoom.html)|Zoom annonce la correction de plusieurs vulnérabilités critiques affectant les produits susmentionnés de vidéoconférence Zoom. L’exploitation de ces failles peut permettre à un attaquant local d’avoir les privilèges d’un utilisateur « root...|16 août 2022|
 |[37791508/22 - Vulnérabilités dans PostgreSQL](/fr/content/3779150822-vulnerabilites-dans-postgresql.html)|Deux vulnérabilités ont été corrigées dans les versions PostgreSQL susmentionnées. L’exploitation de ces failles peut permettre à un attaquant d’exécuter du code arbitraire à distance, de causer un déni de service et de porter atteinte à...|15 août 2022|
 |[37781208/22 - Vulnérabilités dans les produits Siemens](/fr/content/3778120822-vulnerabilites-dans-les-produits-siemens.html)|Plusieurs vulnérabilités ont été corrigées dans les systèmes industriels de Siemens susmentionnés. Un attaquant pourrait exploiter ces failles afin d’exécuter du code arbitraire à dis-tance, réussir une élévation de privilèges, causer un...|12 août 2022|
 |[37771208/22 - Vulnérabilités dans les produits SonicWall](/fr/content/3777120822-vulnerabilites-dans-les-produits-sonicwall.html)|Deux vulnérabilités ont été corrigées dans les produits SonicWall susmentionnés. L’exploitation de ces failles peut permettre à un attaquant de réussir une élévation de privilèges et de porter atteinteà la confidentialité des données.|12 août 2022|
 
 ---

## CERT-FR [:arrow_heading_up:](#cyberowl)

 |Title|Description|Date|
 |---|---|---|
 |[Multiples vulnérabilités dans le noyau Linux d’Ubuntu](https://www.cert.ssi.gouv.fr/avis/CERTFR-2022-AVI-758/)|De multiples vulnérabilités ont été découvertes dans le noyau Linux d'Ubuntu . Elles permettent à un attaquant de provoquer un déni de service et une atteinte à la confidentialité des données.|Publié le 19 août 2022|
 |[Multiples vulnérabilités dans le noyau Linux de SUSE](https://www.cert.ssi.gouv.fr/avis/CERTFR-2022-AVI-757/)|De multiples vulnérabilités ont été découvertes dans le noyau Linux de SUSE. Certaines d'entre elles permettent à un attaquant de provoquer un problème de sécurité non spécifié par l'éditeur, un déni de service et une atteinte à l'intégrité des données.|Publié le 19 août 2022|
 |[Vulnérabilité dans Apple Safari](https://www.cert.ssi.gouv.fr/avis/CERTFR-2022-AVI-756/)|Une vulnérabilité a été découverte dans Apple Safari. Elle permet à un attaquant de provoquer une exécution de code arbitraire à distance.|Publié le 19 août 2022|
 |[Multiples vulnérabilités dans IBM Spectrum](https://www.cert.ssi.gouv.fr/avis/CERTFR-2022-AVI-755/)|De multiples vulnérabilités ont été découvertes dans IBM Spectrum. Certaines d'entre elles permettent à un attaquant de provoquer une exécution de code arbitraire à distance, un contournement de la politique de sécurité et une atteinte à l'intégrité des données.|Publié le 19 août 2022|
 |[Multiples vulnérabilités dans Nagios XI](https://www.cert.ssi.gouv.fr/avis/CERTFR-2022-AVI-754/)|De multiples vulnérabilités ont été découvertes dans Nagios XI. Elles permettent à un attaquant de provoquer un problème de sécurité non spécifié par l'éditeur.|Publié le 19 août 2022|
 |[Vulnérabilité dans Microsoft Edge](https://www.cert.ssi.gouv.fr/avis/CERTFR-2022-AVI-753/)|Une vulnérabilité a été corrigée dans |Publié le 18 août 2022|
 |[Multiples vulnérabilités dans les produits Apple](https://www.cert.ssi.gouv.fr/avis/CERTFR-2022-AVI-752/)|De multiples vulnérabilités ont été découvertes dans les produits Apple. Elles permettent à un attaquant de provoquer une exécution de code arbitraire à distance.|Publié le 18 août 2022|
 |[Vulnérabilité dans Cisco AsyncOS for Secure Web Appliance](https://www.cert.ssi.gouv.fr/avis/CERTFR-2022-AVI-751/)|Une vulnérabilité a été découverte dans Cisco AsyncOS for Secure Web Appliance. Elle permet à un attaquant de provoquer une exécution de code arbitraire à distance et une élévation de privilèges.|Publié le 18 août 2022|
 |[Multiples vulnérabilités dans le noyau Linux de Debian](https://www.cert.ssi.gouv.fr/avis/CERTFR-2022-AVI-750/)|De multiples vulnérabilités ont été découvertes dans le noyau Linux de Debian. Certaines d'entre elles permettent à un attaquant de provoquer un déni de service, un contournement de la politique de sécurité et une atteinte à la confidentialité des données.|Publié le 17 août 2022|
 |[Vulnérabilité dans le noyau Linux de Red Hat](https://www.cert.ssi.gouv.fr/avis/CERTFR-2022-AVI-749/)|Une vulnérabilité a été découverte dans le noyau Linux de Red Hat. Elle permet à un attaquant de provoquer une élévation de privilèges.|Publié le 17 août 2022|
 
 ---

## IBMCLOUD [:arrow_heading_up:](#cyberowl)

 |Title|Description|Date|
 |---|---|---|
 |[Mealie information disclosure (CVE-2022-34624)](https://exchange.xforce.ibmcloud.com/activity/list?filter=Vulnerabilities)|Visit link for details|Aug 19, 2022|
 |[Mealie information disclosure (CVE-2022-34623)](https://exchange.xforce.ibmcloud.com/activity/list?filter=Vulnerabilities)|Visit link for details|Aug 19, 2022|
 |[Mealie security bypass (CVE-2022-34621)](https://exchange.xforce.ibmcloud.com/activity/list?filter=Vulnerabilities)|Visit link for details|Aug 19, 2022|
 |[Mealie security bypass (CVE-2022-34615)](https://exchange.xforce.ibmcloud.com/activity/list?filter=Vulnerabilities)|Visit link for details|Aug 19, 2022|
 |[Octopus Deploy denial of service (CVE-2022-1901)](https://exchange.xforce.ibmcloud.com/activity/list?filter=Vulnerabilities)|Visit link for details|Aug 19, 2022|
 |[Octopus Deploy denial of service (CVE-2022-2049)](https://exchange.xforce.ibmcloud.com/activity/list?filter=Vulnerabilities)|Visit link for details|Aug 19, 2022|
 |[Octopus Deploy denial of service (CVE-2022-2074)](https://exchange.xforce.ibmcloud.com/activity/list?filter=Vulnerabilities)|Visit link for details|Aug 19, 2022|
 