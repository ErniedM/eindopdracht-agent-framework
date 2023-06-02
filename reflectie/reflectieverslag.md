# Reflectie verslag
**Ernie de Magtige - 2ITCSC2 - [Eindopdracht-Repo](https://github.com/ErniedM/eindopdracht-agent-framework)**

---
Aangezien ik meer afiniteit heb met systeemontwikkeling, heb ik ervoor gekozen om een agent-framework te maken. Het idee is om op elke computer van een bedrijf de agent-toepassing te installeren om zo informatie over het computerpark centraal te verzamelen en te valideren.

## De werking
---
Het concept is dat de agent.py-toepassing samen met de benodigde bestanden op elke computer wordt geïnstalleerd. De agent.py-toepassing controleert op regelmatige tijdstippen (momenteel ingesteld op 180 seconden) de GitHub-repository op updates. Als er updates zijn, voert de agent.py-toepassing de vereiste acties uit. De acties worden gedefinieerd in het configuratiebestand. De agent.py-toepassing downloadt en voert de benodigde modules uit voor de acties. Dit wordt gedaan met behulp van de gitpython-module. Door de git-repository naar een tijdelijke directory te downloaden, kunnen we "gemakkelijk" toegang krijgen tot de geëncrypteerde modules. Na de actie wordt de tijdelijke directory verwijderd. De modules worden versleuteld opgeslagen in de GitHub-repository. De agent.py-toepassing zal de modules decrypteren en uitvoeren. De modules verzamelen de vereiste informatie en sturen deze terug naar de GitHub-repository. De sleutel voor het versleutelen en ontsleutelen van de modules wordt opgeslagen in een apart bestand, key.txt. Dit bestand wordt niet opgeslagen in de GitHub-repository, maar het zal beschikbaar zijn op de computers waar de agent.py-toepassing is geïnstalleerd. Het bestand met de sleutel wordt meegeleverd in het zip-bestand op Digitap.

## De features
---
Aangezien het hier gaat om een agent die informatie verzamelt, heb ik ervoor gekozen om de volgende functies te implementeren:

- hardware_inventory.py: Deze module is verantwoordelijk voor het verzamelen van hardware-informatie.
- software_inventory.py: Deze module is verantwoordelijk voor het verzamelen van software-informatie.
- network_inventory.py: Deze module is verantwoordelijk voor het verzamelen van netwerkinformatie.
- system_info.py: Deze module is verantwoordelijk voor het verzamelen van systeeminformatie.

Het is natuurlijk mogelijk om nieuwe modules te schrijven en deze toe te voegen aan de agent.py-toepassing. Denk bijvoorbeeld aan:
- Gebruikers die hebben ingelogd op de computer.
- Het updaten van de computer.
- Het installeren van software.
...

## De keuzes
---
Aangezien de opdracht vereist om het programma te structureren met het oog op overzichtelijkheid, onderhoudbaarheid en herbruikbaarheid van componenten, heb ik ervoor gekozen om een mapstructuur op te zetten. De mapstructuur ziet er als volgt uit:
- config
- logs
- modules
- reflectie

Ik heb er ook voor gekozen om "hulp"-modules te schrijven die de agent.py-toepassing ondersteunen. Deze modules zijn:
- encryption.py: Deze module is specifiek verantwoordelijk voor het versleutelen en ontsleutelen van bestanden.
- github_connector.py: Deze module is specifiek verantwoordelijk voor de communicatie met de GitHub-repository.

Om zo modulair mogelijk te zijn, heb ik ervoor gezorgd dat elke module een collect_data-methode heeft en dat de modules dynamisch kunnen worden geïmporteerd in agent.py, zodat de agent.py-toepassing de vereiste informatie kan verzamelen. Het voordeel hiervan is dat nieuwe modules gemakkelijk kunnen worden toegevoegd zonder dat de agent.py-toepassing hoeft te worden aangepast.

Door het configuratiebestand aan te passen naar behoefte, zal de agent.py-toepassing bij de volgende uitvoering de vereiste modules downloaden en uitvoeren. 

Ik heb ook een time.txt-bestand toegevoegd, zodat de tijdsinterval tussen de oproepen kan worden aangepast. Dit is handig voor het testen van de agent.py-toepassing.

Aanvankelijk heb ik geprobeerd om verbinding te maken met GitHub via de requests-module. Echter, hiermee kon ik alleen lezen van GitHub, maar niet schrijven. Daarom heb ik ervoor gekozen om de gitpython-module te gebruiken om de repository naar een tijdelijke directory te downloaden. 

## De moeilijkheden
---
Over het algemeen heb ik uitgebreide tests uitgevoerd om de volgende uitdagingen te overwinnen:
- Plotse problemen met gitpython, waardoor ik programma's die de import git vereisen niet kon starten.
- Aanvankelijk werkte het uploaden van gegevens naar GitHub niet.
- Problemen met het decrypteren van de modules. De oorzaak was dat ik de geëncrypteerde modules overschreef met de gedecrypteerde modules. Python kon hier niet mee omgaan. De oplossing was om de gedecrypteerde modules een andere naam te geven, zodat de geëncrypteerde modules niet werden overschreven. Dit was uiteindelijk geen probleem, aangezien de tijdelijke repository toch wordt verwijderd.

## Ter info
---
- In het zip-bestand zijn de modules niet geencrypteerd.
- De testen zijn uitgevoerd op een Rocky Linux omgeving maar zouden ook moeten werken op een Windows omgeving en MAC omgeving.
