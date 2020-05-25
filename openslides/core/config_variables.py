from django.core.validators import MaxLengthValidator

from openslides.core.config import ConfigVariable

_legal_notice = (
    "<p>Vote@Home ist ein Abstimmsystem für virtuelle Versammlungen mit speziellen Anforderungen an die "
    "Stimmrechtsverwaltung, wie sie im Rahmen von parlamentarischen Versammlungen, Eigentümerversammlungen, "
    "Mitgliederversammlungen, Aktionärsversammlungen, Genossenschaftsversammlungen u.ä. erfüllt werden müssen.</p>"
    "<p>Es dient der Darstellung und Steuerung von Tagesordnung und Anträgen sowie damit verbundenen Abstimmungen "
    "(Beschlussfassungen) und Wahlen in einer (WEG-) Versammlung. Wenn Sie mit uns Kontakt aufnehmen, finden Sie "
    "nachstehend unsere Kontaktdaten.</p>"
    "<p>VoteWorks GmbH<br>Königswinterer Str. 27<br>53639 Königswinter</p>"
    "<p>Tel +49 2244 8777-0<br>Fax    +49 2244 8777-15<br>e-Mail: info(at)voteworks.de</p>"
    "<p>Amtsgericht Siegburg<br>HRB 12778<br>Ust-IdNr. DE293042893</p>"
    "<p>Name und Anschrift des Vertretungsberechtigten:<br>"
    "Geschäftsführer: Bernd Nixdorf, Königswinterer Str. 27, 53639 Königswinter</p>"
    "<p>Haftungshinweis<br>"
    "Trotz sorgfältiger inhaltlicher Kontrolle übernehmen wir keine Haftung für den Inhalt externer Links. "
    "Für den Inhalt der verlinkten Seiten sind ausschließlich deren Betreiber verantwortlich.</p>"
    "<p>Vote@Home ist eine Adaption der unter MIT-Lizenz bereitgestellten Anwendung OpenSlides<sup>®</sup>, "
    "bei der es sich um ein webbasiertes Präsentations- und Versammlungssystem zur Darstellung und Steuerung von "
    "Tagesordnung, Anträgen und Wahlen einer Versammlung handelt.</p>"
)

