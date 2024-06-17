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

![s](https://github.com/ananda17gb/IndonesianSentenceParser_G1_FP_TBA_IF-46-INT/assets/79387612/0eb236ad-59cd-4a97-8117-aed44278bae5)

### Predicate:

![p](https://github.com/ananda17gb/IndonesianSentenceParser_G1_FP_TBA_IF-46-INT/assets/79387612/e02388ff-92d2-4b0e-bb48-52893611aabb)

### Object:

![o](https://github.com/ananda17gb/IndonesianSentenceParser_G1_FP_TBA_IF-46-INT/assets/79387612/76916319-426c-4cdb-8f86-97ac4aa264b0)

### Adverb:

![k](https://github.com/ananda17gb/IndonesianSentenceParser_G1_FP_TBA_IF-46-INT/assets/79387612/77922660-b829-4bd4-8415-8023d703e856)

### Full FA with word as the terminal symbol:

![spok_word](https://github.com/ananda17gb/IndonesianSentenceParser_G1_FP_TBA_IF-46-INT/assets/79387612/892beea2-2f8d-4b64-bd13-b8316bb1d0f7)

### Full FA with character as the terminal symbol:

![spok_char](https://github.com/ananda17gb/IndonesianSentenceParser_G1_FP_TBA_IF-46-INT/assets/79387612/f6e76046-2c64-4071-9806-b98b120ed473)

## CFG

```
<sentence> ::= <subject> | <predicate_phrases>

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
<<<<<<< HEAD

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
![image](https://github.com/ananda17gb/IndonesianSentenceParser_G1_FP_TBA_IF-46-INT/assets/79387612/ba5438dc-f3dd-41d4-a97a-a5ec6881d3a9)

Invalid example:
![image](https://github.com/ananda17gb/IndonesianSentenceParser_G1_FP_TBA_IF-46-INT/assets/79387612/1273bf82-1486-4a45-910a-61c7e5ddc243)

## Reference
[Presentasi Tubes TBA | Kelompok KAK | TelkomUniversity | IF-45-11](https://www.youtube.com/watch?v=KoPYcwvR-vI&t=147s)
