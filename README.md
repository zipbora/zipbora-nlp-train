# Zipbora AI Models 

[![badge](https://img.shields.io/badge/Version-1.0.0-brightgreen)]()

## Example

```python
from zipbora_ai_models import get_model_by_tag

model = get_model_by_tag('KBC1')

# 예시 result = 0, 0.01  
result = model.predict("이 집을 보라.. 얼마나 좋은가")


model = get_model_by_tag('KBG1')

# 예시 result = ['색깔', '전망', '풍경'] 
result = model.predict("이 집을 보라.. 얼마나 좋은가")

```

## 🗂 Model Cards 

Card Types 
`<language><model><type><enum>`

* 🗺️ Domain
  * `K`  : Korean Sentence
  * `E`  : English Setence
  * `I` : Image
  * `T` : Table Dataset

* 🤖 Model
  * `B` : Bert 
  * `R` : RNN
  * `F` : Fully Connected Layer

* 🐧 Type
  * `C`  : Classification Model
  * `G`  : Generator Model


|Models | input | output| Card |
|:-:|:-:|:-:|:-:|
|Spam Post Classification Model by string| `String` | `(Boolean, Probability)`| `KBC1`|
|Hashtag Generator | `String`  | `LIST<String>`|  `KBG1` |  