_privacy_policy = (
    "<p>1. Datenschutz auf einen Blick</p>"
    "<p>Einleitung</p>"
    "<p>Wir freuen uns sehr über Ihr Interesse an unserer Online Plattform Vote@Home. "
    "Datenschutz hat einen besonders hohen Stellenwert für die VoteWorks GmbH. "
    "Eine Nutzung der Vote@Home&nbsp;Internetseiten der VoteWorks GmbH ist grundsätzlich ohne jede Angabe "
    "personenbezogener Daten möglich.</p>"
    "<p>Sofern eine betroffene Person besondere Services unseres Unternehmens über unsere Internetseite "
    "in Anspruch nehmen möchte, könnte jedoch eine Verarbeitung personenbezogener Daten erforderlich werden. "
    "Ist die Verarbeitung personenbezogener Daten erforderlich und besteht für eine solche Verarbeitung "
    "keine gesetzliche Grundlage, holen wir generell eine Einwilligung der betroffenen Person ein.</p>"
    "<p>Verarbeitung personenbezogener Daten</p>"
    "<p>Die Verarbeitung personenbezogener Daten, beispielsweise des Namens, der E-Mail-Adresse oder Telefonnummer "
    "einer betroffenen Person, erfolgt stets im Einklang mit der Datenschutz-Grundverordnung und in Übereinstimmung "
    "mit den für die VoteWorks GmbH geltenden landesspezifischen Datenschutzbestimmungen. "
    "Mittels dieser Datenschutzerklärung möchte unser Unternehmen die Öffentlichkeit über Art, "
    "Umfang und Zweck der von uns erhobenen, genutzten und verarbeiteten personenbezogenen Daten informieren. "
    "Ferner werden betroffene Personen mittels dieser Datenschutzerklärung "
    "über die ihnen zustehenden Rechte aufgeklärt.</p>"
    "<p>Zu den im Rahmen dieses Onlineangebotes verarbeiteten personenbezogenen Daten der Nutzer "
    "gehören Bestandsdaten (z.B. Namen von Kunden), Vertragsdaten (z.B. in Anspruch genommene Leistungen, "
    "Namen von Sachbearbeitern, Zahlungsinformationen), Nutzungsdaten (z.B. die besuchten Webseiten "
    "unseres Onlineangebotes, Interesse an unseren Produkten) und Inhaltsdaten (z.B. Stimmrechte).</p>"
    "<p>Die VoteWorks GmbH hat als für die Verarbeitung Verantwortlicher technische und organisatorische Maßnahmen "
    "umgesetzt, um einen möglichst lückenlosen Schutz der über diese Internetseite verarbeiteten "
    "personenbezogenen Daten sicherzustellen. Dennoch können Internetbasierte Datenübertragungen "
    "grundsätzlich Sicherheitslücken aufweisen, sodass ein absoluter Schutz nicht gewährleistet werden kann. "
    "Aus diesem Grund steht es jeder betroffenen Person frei, personenbezogene Daten auch auf alternativen Wegen, "
    "beispielsweise telefonisch, an uns zu übermitteln.</p>"
    "<p>Verantwortlicher</p>"
    "<p>Verantwortlicher im Sinne der Datenschutz-Grundverordnung, sonstiger in den Mitgliedstaaten "
    "der Europäischen Union geltenden Datenschutzgesetze und anderer Bestimmungen mit datenschutzrechtlichem "
    "Charakter ist die:</p>"
    "<p>VoteWorks GmbH<br>Königswinterer Str. 27<br>53639 Königswinter<br>Deutschland</p"
    "><p>Tel.: +49 2244 8777-0<br>Fax: +49 2244 8777-15</p>"
    "<p>E-Mail: info(at)voteworks.de<br>Website: www.voteworks.de</p>"
    "<p>Datenschutzbeauftragter</p>"
    "<p>Sie können sich aufgrund des Bundesdatenschutzgesetzes bei Fragen zur Erhebung, Verarbeitung oder "
    "Nutzung Ihrer personenbezogenen Daten, bei Auskünften, Berichtigung, Sperrung oder Löschung von Daten "
    "sowie Widerruf erteilter Einwilligungen an unseren betrieblichen Datenschutzbeauftragten wenden. "
    "Wir werden Sie gern über die zu Ihrer Person gespeicherten Daten informieren.</p>"
    "<p>E-Mail: datenschutz(at)voteworks.de</p>"
    "<p>Tel.: +49 2244 8777-0</p>"
    "<p>Erfassung von allgemeinen Daten und Informationen</p>"
    "<p>Die Internetseiten der VoteWorks GmbH erfassen mit jedem Aufruf der Internetseite durch eine betroffene "
    "Person oder ein automatisiertes System eine Reihe von allgemeinen Daten und Informationen. "
    "Diese allgemeinen Daten und Informationen werden in den Logfiles des Servers gespeichert. "
    "Erfasst werden können die</p>"
    "<p>(1) verwendeten Browsertypen und Versionen,<br>"
    "(2) das vom zugreifenden System verwendete Betriebssystem,<br>"
    "(3) die Internetseite, von welcher ein zugreifendes System auf unsere Internetseite gelangt "
    "(sogenannte Referrer),<br>"
    "(4) die Unterwebseiten, welche über ein zugreifendes System auf unserer Internetseite angesteuert werden,<br>"
    "(5) das Datum und die Uhrzeit eines Zugriffs auf die Internetseite,<br>"
    "(6) eine Internet-Protokoll-Adresse (IP-Adresse),<br>"
    "(7) der Internet-Service-Provider des zugreifenden Systems und<br>"
    "(8) sonstige ähnliche Daten und Informationen, die der Gefahrenabwehr im Falle von Angriffen auf unsere "
    "informationstechnologischen Systeme dienen.</p>"
    "<p>Bei der Nutzung dieser allgemeinen Daten und Informationen zieht die VoteWorks GmbH keine Rückschlüsse "
    "auf die betroffene Person. Diese Informationen werden vielmehr benötigt, um</p>"
    "<p>(1) die Inhalte unserer Internetseite korrekt auszuliefern,<br>"
    "(2) die Inhalte unserer Internetseite sowie die Werbung für diese zu optimieren,<br>"
    "(3) die dauerhafte Funktionsfähigkeit unserer informationstechnologischen Systeme und der Technik "
    "unserer Internetseite zu gewährleisten sowie<br>"
    "(4) um Strafverfolgungsbehörden im Falle eines Cyberangriffes die zur Strafverfolgung notwendigen "
    "Informationen bereitzustellen. Diese erhobenen Daten und Informationen werden durch VoteWorks GmbH daher "
    "einerseits statistisch und ferner mit dem Ziel ausgewertet, den Datenschutz und die Datensicherheit in "
    "unserem Unternehmen zu erhöhen, um letztlich ein optimales Schutzniveau für die von uns verarbeiteten "
    "personenbezogenen Daten sicherzustellen. Die anonymen Daten der Server-Logfiles werden getrennt von allen "
    "durch eine betroffene Person angegebenen personenbezogenen Daten gespeichert.</p>"
    "<p>Routinemäßige Löschung und Sperrung von personenbezogenen Daten</p>"
    "<p>Der für die Verarbeitung Verantwortliche verarbeitet und speichert personenbezogene Daten der "
    "betroffenen Person nur für den Zeitraum, der zur Erreichung des Speicherungszwecks erforderlich ist oder "
    "sofern dies durch den Europäischen Richtlinien- und Verordnungsgeber oder einen anderen Gesetzgeber "
    "in Gesetzen oder Vorschriften, welchen der für die Verarbeitung Verantwortliche unterliegt, vorgesehen wurde.</p>"
    "<p>Entfällt der Speicherungszweck oder läuft eine vom Europäischen Richtlinien- und Verordnungsgeber oder "
    "einem anderen zuständigen Gesetzgeber vorgeschriebene Speicherfrist ab, werden die personenbezogenen Daten "
    "routinemäßig und entsprechend den gesetzlichen Vorschriften gesperrt oder gelöscht.</p>"
    "<p>Produktempfehlungen und praktische Tipps per E-Mail</p>"
    "<p>Als VoteWorks-Kunde bzw. Bezieher unserer Dienstleistung (z. B. Nutzung einer Demo- oder Test-Version) "
    "erhalten Sie von uns regelmäßig Produktempfehlungen und praktische Tipps per E-Mail. Diese Produktempfehlungen "
    "erhalten Sie von uns unabhängig davon, ob Sie einen Newsletter abonniert haben. Wir wollen Sie auf diese Weise "
    "über Produkte aus unserem Angebot informieren, die Sie interessieren könnten. Außerdem erhalten Sie hier "
    "wertvolle Tipps zu der Nutzung unserer Software.</p>"
    "<p>Sofern Sie keine Produktempfehlungen oder insgesamt keine werblichen Nachrichten mehr von uns erhalten wollen, "
    "können Sie dem jederzeit widersprechen. Richten Sie Ihren Widerspruch bitte in Textform "
    "(z. B. E-Mail, Fax, Brief) an unsere Kontaktadresse. Selbstverständlich finden Sie auch am Ende jeder "
    "E-Mail einen Abmelde-Link.</p>"
    "<p>Rechtsgrundlage ist Art. 6 Abs. 1 UAbs. 1 lit. f DSGVO sowie § 7 Abs. 3 UWG.</p>"
    "<p>Datensicherheit</p>"
    "<p>Wir haben technische und organisatorische Sicherheitsmaßnahmen getroffen, um Ihre personenbezogenen Daten "
    "vor Verlust, Zerstörung, Manipulation und unberechtigten Zugriff zu schützen. Alle unsere Mitarbeiter und alle "
    "an der Datenverarbeitung beteiligten Dritten sind auf das Bundesdatenschutzgesetz und den vertraulichen "
    "Umgang mit personenbezogenen Daten verpflichtet.</p>"
    "<p>Im Falle der Erhebung und Verarbeitung personenbezogener Daten über unsere Webseite werden die Informationen "
    "in verschlüsselter Form übertragen, um einem Missbrauch durch Dritte vorzubeugen. "
    "Unsere Sicherungsmaßnahmen werden entsprechend der technologischen Entwicklung fortlaufend überarbeitet.</p>"
    "<p>Kontaktmöglichkeit über die Internetseite Vote@Home</p>"
    "<p>Die Internetseite Vote@Home der VoteWorks GmbH enthält aufgrund von gesetzlichen Vorschriften Angaben, "
    "die eine schnelle elektronische Kontaktaufnahme zu unserem Unternehmen sowie eine unmittelbare Kommunikation "
    "mit uns ermöglichen, was ebenfalls eine allgemeine Adresse der sogenannten elektronischen Post (E-Mail-Adresse) "
    "umfasst. Sofern eine betroffene Person per E-Mail oder über ein Kontaktformular den Kontakt mit dem für "
    "die Verarbeitung Verantwortlichen aufnimmt, werden die von der betroffenen Person übermittelten "
    "personenbezogenen Daten automatisch gespeichert. Solche auf freiwilliger Basis von einer betroffenen Person "
    "an den für die Verarbeitung Verantwortlichen übermittelten personenbezogenen Daten werden für Zwecke "
    "der Bearbeitung oder der Kontaktaufnahme zur betroffenen Person gespeichert.</p>"
    "<p>Neben der rein informatorischen Nutzung unserer Website bieten wir verschiedene Leistungen an, die Sie "
    "bei Interesse nutzen können. Dazu müssen Sie in der Regel weitere personenbezogene Daten angeben, die wir "
    "zur Erbringung der jeweiligen Leistung nutzen und für die die zuvor genannten Grundsätze "
    "zur Datenverarbeitung gelten.</p>"
    "<p>Es erfolgt keine Weitergabe dieser personenbezogenen Daten an Dritte außer an unsere rechtlich "
    "selbstständigen örtlichen Vertragshändler.</p>"
    "<p>Datenschutz bei Bewerbungen und im Bewerbungsverfahren<br>Der für die Verarbeitung Verantwortliche erhebt "
    "und verarbeitet die personenbezogenen Daten von Bewerbern zum Zwecke der Abwicklung des Bewerbungsverfahrens. "
    "Die Verarbeitung kann auch auf elektronischem Wege erfolgen. Dies ist insbesondere dann der Fall, wenn "
    "ein Bewerber entsprechende Bewerbungsunterlagen auf dem elektronischen Wege, beispielsweise per E-Mail oder "
    "über ein auf der Internetseite befindliches Webformular, an den für die Verarbeitung Verantwortlichen "
    "übermittelt. Schließt der für die Verarbeitung Verantwortliche einen Anstellungsvertrag mit einem Bewerber, "
    "werden die übermittelten Daten zum Zwecke der Abwicklung des Beschäftigungsverhältnisses unter Beachtung "
    "der gesetzlichen Vorschriften gespeichert.</p>"
    "<p>Sollten wir dem Bewerber keine zu besetzende Stelle anbieten können, jedoch aufgrund des Bewerberprofils "
    "der Ansicht sein, dass die Bewerbung eventuell für zukünftige Stellenangebote interessant sein könnte, "
    "werden wir die persönlichen Bewerbungsdaten zwölf Monate lang speichern, sofern der Bewerber einer solchen "
    "Speicherung und Nutzung nicht widerspricht. Eine Weitergabe an Dritte Ihrer Daten erfolgt in keinem Fall.</p>"
    "<p>Rechtsgrundlage der Verarbeitung<br>Art. 6 I lit. a DSGVO dient unserem Unternehmen als Rechtsgrundlage "
    "für Verarbeitungsvorgänge, bei denen wir eine Einwilligung für einen bestimmten Verarbeitungszweck einholen. "
    "Ist die Verarbeitung personenbezogener Daten zur Erfüllung eines Vertrags, dessen Vertragspartei die "
    "betroffene Person ist, erforderlich, wie dies beispielsweise bei Verarbeitungsvorgängen der Fall ist, die für "
    "eine Lieferung von Waren oder die Erbringung einer sonstigen Leistung oder Gegenleistung notwendig sind, "
    "so beruht die Verarbeitung auf Art. 6 I lit. b DSGVO. Gleiches gilt für solche Verarbeitungsvorgänge, die "
    "zur Durchführung vorvertraglicher Maßnahmen erforderlich sind, etwa in Fällen von Anfragen zur "
    "unseren Produkten oder Leistungen. Unterliegt unser Unternehmen einer rechtlichen Verpflichtung, durch welche "
    "eine Verarbeitung von personenbezogenen Daten erforderlich wird, wie beispielsweise zur Erfüllung "
    "steuerlicher Pflichten, so basiert die Verarbeitung auf Art. 6 I lit. c DSGVO.</p>"
    "<p>In seltenen Fällen könnte die Verarbeitung von personenbezogenen Daten erforderlich werden, um "
    "lebenswichtige Interessen der betroffenen Person oder einer anderen natürlichen Person zu schützen. "
    "Dies wäre beispielsweise der Fall, wenn ein Besucher in unserem Betrieb verletzt werden würde und daraufhin "
    "sein Name, sein Alter, seine Krankenkassendaten oder sonstige lebenswichtige Informationen an einen Arzt, "
    "ein Krankenhaus oder sonstige Dritte weitergegeben werden müssten. Dann würde die Verarbeitung auf "
    "Art. 6 I lit. d DSGVO beruhen. Letztlich könnten Verarbeitungsvorgänge auf Art. 6 I lit. f DSGVO beruhen. "
    "Auf dieser Rechtsgrundlage basieren Verarbeitungsvorgänge, die von keiner der vorgenannten Rechtsgrundlagen "
    "erfasst werden, wenn die Verarbeitung zur Wahrung eines berechtigten Interesses unseres Unternehmens oder "
    "eines Dritten erforderlich ist, sofern die Interessen, Grundrechte und Grundfreiheiten des Betroffenen "
    "nicht überwiegen. Solche Verarbeitungsvorgänge sind uns insbesondere deshalb gestattet, weil sie durch "
    "den Europäischen Gesetzgeber besonders erwähnt wurden. Er vertrat insoweit die Auffassung, dass ein "
    "berechtigtes Interesse anzunehmen sein könnte, wenn die betroffene Person ein Kunde des Verantwortlichen ist "
    "(Erwägungsgrund 47 Satz 2 DSGVO).</p>"
    "<p>Berechtigte Interessen an der Verarbeitung, die von dem Verantwortlichen oder einem Dritten verfolgt werden<br>"
    "Basiert die Verarbeitung personenbezogener Daten auf Artikel 6 I lit. f DSGVO, ist unser berechtigtes "
    "Interesse die Durchführung unserer Geschäftstätigkeit zugunsten des Wohlergehens all unserer "
    "Mitarbeiter und unserer Anteilseigner.</p>"
    "<p>Dauer, für die die personenbezogenen Daten gespeichert werden<br>Das Kriterium für die Dauer "
    "der Speicherung von personenbezogenen Daten ist die jeweilige gesetzliche Aufbewahrungsfrist. "
    "Nach Ablauf der Frist werden die entsprechenden Daten routinemäßig gelöscht, sofern sie nicht mehr "
    "zur Vertragserfüllung oder Vertragsanbahnung erforderlich sind.</p>"
    "<p>Gesetzliche oder vertragliche Vorschriften zur Bereitstellung der personenbezogenen Daten; "
    "Erforderlichkeit für den Vertragsabschluss; Verpflichtung der betroffenen Person, die personenbezogenen "
    "Daten bereitzustellen; mögliche Folgen der Nichtbereitstellung<br>Wir klären Sie darüber auf, dass "
    "die Bereitstellung personenbezogener Daten zum Teil gesetzlich vorgeschrieben ist (z.B. Steuervorschriften) "
    "oder sich auch aus vertraglichen Regelungen (z.B. Angaben zum Vertragspartner) ergeben kann. Mitunter kann "
    "es zu einem Vertragsschluss erforderlich sein, dass eine betroffene Person uns personenbezogene Daten "
    "zur Verfügung stellt, die in der Folge durch uns verarbeitet werden müssen. Die betroffene Person ist "
    "beispielsweise verpflichtet uns personenbezogene Daten bereitzustellen, wenn unser Unternehmen mit "
    "ihr einen Vertrag abschließt.</p>"
    "<p>Eine Nichtbereitstellung der personenbezogenen Daten hätte zur Folge, dass der Vertrag mit dem Betroffenen "
    "nicht geschlossen werden könnte. Vor einer Bereitstellung personenbezogener Daten durch den Betroffenen "
    "muss sich der Betroffene an einen unserer Mitarbeiter wenden. Unser Mitarbeiter klärt den Betroffenen "
    "einzelfallbezogen darüber auf, ob die Bereitstellung der personenbezogenen Daten gesetzlich oder vertraglich "
    "vorgeschrieben oder für den Vertragsabschluss erforderlich ist, ob eine Verpflichtung besteht, die "
    "personenbezogenen Daten bereitzustellen, und welche Folgen die Nichtbereitstellung "
    "der personenbezogenen Daten hätte.</p>"
    "<p>Änderung unserer Datenschutzbestimmungen<br>Wir behalten uns das Recht vor, diese Datenschutzerklärung "
    "bei Gelegenheit anzupassen, falls dies aufgrund rechtlichen Anforderungen, neuer Technologien oder "
    "Veränderungen unserer Dienstleistungen erforderlich sein sollte, z.B. bei der "
    "Einführung neuer Serviceleistungen.</p>"
    "<p>Werden grundlegende Änderungen an unserer Datenschutzerklärung vorgenommen, geben wir "
    "diese auf unserer Website bekannt. Für Ihren wiederholten Besuch auf unserer Internetseite gilt dann die "
    "neue Datenschutzerklärung.</p>"
    "<p>2. Datenschutzerklärung Begriffsbestimmungen</p>"
    "<p>Personenbezogene Daten<br>Personenbezogene Daten sind alle Informationen, die sich auf eine identifizierte "
    "oder identifizierbare natürliche Person (im Folgenden „betroffene Person“) beziehen. Als identifizierbar "
    "wird eine natürliche Person angesehen, die direkt oder indirekt, insbesondere mittels Zuordnung zu einer "
    "Kennung wie einem Namen, zu einer Kennnummer, zu Standortdaten, zu einer Online-Kennung oder zu einem oder "
    "mehreren besonderen Merkmalen, die Ausdruck der physischen, physiologischen, genetischen, "
    "psychischen, wirtschaftlichen, kulturellen oder sozialen Identität dieser natürlichen Person sind, "
    "identifiziert werden kann.</p>"
    "<p>Betroffene Person<br>Betroffene Person ist jede identifizierte oder identifizierbare natürliche Person, "
    "deren personenbezogene Daten von dem für die Verarbeitung Verantwortlichen verarbeitet werden.</p>"
    "<p>Verarbeitung<br>Verarbeitung ist jeder mit oder ohne Hilfe automatisierter Verfahren ausgeführte Vorgang "
    "oder jede solche Vorgangsreihe im Zusammenhang mit personenbezogenen Daten wie das Erheben, das Erfassen, "
    "die Organisation, das Ordnen, die Speicherung, die Anpassung oder Veränderung, das Auslesen, das Abfragen, "
    "die Verwendung, die Offenlegung durch Übermittlung, Verbreitung oder eine andere Form der Bereitstellung, "
    "den Abgleich oder die Verknüpfung, die Einschränkung, das Löschen oder die Vernichtung.</p>"
    "<p>Einschränkung der Verarbeitung<br>Einschränkung der Verarbeitung ist die Markierung gespeicherter "
    "personenbezogener Daten mit dem Ziel, ihre künftige Verarbeitung einzuschränken.</p>"
    "<p>Profiling<br>Profiling ist jede Art der automatisierten Verarbeitung personenbezogener Daten, die darin "
    "besteht, dass diese personenbezogenen Daten verwendet werden, um bestimmte persönliche Aspekte, die sich "
    "auf eine natürliche Person beziehen, zu bewerten, analysieren oder vorherzusagen.</p>"
    "<p>Pseudonymisierung<br>Pseudonymisierung ist die Verarbeitung personenbezogener Daten in einer Weise, auf "
    "welche die personenbezogenen Daten ohne Hinzuziehung zusätzlicher Informationen nicht mehr einer spezifischen "
    "betroffenen Person zugeordnet werden können, sofern diese zusätzlichen Informationen gesondert aufbewahrt "
    "werden und technischen und organisatorischen Maßnahmen unterliegen, die gewährleisten, dass die personenbezogenen "
    "Daten nicht einer identifizierten oder identifizierbaren natürlichen Person zugewiesen werden.</p>"
    "<p>Verantwortlicher oder für die Verarbeitung Verantwortlicher<br>Verantwortlicher oder für die Verarbeitung "
    "Verantwortlicher ist die natürliche oder juristische Person, Behörde, Einrichtung oder andere Stelle, die "
    "allein oder gemeinsam mit anderen über die Zwecke und Mittel der Verarbeitung von personenbezogenen Daten "
    "entscheidet. Sind die Zwecke und Mittel dieser Verarbeitung durch das Unionsrecht oder das Recht der "
    "Mitgliedstaaten vorgegeben, so kann der Verantwortliche beziehungsweise können die bestimmten Kriterien "
    "seiner Benennung nach dem Unionsrecht oder dem Recht der Mitgliedstaaten vorgesehen werden.</p>"
    "<p>Auftragsverarbeiter<br>Auftragsverarbeiter ist eine natürliche oder juristische Person, Behörde, "
    "Einrichtung oder andere Stelle, die personenbezogene Daten im Auftrag des Verantwortlichen verarbeitet.</p>"
    "<p>Empfänger<br>Empfänger ist eine natürliche oder juristische Person, Behörde, Einrichtung oder andere Stelle, "
    "der personenbezogene Daten offengelegt werden, unabhängig davon, ob es sich bei ihr um einen Dritten handelt "
    "oder nicht. Behörden, die im Rahmen eines bestimmten Untersuchungsauftrags nach dem Unionsrecht oder dem Recht "
    "der Mitgliedstaaten möglicherweise personenbezogene Daten erhalten, gelten jedoch nicht als Empfänger.</p>"
    "<p>Dritter<br>Dritter ist eine natürliche oder juristische Person, Behörde, Einrichtung oder andere Stelle "
    "außer der betroffenen Person, dem Verantwortlichen, dem Auftragsverarbeiter und den Personen, die unter der "
    "unmittelbaren Verantwortung des Verantwortlichen oder des Auftragsverarbeiters befugt sind, die "
    "personenbezogenen Daten zu verarbeiten.</p>"
    "<p>Einwilligung<br>Einwilligung ist jede von der betroffenen Person freiwillig für den bestimmten Fall in "
    "informierter Weise und unmissverständlich abgegebene Willensbekundung in Form einer Erklärung oder einer "
    "sonstigen eindeutigen bestätigenden Handlung, mit der die betroffene Person zu verstehen gibt, dass sie mit "
    "der Verarbeitung der sie betreffenden personenbezogenen Daten einverstanden ist.</p>"
    "<p>3. Datenerfassung auf unserer Website</p>"
    "<p>Cookies<br>Die Internetseiten verwenden teilweise sogenannte Cookies. Cookies richten auf Ihrem Rechner "
    "keinen Schaden an und enthalten keine Viren. Cookies dienen dazu, unser Angebot nutzerfreundlicher, "
    "effektiver und sicherer zu machen. Cookies sind kleine Textdateien, die auf Ihrem Rechner abgelegt werden "
    "und die Ihr Browser speichert.</p>"
    "<p>Die meisten der von uns verwendeten Cookies sind so genannte “Session-Cookies”. Sie werden nach Ende "
    "Ihres Besuchs automatisch gelöscht. Andere Cookies bleiben auf Ihrem Endgerät gespeichert bis Sie diese löschen. "
    "Diese Cookies ermöglichen es uns, Ihren Browser beim nächsten Besuch wiederzuerkennen.</p>"
    "<p>Sie können Ihren Browser so einstellen, dass Sie über das Setzen von Cookies informiert werden und "
    "Cookies nur im Einzelfall erlauben, die Annahme von Cookies für bestimmte Fälle oder generell ausschließen "
    "sowie das automatische Löschen der Cookies beim Schließen des Browser aktivieren. Bei der Deaktivierung "
    "von Cookies kann die Funktionalität dieser Website eingeschränkt sein.</p>"
    "<p>Cookies, die zur Durchführung des elektronischen Kommunikationsvorgangs oder zur Bereitstellung bestimmter, "
    "von Ihnen erwünschter Funktionen (z.B. Warenkorbfunktion) erforderlich sind, werden auf Grundlage "
    "von Art. 6 Abs. 1 lit. f DSGVO gespeichert. Der Websitebetreiber hat ein berechtigtes Interesse an der "
    "Speicherung von Cookies zur technisch fehlerfreien und optimierten Bereitstellung seiner Dienste. "
    "Soweit andere Cookies (z.B. Cookies zur Analyse Ihres Surfverhaltens) gespeichert werden, werden diese in "
    "dieser Datenschutzerklärung gesondert behandelt.</p>"
    "<p>Server-Log-Dateien<br>Der Provider der Seiten erhebt und speichert automatisch Informationen in so "
    "genannten Server-Log-Dateien, die Ihr Browser automatisch an uns übermittelt.</p>"
    "<p>Dies sind:</p>"
    "<p>* Browsertyp und Browserversion</p>"
    "<p>* verwendetes Betriebssystem</p>"
    "<p>* Referrer URL</p>"
    "<p>* Hostname des zugreifenden Rechners</p>"
    "<p>* Uhrzeit der Serveranfrage</p>"
    "<p>* IP-Adresse</p>"
    "<p>Eine Zusammenführung dieser Daten mit anderen Datenquellen wird nicht vorgenommen.<br>"
    "Grundlage für die Datenverarbeitung ist Art. 6 Abs. 1 lit. b DSGVO, der die Verarbeitung von Daten "
    "zur Erfüllung eines Vertrags oder vorvertraglicher Maßnahmen gestattet.</p>"
    "<p>Kontaktformular</p>"
    "<p>Wenn Sie uns per Kontaktformular Anfragen zukommen lassen, werden Ihre Angaben aus dem Anfrageformular "
    "inklusive der von Ihnen dort angegebenen Kontaktdaten zwecks Bearbeitung der Anfrage und für den Fall "
    "von Anschlussfragen bei uns gespeichert. Diese Daten geben wir nicht ohne Ihre Einwilligung weiter.</p>"
    "<p>Die Verarbeitung der in das Kontaktformular eingegebenen Daten erfolgt somit ausschließlich auf "
    "Grundlage Ihrer Einwilligung (Art. 6 Abs. 1 lit. a DSGVO). Sie können diese Einwilligung jederzeit widerrufen. "
    "Dazu reicht eine formlose Mitteilung per E-Mail an uns. Die Rechtmäßigkeit der bis zum Widerruf erfolgten "
    "Datenverarbeitungsvorgänge bleibt vom Widerruf unberührt.</p>"
    "<p>Die von Ihnen im Kontaktformular eingegebenen Daten verbleiben bei uns, bis Sie uns zur Löschung auffordern, "
    "Ihre Einwilligung zur Speicherung widerrufen oder der Zweck für die Datenspeicherung entfällt "
    "(z.B. nach abgeschlossener Bearbeitung Ihrer Anfrage). Zwingende gesetzliche Bestimmungen "
    "– insbesondere Aufbewahrungsfristen – bleiben unberührt.</p>"
    "<p>Verarbeiten von Daten (Kunden- und Vertragsdaten)</p>"
    "<p>Wir erheben, verarbeiten und nutzen personenbezogene Daten nur, soweit sie für die Begründung, "
    "inhaltliche Ausgestaltung oder Änderung des Rechtsverhältnisses erforderlich sind (Bestandsdaten). "
    "Dies erfolgt auf Grundlage von Art. 6 Abs. 1 lit. b DSGVO, der die Verarbeitung von Daten zur Erfüllung "
    "eines Vertrags oder vorvertraglicher Maßnahmen gestattet. Personenbezogene Daten über die Inanspruchnahme "
    "unserer Internetseiten (Nutzungsdaten) erheben, verarbeiten und nutzen wir nur, soweit dies erforderlich ist, "
    "um dem Nutzer die Inanspruchnahme des Dienstes zu ermöglichen oder abzurechnen.</p>"
    "<p>Die erhobenen Kundendaten werden nach Abschluss des Auftrags oder Beendigung der Geschäftsbeziehung gelöscht. "
    "Gesetzliche Aufbewahrungsfristen bleiben unberührt.</p>"
    "<p>Datenübermittlung bei Vertragsschluss für Dienstleistungen und digitale Inhalte<br>Wir übermitteln "
    "personenbezogene Daten an Dritte nur dann, wenn dies im Rahmen der Vertragsabwicklung notwendig ist, "
    "etwa an das mit der Zahlungsabwicklung beauftragte Kreditinstitut.</p>"
    "<p>Eine weitergehende Übermittlung der Daten erfolgt nicht bzw. nur dann, wenn Sie der Übermittlung "
    "ausdrücklich zugestimmt haben. Eine Weitergabe Ihrer Daten an Dritte ohne ausdrückliche Einwilligung, "
    "etwa zu Zwecken der Werbung, erfolgt nicht.</p>"
    "<p>Grundlage für die Datenverarbeitung ist Art. 6 Abs. 1 lit. b DSGVO, der die Verarbeitung von Daten "
    "zur Erfüllung eines Vertrags oder vorvertraglicher Maßnahmen gestattet.</p>"
    "<p>4.&nbsp;Datenschutzbestimmungen zu Einsatz und Verwendung von YouTube</p>"
    "<p>Der für die Verarbeitung Verantwortliche hat auf dieser Internetseite Komponenten von YouTube integriert. "
    "YouTube ist ein Internet-Videoportal, dass Video-Publishern das kostenlose Einstellen von Videoclips und anderen Nutzern die ebenfalls kostenfreie Betrachtung, Bewertung und Kommentierung dieser ermöglicht. YouTube gestattet die Publikation aller Arten von Videos, weshalb sowohl komplette Film- und Fernsehsendungen, aber auch Musikvideos, Trailer oder von Nutzern selbst angefertigte Videos über das Internetportal abrufbar sind.</p>"
    "<p>Betreibergesellschaft von YouTube ist die YouTube, LLC, 901 Cherry Ave., San Bruno, CA 94066, USA. "
    "Die YouTube, LLC ist einer Tochtergesellschaft der Google Inc., 1600 Amphitheatre Pkwy, Mountain View, "
    "CA 94043-1351, USA.</p>"
    "<p>Durch jeden Aufruf einer der Einzelseiten dieser Internetseite, die durch den für die Verarbeitung "
    "Verantwortlichen betrieben wird und auf welcher eine YouTube-Komponente (YouTube-Video) integriert wurde, "
    "wird der Internetbrowser auf dem informationstechnologischen System der betroffenen Person automatisch durch "
    "die jeweilige YouTube-Komponente veranlasst, eine Darstellung der entsprechenden YouTube-Komponente von "
    "YouTube herunterzuladen. Weitere Informationen zu YouTube können unter https://www.youtube.com/yt/about/de/ "
    "abgerufen werden. Im Rahmen dieses technischen Verfahrens erhalten YouTube und Google Kenntnis darüber, "
    "welche konkrete Unterseite unserer Internetseite durch die betroffene Person besucht wird.</p>"
    "<p>Sofern die betroffene Person gleichzeitig bei YouTube eingeloggt ist, erkennt YouTube mit dem "
    "Aufruf einer Unterseite, die ein YouTube-Video enthält, welche konkrete Unterseite unserer Internetseite "
    "die betroffene Person besucht. Diese Informationen werden durch YouTube und Google gesammelt und dem "
    "jeweiligen YouTube-Account der betroffenen Person zugeordnet.</p>"
    "<p>YouTube und Google erhalten über die YouTube-Komponente immer dann eine Information darüber, dass "
    "die betroffene Person unsere Internetseite besucht hat, wenn die betroffene Person zum Zeitpunkt des "
    "Aufrufs unserer Internetseite gleichzeitig bei YouTube eingeloggt ist; dies findet unabhängig davon statt, "
    "ob die betroffene Person ein YouTube-Video anklickt oder nicht. Ist eine derartige Übermittlung dieser "
    "Informationen an YouTube und Google von der betroffenen Person nicht gewollt, kann diese "
    "die Übermittlung dadurch verhindern, dass sie sich vor einem Aufruf unserer Internetseite aus "
    "ihrem YouTube-Account ausloggt.</p>"
    "<p>Die von YouTube veröffentlichten Datenschutzbestimmungen, die unter "
    "https://www.google.de/intl/de/policies/privacy/ abrufbar sind, geben Aufschluss über die Erhebung, "
    "Verarbeitung und Nutzung personenbezogener Daten durch YouTube und Google.</p>"
    "<p>5. Newsletter</p>"
    "<p>Newsletterdaten<br>Wenn Sie den auf der Website angebotenen Newsletter beziehen möchten, benötigen wir von "
    "Ihnen eine E-Mail-Adresse sowie Informationen, welche uns die Überprüfung gestatten, dass Sie der Inhaber "
    "der angegebenen E-Mail-Adresse sind und mit dem Empfang des Newsletters einverstanden sind. Weitere "
    "Daten werden nicht bzw. nur auf freiwilliger Basis erhoben. Diese Daten verwenden wir ausschließlich "
    "für den Versand der angeforderten Informationen und geben diese nicht an Dritte weiter.</p>"
    "<p>Die Verarbeitung der in das Newsletteranmeldeformular eingegebenen Daten erfolgt ausschließlich auf "
    "Grundlage Ihrer Einwilligung (Art. 6 Abs. 1 lit. a DSGVO). Die erteilte Einwilligung zur Speicherung der "
    "Daten, der E-Mail-Adresse sowie deren Nutzung zum Versand des Newsletters können Sie jederzeit widerrufen, "
    "etwa über den „Austragen“-Link im Newsletter. Die Rechtmäßigkeit der bereits erfolgten "
    "Datenverarbeitungsvorgänge bleibt vom Widerruf unberührt.</p>"
    "<p>Die von Ihnen zum Zwecke des Newsletter-Bezugs bei uns hinterlegten Daten werden von uns bis zu "
    "Ihrer Austragung aus dem Newsletter gespeichert und nach der Abbestellung des Newsletters gelöscht. "
    "Daten, die zu anderen Zwecken bei uns gespeichert wurden (z.B. E-Mail-Adressen für den Mitgliederbereich) "
    "bleiben hiervon unberührt.</p>"
    "<p>Newsletter2Go</p>"
    "<p>Diese Website nutzt die Dienste von Newsletter2Go für den Versand von Newslettern. "
    "Anbieter ist die Newsletter2GO GmbH, Köpenicker Str. 126, 10179 Berlin.</p>"
    "<p>Newsletter2Go ist ein Dienst, mit dem u.a. der Versand von Newslettern organisiert und analysiert werden kann. "
    "Wenn Sie Daten zum Zwecke des Newsletterbezugs eingeben (z.B. E-Mail-Adresse), werden diese auf den Servern "
    "von Newsletter2GO oder seinen Dienstleistern in Deutschland oder der EU gespeichert.</p>"
    "<p>Newsletter2GO verfügt über eine Zertifizierung nach dem “EU-US-Privacy-Shield”. Der “Privacy-Shield” ist "
    "ein Übereinkommen zwischen der Europäischen Union (EU) und den USA, das die Einhaltung europäischer "
    "Datenschutzstandards in den USA gewährleisten soll.</p>"
    "<p>Wenn Sie den auf der Webseite angebotenen Newsletter beziehen möchten, benötigen wir von Ihnen eine "
    "E-Mail-Adresse sowie Informationen, welche uns die Überprüfung gestatten, dass Sie der Inhaber der angegebenen "
    "E-Mail-Adresse und mit dem Empfang des Newsletters einverstanden sind.</p>"
    "<p>Zur Gewährleistung einer einverständlichen Newsletter-Versendung nutzen wir das sogenannte "
    "Double-Opt-in-Verfahren. Im Zuge dessen lässt sich der potentielle Empfänger in einen Verteiler aufnehmen. "
    "Anschließend erhält der Nutzer durch eine Bestätigungs-E-Mail die Möglichkeit, die Anmeldung rechtssicher "
    "zu bestätigen. Nur wenn die Bestätigung erfolgt, wird die Adresse aktiv in den Verteiler aufgenommen.</p>"
    "<p>Diese Daten verwenden wir ausschließlich für den Versand der angeforderten Informationen und Angebote.</p>"
    "<p>Als Newsletter Software wird Newsletter2Go verwendet. Ihre Daten werden dabei an die Newsletter2Go GmbH "
    "übermittelt. Newsletter2Go ist es dabei untersagt, Ihre Daten zu verkaufen und für andere Zwecke, als für "
    "den Versand von Newslettern zu nutzen. Newsletter2Go ist ein deutscher, zertifizierter Anbieter, welcher "
    "nach den Anforderungen der Datenschutz-Grundverordnung und des Bundesdatenschutzgesetzes ausgewählt wurde.</p>"
    "<p>Weitere Informationen finden Sie hier: https://www.newsletter2go.de/informationen-newsletter-empfaenger/</p>"
    "<p>Die erteilte Einwilligung zur Speicherung der Daten, der E-Mail-Adresse sowie deren Nutzung zum Versand "
    "des Newsletters können Sie jederzeit widerrufen, etwa über den „Abmelden“-Link im Newsletter.</p>"
    "<p>Abschluss eines Vertrags zur Auftragsverarbeitung<br>Wir haben einen sog. “Vertrag zur Auftragsverarbeitung” "
    "mit Newsletter2GO abgeschlossen, in dem wir Newsletter2Go verpflichten, die Daten unserer Kunden zu schützen und "
    "sie nicht an Dritte weiterzugeben.</p>"
    "<p>Vote@Home™&nbsp;ist das Produkt einer engen Zusammenarbeit mit Versammlungsleitern, die das "
    "Produkt regelmässig auf (virtuellen) Versammlungen&nbsp;einsetzen und stetig weiterentwickeln.&nbsp;Gerne "
    "nehmen wir auch Ihre Anregungen bezüglich hilfreicher Verbesserungen entgegen.</p>"
)

