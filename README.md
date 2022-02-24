# Zipbora AI Models 

[![badge](https://img.shields.io/badge/Version-1.0.0-brightgreen)]()

## 🗂 Model Cards 

Card Types 
* `C`  : Classification Model
* `G`  : Generator Model

|Models | input | output| Card |
|:-:|:-:|:-:|:-:|
|Spam Post Classification Model by string| `String` | `(Boolean, Probability)`| `C1`|
|Hashtag Generator | `String`  | `LIST<String>`|  `G1` |  

## Example

```python
from zipbora_ai_models import get_model_by_tag

model = get_model_by_tag('C1')

# 예시 result = 0, 0.01  
result = model("이 집을 보라.. 얼마나 좋은가")


model = get_model_by_tag('G1')

# 예시 result = ['색깔', '전망', '풍경'] 
result = model("이 집을 보라.. 얼마나 좋은가")

```