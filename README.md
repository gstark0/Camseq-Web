# CAMSEQ

#### Inteligentny system wsparcia bezpieczeństwa publicznego z wykorzystaniem algorytmów sztucznej inteligencji

<img src="https://raw.githubusercontent.com/gstark0/Camseq-Web/master/pictures/banner.png" width="500">

Zobacz prezentację systemu

[![](http://img.youtube.com/vi/ib39HBUxWwM/0.jpg)](http://www.youtube.com/watch?v=ib39HBUxWwM "Prezentacja systemu")

### O Projekcie
Każdy na świecie powinien mieć prawo czuć się bezpiecznie, nieważne gdzie jest i co robi. To niestety nie zawsze jest możliwe, dlatego jest to problem globalny, zdażają się przecież napaści, pożary czy groźne wypadki samochodowe. Na przeciw temu problemowi występuje system Camseq, który pozwala w czasie rzeczywistym wykrywać i klasyfikować zdarzenia na podstawie obrazu z kamery monitoringu - na głównej ulicy w centrum miasta czy w siedzibie niewielkiej firmy - każdy powinien czuć się bezpiecznie.

Camseq pozwala zarejestrowanym użytkownikom na dodawanie własnych źródeł obrazu. Dzięki temu, władze miast, jak również prywatni właściciele kamer monitoringu mogą wykorzystać system do ujednolicenia infrastruktury i poprawy bezpieczeństwa w całym mieście lub regionie. Taki administrator na swoje konto dostaje powiadomienia o wykrytych zagrożeniach i poważnych niebezpieczeństwach, które z kolei zostają natychmiast nagrywane i administrator od razu ma do nich dostęp.

![](https://raw.githubusercontent.com/gstark0/Camseq-Web/master/pictures/logowanie.png)

![](https://raw.githubusercontent.com/gstark0/Camseq-Web/master/pictures/kamery.png)

Oprócz tego, Camseq na podstawie dodanych kamer analizuje i tworzy wizualizacje bezpieczeństwa w danych regionach miasta wraz z przedstawionymi danymi odnośnie zdarzeń i incydentów.

![](https://raw.githubusercontent.com/gstark0/Camseq-Web/master/pictures/mapa.png)

### Technologia
System Camseq korzysta z technologi uczenia maszynowego, a dokładnie z konwolucyjnych sieci neuronowych, które klasyfikują klatki obrazu pod kątem obecności różnych zdarzeń. Camseq wykorzystuje bibliotekę TensorFlow i Keras do tworzenia modeli sztucznych sieci neuronowych oraz bibliotekę OpenCV do przetwarzania obrazu z kamer. Cały serwer jest postawiony na mikroframeworku zwanym Python-Flask.

### Aktualny postęp
Lista aktualnie zaimplementowanych funkcjonalności:
* System logowania, oddzielne kamery dla różnych kont
* System przetwarzania i wyświetlania obrazu w aplikacji
* Modele sztucznych sieci neuronowych do wykrywania pożarów, bójek oraz wypadków samochodowych
* Klasyfikator kaskadowy do wykrywania broni
* Dziennik zdarzeń/rejestr wszystkich wykrytych incydentów dla danej kamery, wraz z zapisanym z tego momentu obrazem
* Ogólnodostępna mapa z naniesionymi znacznikami określającymi bezpieczeństwo w danej dzielnicy/regionie
* Ogólnodostępny panel z podsumowaniem zdarzeń/incydentów w wybranej dzielnicy/regionie z ostatniego tygodnia i znacznikiem określającym poziom bezpieczeństwa

### Co dalej?
Problem jest globalny, a możliwości systemu dzieki zastosowanym technologiom są praktycznie nieograniczone. Planowaną funkcjonalnością jest wykrywanie i klasyfikowanie większej ilości zdarzeń, takich jak np. kradzieże lub włamania. W dalszej przyszłości można zaimplementować również systemy wykrywające katastrofy środowiskowe - powodzie, huragany i pomagające w lepszym i szybszym planowaniu akcji ratunkowych.