_welcome_text = (
    "<p>Für die Teilnahme an der Veranstaltung und der Stimmabgabe zu den anstehenden Beschlüssen und Wahlen stehen "
    "Ihnen zwei Möglichkeiten zur Verfügung:</p>"
    "<p>Sie können die Videokonferenz und die Abstimmungen auf ein und demselben Endgerät verfolgen bzw. vornehmen. "
    "Dazu nutzen Sie Ihren PC oder Notebook und ordnen beide Anwendungen (Videokonferenz und vote@home) nebeneinander "
    "auf Ihrem Bildschirm an.&nbsp;Zur Einrichtung Ihres Bildschirms für diese Form der Teilnahme folgen Sie "
    "einfach der Anleitung weiter unten in diesem Text.</p>"
    "<p>Alternativ können Sie die Videokonferenz über Ihren PC oder Notebook verfolgen und nehmen "
    "<strong>parallel </strong>die Abstimmungen über ein mobiles Gerät wie z.B. Smartphone oder Tablett vor. "
    "Hierzu öffen Sie den Link zu Ihrer Veranstaltung auf Ihrem Smart-Device und melden sich mit Ihren "
    "Benutzerdaten an. Sie werden dann automatisch zum aktuellen aufgerufenen TOP geleitet und für "
    "die Beschlussfassungen zur Abgabe Ihrer Stimme aufgefordert.</p>"
    "<p>Um nun der Videokonferenz beizutreten, klicken Sie mit der rechten Maustaste auf den nachstehenden Link "
    "und wählen die Option „In neuem TAB öffnen“:</p><p><strong>Hier Link zur Videokonferenz einfügen</strong></p>"
    "<p>Wenn Sie die Abstimmungen mit einem mobilen Endgerät vornehmen möchten, öffnen Sie nun den Link zu "
    "Ihrer Veranstaltung auf <u>dem mobilen Endgerät</u> und geben Sie Ihre Benutzerdaten ein. "
    "Wenn die Versammlung noch nicht begonnen hat, wird Ihnen die Begrüßungsseite angezeigt, "
    "ansonsten wird Ihnen direkt der aktuell behandelte TOP angezeigt.</p>"
    "<p>Möchten Sie die Videokonferenz und die Abstimmungen von einem Gerät aus verfolgen gehen Sie bitte "
    "folgendermaßen vor:</p>"
    "<p><strong>Ordnen Sie die beiden Browserfenster auf Ihrem Bildschirm nebeneinander an.<br>"
    "Halbieren Sie dazu zunächst die Fenstergröße. Klicken Sie nun auf den oberen Rand des Fensters und ziehen es "
    "mit gedrückter linker Maustaste an die gewünschte Position.</strong><br>"
    "<em>Zusätzlich finden Sie den Vorgang&nbsp;"
    "<a href=\"/media/file/VoteHome-VC-anordnen.mp4\">hier nochmal in einem Video erklärt</a>&nbsp; "
    "(Bitte starten sie das Video mit rechtem Mausklick über die Option „Link In neuem Tab öffnen“):</em></p>"
)

