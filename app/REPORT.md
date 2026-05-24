# Zastosowanie algorytmu A* do znajdowania ścieżki w labiryncie

Kasjan Kozłowski
---
# 1. Opis problemu
Celem projektu było zaimplementowanie algorytmu A* oraz wykorzystanie go do
znajdowania najkrótszej ścieżki w labiryncie reprezentowanym jako siatka 2D.
Problem znajdowania ścieżki występuje między innymi w:
- grach komputerowych
- robotyce
- systemach GPS
- sztucznej inteligencji

Labirynt został przedstawiony jako dwuwymiarowa tablica znaków.
---
# 2. Opis algorytmu
Algorytm A* jest algorytmem przeszukiwania grafu wykorzystującym funkcję
oceny:
f(n) = g(n) + h(n)
Gdzie:
- g(n) oznacza koszt dojścia od startu do aktualnego węzła
- h(n) oznacza heurystyczne oszacowanie kosztu dojścia do celu
Algorytm wybiera w każdym kroku węzeł o najniższym koszcie f(n).
# 3. Heurystyki
W projekcie wykorzystano trzy heurystyki:
## Manhattan
Dobrze sprawdza się przy ruchu góra/dół/lewo/prawo.
## Euklidesowa
Oblicza rzeczywistą odległość geometryczną.
## Zerowa heurystyka
Powoduje działanie podobne do algorytmu Dijkstry.
---
# 4. Dane testowe
Przygotowano trzy przykładowe labirynty o różnym poziomie trudności.
Każdy labirynt zawiera:
- punkt startowy S
- punkt końcowy E
- ściany #
- wolne pola .
---
# 5. Eksperyment
Dla każdej heurystyki wykonano pomiary:
- czasu działania
- liczby odwiedzonych pól
- długości ścieżki
---
# 6. Wyniki
| Heurystyka | Czas | Odwiedzone pola | Długość ścieżki |
|---|---|---|---|
| Manhattan | bardzo krótki | najmniej | poprawna |
| Euklidesowa | krótki | średnio | poprawna |
| Zerowa | najdłuższy | najwięcej | poprawna |
# 7. Wnioski
Algorytm A* skutecznie znajduje najkrótszą ścieżkę w labiryncie.
Najlepsze wyniki uzyskano dla heurystyki Manhattan, ponieważ ruch był możliwy
wyłącznie w czterech kierunkach.
Zastosowanie heurystyki znacząco zmniejsza liczbę odwiedzanych węzłów oraz
przyspiesza działanie algorytmu.
Brak heurystyki powoduje zwiększenie czasu działania i liczby sprawdzanych
pól.
