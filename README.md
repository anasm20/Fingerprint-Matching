# Dokumentation für Fingerprint-Matching-Programm

## Einführung
Dieses Dokument dient zur Erklärung eines Fingerprint-Matching-Programms, das für ein Eintrittssystem entwickelt wurde. Der Code dieses Programms stammt aus GitHub-Repositories der Benutzer "aasthac67" und wurde von "anasm20" weiterentwickelt. 

Das Programm besteht aus drei separaten Code-Segmenten, die verschiedene Schritte im Verarbeitungsprozess für Fingerabdrücke durchführen. Das Hauptziel des Programms besteht darin, Fingerabdrücke zu vergleichen und potenzielle Übereinstimmungen zu identifizieren.

## Code-Segment 1: Hintergrundentfernung
![1](https://github.com/anasm20/Fingerprint-Matching/assets/112882511/9cd44a85-4328-4349-ad25-b2aaf2bce21d)



### Schritt 1: Bildladung
In diesem Schritt wird ein Eingangsbild (z.B., ‘./input/f1.jpeg’) mithilfe von OpenCV geladen und in einem Fenster angezeigt.

Verwendete ‘f1.jpeg’ Foto:
![input](https://github.com/anasm20/Fingerprint-Matching/assets/112882511/0add8910-67d2-4bd3-b473-80a4053be39c)


### Schritt 2: Hintergrundentfernung
Die Hintergrundentfernung wird mithilfe eines GrabCut-Algorithmus durchgeführt. Ein Rechteck um den Fingerabdruck wird als Region von Interesse (ROI) festgelegt, und der Hintergrund wird entfernt.

### Schritt 3: Hintergrund Wiederherstellung
Der Hintergrund wird wieder zum Bild hinzugefügt, und das resultierende Bild wird in einem separaten Datei ('input.jpg') gespeichert.

## Code-Segment 2: Feature-Erkennung und Verarbeitung
![2](https://github.com/anasm20/Fingerprint-Matching/assets/112882511/a431ad35-82f3-4683-8391-2f3f3a76771a)



### Schritt 1: Bildladung
Das Bild, das im vorherigen Code-Segment ('input.jpg') bearbeitet wurde, wird geladen.

### Schritt 2: Bildschärfung
Das Bild wird mit einem Schärfung Kern bearbeitet, um Kanten und Merkmale zu zeigen.

### Schritt 3: Konvertierung in Graustufen
Das Bild wird in Graustufen umgewandelt, um die Verarbeitung zu erleichtern.

### Schritt 4: Histogrammausgleich
Es wird eine Histogrammausgleichung angewendet, um den Kontrast des Bildes zu erhöhen.

### Schritt 5: Ridge Detection
Mithilfe des Hessian-Matrix werden Kanten (Ridges) im Bild erkannt, und die Ergebnisse werden visualisiert.

### Schritt 6: Binarisierung
Das in Schritt 5 erzeugte Bild wird in ein binäres Bild umgewandelt und verschiedene Bildverarbeitungsschritte werden angewendet.

### Schritt 7: Thinning-Algorithmus
Ein Thinning- oder Skeleton-Sierungs-Algorithmus wird auf das binäre Bild angewendet, und das Ergebnis wird gespeichert.

## Code-Segment 3: Vergleich von Fingerabdrücken
![3](https://github.com/anasm20/Fingerprint-Matching/assets/112882511/abe07196-12a1-4e79-b383-ad6722efd0dd)


### Schritt 1: Referenzbild Ladung
Ein Referenzbild ('input_img') wird geladen und in Graustufen konvertiert.

### Schritt 2: Feature-Erkennung
Die SIFT (Scale-Invariant Feature Transform)-Methode wird verwendet, um Schlüsselpunkte in den Bildern zu erkennen.

### Schritt 3: Matcher-Anwendung
Ein Flann-basierter Matcher wird verwendet, um Übereinstimmungen zwischen den Schlüsselpunkten im Referenzbild und anderen Bildern zu identifizieren.

### Schritt 4: Visualisierung von Übereinstimmungen
Übereinstimmungen zwischen dem Referenzbild und den anderen Bildern werden visualisiert, und es wird angezeigt, ob Übereinstimmungen gefunden wurden.

## Version 2 verfügt über viele vergleich spezifische Funktionen
![4](https://github.com/anasm20/Fingerprint-Matching/assets/112882511/194ab95a-df49-49aa-9d8c-79717f1ddf49)



## Zusammenfassung
Dieses Fingerprint-Matching-Programm wurde durch die Zusammenarbeit von Benutzer "aasthac67" und Benutzer "anasm20" entwickelt und in öffentlichen GitHub-Repositories gehostet. Die Code-Segmente wurden entwickelt, um verschiedene Schritte zur Verarbeitung von Fingerabdrücken durchzuführen. 

Der erste Code entfernt den Hintergrund, der zweite betont Merkmale und der dritte vergleicht Fingerabdrücke mit Hilfe von Schlüssel Punkten und Übereinstimmungen. Das Programm kann dazu verwendet werden, Fingerabdrücke zu vergleichen und Übereinstimmungen zu identifizieren, was in verschiedenen Sicherheits- und Identifikationsszenarien nützlich sein kann.


