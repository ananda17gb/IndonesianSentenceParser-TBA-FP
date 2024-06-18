## Member

### IF-46-INT Group 1:

- Ruly Bija (1301224196)
- Ananda Arti Widigdo (1301224386)
- Devin Prawira Arissaputra (1301224478)

## Sentence structures

- S – P – O – K (Subject – Predicate – Object – Adverb)
- S – P – K
- S – P – O
- S – P

## Words for each categories

- S: {"Ana", "Ani", "Anu", "Ane", "Ano"}
- P: {"membeli", "membayar", "membuang", "membakar", "membaca"}
- O: {"sampah", "samsir", "sampan", "samsak", "sampul"}
- K: {"di pasar", "di TPA", "di warteg", "di warung", "di plaza"}

## Finite Automata

### Subject:

![s](https://github.com/ananda17gb/IndonesianSentenceParser-TBA-FP/assets/79387612/22656dcb-8e76-410e-a4c3-fab1d94e5f8d)

### Predicate:

![p](https://github.com/ananda17gb/IndonesianSentenceParser-TBA-FP/assets/79387612/2d2ea7de-54bb-4137-bb82-db3595201f2d)

### Object:

![o](https://github.com/ananda17gb/IndonesianSentenceParser-TBA-FP/assets/79387612/1dc1c29d-6e15-4df9-bd0b-a706b69447ff)

### Adverb:

![k](https://github.com/ananda17gb/IndonesianSentenceParser-TBA-FP/assets/79387612/8ed73901-1c85-4881-b7c3-1beab725a3e0)

### Full FA with word as the terminal symbol:

![spok_word](https://github.com/ananda17gb/IndonesianSentenceParser-TBA-FP/assets/79387612/ff59785b-c8e5-492d-9e2c-de5d92e5fea9)

### Full FA with character as the terminal symbol:

![spok_char](https://github.com/ananda17gb/IndonesianSentenceParser-TBA-FP/assets/79387612/3498bf2c-d022-4efa-af08-43bc5e890d0c)

## CFG

```
<sentence> ::= <subject> <predicate_phrases>

<subject> ::= "Ana" | "Ani" | "Anu" | "Ane" | "Ano"

<predicate_phrases> ::= <predicate>
                      | <predicate> <object>
                      | <predicate> <adverb>
                      | <predicate> <object> <adverb>

<predicate> ::= "membeli" | "membayar" | "membuang" | "membakar" | "membaca"

<object> ::= "sampah" | "samsir" | "sampan" | "samsak" | "sampul"

<adverb> ::= "di pasar" | "di TPA" | "di warteg" | "di warung" | "di plaza"
```

## Parse Table

| Non-terminal | Ana    | Ani    | Anu    | Ane    | Ano    | membeli                                | membayar                               | membuang                               | membakar                               | membaca                                | sampah   | samsir   | sampan   | samsak   | sampul   | di pasar   | di TPA   | di warteg   | di warung   | di plaza   | EOS   |
| ------------ | ------ | ------ | ------ | ------ | ------ | -------------------------------------- | -------------------------------------- | -------------------------------------- | -------------------------------------- | -------------------------------------- | -------- | -------- | -------- | -------- | -------- | ---------- | -------- | ----------- | ----------- | ---------- | ----- |
| `<S>`        | `<SU>` | `<SU>` | `<SU>` | `<SU>` | `<SU>` | `<PP>`                                 | `<PP>`                                 | `<PP>`                                 | `<PP>`                                 | `<PP>`                                 |          |          |          |          |          |            |          |             |             |            | error |
| `<SU>`       | "Ana"  | "Ani"  | "Anu"  | "Ane"  | "Ano"  |                                        |                                        |                                        |                                        |                                        |          |          |          |          |          |            |          |             |             |            | error |
| `<PP>`       |        |        |        |        |        | `<P>`, `<P><O>`, `<P><K>`, `<P><O><K>` | `<P>`, `<P><O>`, `<P><K>`, `<P><O><K>` | `<P>`, `<P><O>`, `<P><K>`, `<P><O><K>` | `<P>`, `<P><O>`, `<P><K>`, `<P><O><K>` | `<P>`, `<P><O>`, `<P><K>`, `<P><O><K>` |          |          |          |          |          |            |          |             |             |            | error |
| `<P>`        |        |        |        |        |        | "membeli"                              | "membayar"                             | "membuang"                             | "membakar"                             | "membaca"                              |          |          |          |          |          |            |          |             |             |            | error |
| `<O>`        |        |        |        |        |        |                                        |                                        |                                        |                                        |                                        | "sampah" | "samsir" | "sampan" | "samsak" | "sampul" |            |          |             |             |            | error |
| `<K>`        |        |        |        |        |        |                                        |                                        |                                        |                                        |                                        |          |          |          |          |          | "di pasar" | "di TPA" | "di warteg" | "di warung" | "di plaza" | error |

## Output

Valid example:
![image](https://github.com/ananda17gb/IndonesianSentenceParser-TBA-FP/assets/79387612/f59e6a73-03ae-4962-aa21-772fbec912f2)

Invalid example:
![image](https://github.com/ananda17gb/IndonesianSentenceParser-TBA-FP/assets/79387612/061c082a-c393-42f5-bbd8-9b72be1fc835)
