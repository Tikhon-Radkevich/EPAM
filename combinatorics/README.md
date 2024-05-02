### The Order of Wisdom

The university lecture scheduler has three key professors — Alejandro, Bernardo, and Vicente — planned
to give a series of guest lectures which are expected to significantly boost the university's academic reputation.
They hypothesize that the impact of these lectures on students and faculty will be maximized if the professors speak
in a particular sequence: Alejandro first, followed by Bernardo, and then Vicente.
But there are also five other speakers set to present. However, the organizers have not yet decided the exact order for
all the presentations.What are the probabilities that the three key professors will present in the optimal sequence?
It should be noted that it does not matter if other speakers present before, in between, or after the three professors;
the critical factor for achieving the desired impact is that the sequence of Alejandro,
Bernardo, and Vicente's lectures is preserved.

### Математическое Решение

Пускай у нас `K = 3` профессоров и `S = 5` остальных спикеров. Всего `(K + S) = 8` выступающих.<br>
"Безымянных" спикеров буду считать различными (условно пронумерую их от 0 до N-1).

Вероятность того, что профессора выступят в правильном порядке рассчитаю как отношение числа `1) благоприятных исходов` к `2) общему числу исходов`.

1) Число благоприятных исходов буду считать следующим образом:
    - Сначала рассположу `S` спикеров и посчитаю их всевозможные перестановки: `S!`
    - Затем "размещу" `K` профессоров между/после/перед спикерами: `S+1` мест
    - Размещаем мы `K` профессоров на `S+1` мест: `A = C * P`, однако в нашем случае у нас задана расстановка профессоров (Alejandro -> Bernardo -> Vicente), значит перестановки `P`ненужны. Более того - профессоров можно помещать в одно и тоже место, так чтобы между ними не было других спикеров. Итого нам нужны сочетания с повторениями: `(S+1)C(K)`, и перейдём к просто сочетаниям: `(S+K)C(K)`
    - В результате получаем: `S! * (S+K)C(K)` = `S!*(S+K)!/(S!*K!)` = `(S+K)!/K!` - число благоприятных исходов.
2) Общее число исходов равно `(S + K)!`

Таким образом, вероятность того, что профессора выступят в правильном порядке равна: `(S+K)!/K! / (S+K)!` = `1/K!`<br>
Видно, что вероятность не зависит от числа остальных спикеров. И в нашем случае она равна `1/3! = 1/6 = 0.1666%`

Ответ: `1/6`
