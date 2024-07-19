# FractionExpressionGenerator: 生成分数表达式练习题和答案
FractionExpressionGenerator 是一个用于生成分数表达式练习题和答案的Python脚本。它能够创建包含分数的数学表达式，支持基本的算术运算（加、减、乘、除），并且可以生成对应的答案。题目的面向对象主要为初一学生。此外，脚本还提供了将表达式转换为LaTeX格式以及将练习题和答案保存为文本文件和图片文件的功能。
## 功能特性
- 随机生成包含分数的算术表达式。
- 支持添加括号以改变运算顺序。
- 表达式可以为分数或小数。
- 将生成的表达式和答案保存为文本文件。
- 将表达式和答案转换为LaTeX格式并保存为图片文件。
## 安装
确保你的环境中安装了Python和以下依赖库：
- matplotlib：用于生成图片文件，可通过`pip install matplotlib`安装。
## 使用方法
### 初始化生成器
```python
generator = FractionExpressionGenerator(save_path='Exercise/')
```
`save_path`参数用于指定保存文件的位置，默认为当前目录下的`Exercise/`文件夹。
### 生成练习题和答案
```python
generator.generate_practice_and_answers(num_of_problems=20, num_of_operands=2, filename_prefix='21')
```
- `num_of_problems`：要生成的练习题数量。
- `num_of_operands`：每个表达式中操作数的数量。
- `filename_prefix`：保存文件时使用的文件名前缀。
执行上述命令后，脚本将在指定的`save_path`下生成以下文件：
- `{filename_prefix}_练习题.txt`：包含生成的练习题。
- `{filename_prefix}_答案.txt`：包含对应的答案。
- `{filename_prefix}练习题.png`：包含练习题的图片。
- `{filename_prefix}答案.png`：包含答案的图片。
## 示例
以下是如何使用FractionExpressionGenerator的示例：
```python
import os
from FractionExpressionGenerator import FractionExpressionGenerator
# 创建生成器实例
generator = FractionExpressionGenerator(save_path='Exercise/')
# 确保保存路径存在
os.makedirs(generator.save_path, exist_ok=True)
# 生成20个问题，每个问题包含2个操作数，文件名前缀为'21'
generator.generate_practice_and_answers(num_of_problems=20, num_of_operands=2, filename_prefix='21')
```
执行上述代码后，你将在`Exercise/`文件夹中找到生成的文件。
