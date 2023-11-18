# operacje_na_bazie_uzytkownikow

```
pip install flask pytest
```

| Zadanie | Zrobione |
| ------- | -------- |
| GET     | tak      |
| GET id  | tak      |
| POST    | tak      |
| PATCH   | tak      |
| PUT     | tak      |
| DELETE  | tak      |

Proszę napisać aplikację serwerową spełniającą następujące warunki:
1. Korzysta z protokołu HTTP w wersji 1.1

2. Obsługuje następujące końcówki (endpointy):
- GET /users -> zwracającą odpowiedź o kodzie 200 i listę użytkowników zakodowaną w JSON w postaci: [{"id": 1, "name": "Wojciech", "lastname": "Oczkowski}, ...];
- GET /users/\<id\> -> Zwracającą odpowiedź o kodzie 200 i pojedynczego użytkownika o podanym id;
- POST /users -> przyjmującą request o ciele w postaci {"name": "Wojciech", "lastname": "Oczkowski} i zapisujący użytkownika w tymczasowej persystencji, nadając mu pierwszy wolny numer id i zwracający kod odpowiedzi 201;
- PATCH /users/\<id\> -> przyjmującej request o ciele w postaci {"name": "Wojciech"} lub {"lastname": "Oczkowski"}, modyfikujący obiekt o podanym id i zwracającego w takim wypadku kod 204. Jeżeli id jest nieobecne lub ciało żądania ma inną postać zwracamy kod odpowiedzi 400;
- PUT /users/\<id\> -> przyjmującej request o ciele w postaci {"name": "Wojciech", "lastname": "Oczkowski} i zapisującej lub modyfikującej użytkownka o podanym id - zwracamy kod odpowiedzi 204;
- DELETE /users/\<id\> -> usuwającej z tymczasowej persystencji użytkownika o podanym id, jeżeli istnieje - zwracamy wówczas kod odpowiedzi 204. Jeżeli nie istnieje - zwracamy kod odpowiedzi 400

3. Końcówki są przetestowane jednostkowo i integracyjnie.

4. Cała praca oddana jest w postaci repozytorium (w idealnym wypadku jako link do zdalnego repozytorium), z historią commitów obrazującą przebieg pracy.

5. Stosujemy się do konwencji formatowania kodu i nazewnictwa w Pythonie.