def get_config_variables():
    """
    Generator which yields all config variables of this app.

    There are two main groups: 'General' and 'Projector'. The group 'General'
    has subgroups. The generator has to be evaluated during app loading
    (see apps.py).
    """
    yield ConfigVariable(
        name='general_event_name',
        default_value='Musterversammlung',
        label='Event name',
        weight=110,
        group='General',
        subgroup='Event',
        validators=(MaxLengthValidator(100),))

    yield ConfigVariable(
        name='general_event_description',
        default_value='Virtuelle Versammlung',
        label='Short description of event',
        weight=115,
        group='General',
        subgroup='Event',
        validators=(MaxLengthValidator(100),))

    yield ConfigVariable(
        name='general_event_date',
        default_value='',
        label='Event date',
        weight=120,
        group='General',
        subgroup='Event')

    yield ConfigVariable(
        name='general_event_location',
        default_value='Online Veranstaltung',
        label='Event location',
        weight=125,
        group='General',
        subgroup='Event')

    yield ConfigVariable(
        name='general_event_legal_notice',
        default_value=_legal_notice,
        input_type='markupText',
        label='Legal notice',
        weight=132,
        group='General',
        subgroup='Event')

    yield ConfigVariable(
        name='general_event_privacy_policy',
        default_value=_privacy_policy,
        input_type='markupText',
        label='Privacy policy',
        weight=132,
        group='General',
        subgroup='Event')

    yield ConfigVariable(
        name='general_event_welcome_title',
        default_value='Herzlich Willkommen zu Ihrer Vote@Home Versammlung',
        label='Front page title',
        weight=134,
        group='General',
        subgroup='Event')

    yield ConfigVariable(
        name='general_event_welcome_text',
        default_value=_welcome_text,
        input_type='markupText',
        label='Front page text',
        weight=136,
        group='General',
        subgroup='Event')

    # General System

    yield ConfigVariable(
        name='general_system_enable_anonymous',
        default_value=False,
        input_type='boolean',
        label='Allow access for anonymous guest users',
        weight=138,
        group='General',
        subgroup='System')

    yield ConfigVariable(
        name='general_login_info_text',
        default_value='',
        label='Show this text on the login page',
        weight=140,
        group='General',
        subgroup='System')

    # General export settings

    yield ConfigVariable(
        name='general_csv_separator',
        default_value=',',
        label='Separator used for all csv exports and examples',
        weight=142,
        group='General',
        subgroup='Export')

    yield ConfigVariable(
        name='general_export_pdf_pagenumber_alignment',
        default_value='center',
        input_type='choice',
        label='Page number alignment in PDF',
        choices=(
            {'value': 'left', 'display_name': 'Left'},
            {'value': 'center', 'display_name': 'Center'},
            {'value': 'right', 'display_name': 'Right'}),
        weight=144,
        group='General',
        subgroup='Export')

    yield ConfigVariable(
        name='general_export_pdf_fontsize',
        default_value='10',
        input_type='choice',
        label='Standard font size in PDF',
        choices=(
            {'value': '10', 'display_name': '10'},
            {'value': '11', 'display_name': '11'},
            {'value': '12', 'display_name': '12'}),
        weight=146,
        group='General',
        subgroup='Export')

    # Projector

    yield ConfigVariable(
        name='projector_language',
        default_value='browser',
        input_type='choice',
        label='Projector language',
        choices=(
            {'value': 'browser', 'display_name': 'Current browser language'},
            {'value': 'en', 'display_name': 'English'},
            {'value': 'de', 'display_name': 'Deutsch'},
            {'value': 'fr', 'display_name': 'Français'},
            {'value': 'es', 'display_name': 'Español'},
            {'value': 'pt', 'display_name': 'Português'},
            {'value': 'cs', 'display_name': 'Čeština'},
            {'value': 'ru', 'display_name': 'русский'}),
        weight=150,
        group='Projector')

    yield ConfigVariable(
        name='projector_enable_logo',
        default_value=True,
        input_type='boolean',
        label='Show logo on projector',
        help_text='You can replace the logo by uploading an image and set it as '
                  'the "Projector logo" in "files".',
        weight=152,
        group='Projector')

    yield ConfigVariable(
        name='projector_enable_clock',
        default_value=True,
        input_type='boolean',
        label='Show the clock on projector',
        weight=154,
        group='Projector')

    yield ConfigVariable(
        name='projector_enable_title',
        default_value=True,
        input_type='boolean',
        label='Show title and description of event on projector',
        weight=155,
        group='Projector')

    yield ConfigVariable(
        name='projector_enable_header_footer',
        default_value=True,
        input_type='boolean',
        label='Display header and footer',
        weight=157,
        group='Projector')

    yield ConfigVariable(
        name='projector_header_backgroundcolor',
        default_value='#317796',
        input_type='colorpicker',
        label='Background color of projector header and footer',
        weight=160,
        group='Projector')

    yield ConfigVariable(
        name='projector_header_fontcolor',
        default_value='#F5F5F5',
        input_type='colorpicker',
        label='Font color of projector header and footer',
        weight=165,
        group='Projector')

    yield ConfigVariable(
        name='projector_h1_fontcolor',
        default_value='#317796',
        input_type='colorpicker',
        label='Font color of projector headline',
        weight=170,
        group='Projector')

    yield ConfigVariable(
        name='projector_default_countdown',
        default_value=60,
        input_type='integer',
        label='Predefined seconds of new countdowns',
        weight=185,
        group='Projector')

    yield ConfigVariable(
        name='projector_blank_color',
        default_value='#FFFFFF',
        input_type='colorpicker',
        label='Color for blanked projector',
        weight=190,
        group='Projector')

    yield ConfigVariable(
        name='projector_broadcast',
        default_value=0,
        input_type='integer',
        label='Projector which is broadcasted',
        weight=200,
        group='Projector',
        hidden=True)

    yield ConfigVariable(
        name='projector_currentListOfSpeakers_reference',
        default_value=1,
        input_type='integer',
        label='Projector reference for list of speakers',
        weight=201,
        group='Projector',
        hidden=True)

    # Logos.
    yield ConfigVariable(
        name='logos_available',
        default_value=[
            'logo_projector_main',
            'logo_projector_header',
            'logo_web_header',
            'logo_pdf_header_L',
            'logo_pdf_header_R',
            'logo_pdf_footer_L',
            'logo_pdf_footer_R',
            'logo_pdf_ballot_paper'],
        weight=300,
        group='Logo',
        hidden=True)

    yield ConfigVariable(
        name='logo_projector_main',
        default_value={
            'display_name': 'Projector logo',
            'path': ''},
        input_type='static',
        weight=301,
        group='Logo',
        hidden=True)

    yield ConfigVariable(
        name='logo_projector_header',
        default_value={
            'display_name': 'Projector header image',
            'path': ''},
        input_type='static',
        weight=302,
        group='Logo',
        hidden=True)

    yield ConfigVariable(
        name='logo_web_header',
        default_value={
            'display_name': 'Web interface header logo',
            'path': ''},
        input_type='static',
        weight=303,
        group='Logo',
        hidden=True)

    # PDF logos
    yield ConfigVariable(
        name='logo_pdf_header_L',
        default_value={
            'display_name': 'PDF header logo (left)',
            'path': ''},
        input_type='static',
        weight=310,
        group='Logo',
        hidden=True)

    yield ConfigVariable(
        name='logo_pdf_header_R',
        default_value={
            'display_name': 'PDF header logo (right)',
            'path': ''},
        input_type='static',
        weight=311,
        group='Logo',
        hidden=True)

    yield ConfigVariable(
        name='logo_pdf_footer_L',
        default_value={
            'display_name': 'PDF footer logo (left)',
            'path': ''},
        input_type='static',
        weight=312,
        group='Logo',
        hidden=True)

    yield ConfigVariable(
        name='logo_pdf_footer_R',
        default_value={
            'display_name': 'PDF footer logo (right)',
            'path': ''},
        input_type='static',
        weight=313,
        group='Logo',
        hidden=True)

    yield ConfigVariable(
        name='logo_pdf_ballot_paper',
        default_value={
            'display_name': 'PDF ballot paper logo',
            'path': ''},
        input_type='static',
        weight=314,
        group='Logo',
        hidden=True)

    # Fonts
    yield ConfigVariable(
        name='fonts_available',
        default_value=[
            'font_regular',
            'font_italic',
            'font_bold',
            'font_bold_italic'],
        weight=320,
        group='Font',
        hidden=True)

    yield ConfigVariable(
        name='font_regular',
        default_value={
            'display_name': 'Font regular',
            'default': 'static/fonts/Roboto-Regular.woff',
            'path': ''},
        input_type='static',
        weight=321,
        group='Font',
        hidden=True)

    yield ConfigVariable(
        name='font_italic',
        default_value={
            'display_name': 'Font italic',
            'default': 'static/fonts/Roboto-Medium.woff',
            'path': ''},
        input_type='static',
        weight=321,
        group='Font',
        hidden=True)

    yield ConfigVariable(
        name='font_bold',
        default_value={
            'display_name': 'Font bold',
            'default': 'static/fonts/Roboto-Condensed-Regular.woff',
            'path': ''},
        input_type='static',
        weight=321,
        group='Font',
        hidden=True)

    yield ConfigVariable(
        name='font_bold_italic',
        default_value={
            'display_name': 'Font bold italic',
            'default': 'static/fonts/Roboto-Condensed-Light.woff',
            'path': ''},
        input_type='static',
        weight=321,
        group='Font',
        hidden=True)

    # Custom translations
    yield ConfigVariable(
        name='translations',
        label='Custom translations',
        default_value=[],
        input_type='translations',
        weight=1000,
        group='Custom translations')
