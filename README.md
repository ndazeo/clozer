# clozer

## Prequisites

* python3

## Instalation

`pip3 install clozer`

## Example

Python file (`sumquiz.py`):
```
import random

from clozer import Quiz, QuestionVar


class SumQuiz(Quiz):
    file = 'template.html'
    
    def __init__(self):
        super().__init__()
        self._name = 'SumQuiz' 

    @QuestionVar
    def A(self):
        return random.randint(1,10)

    @QuestionVar
    def B(self):
        return random.randint(1,10)

    @QuestionVar
    def C(self):
        return self.A + self.B


if __name__ == "__main__":
    quiz = SumQuiz()
    quiz.store()
```

Template (`template.html`):
```
<p>Solve:</p>
<p>{A}+{B}={{:NUMERIC:={C}}}</p>
```

Run:
`python3 sumquiz.py`