import fractions
import random
import re
import matplotlib.pyplot as plt
import os 
class FractionExpressionGenerator:
    def __init__(self,save_path=None):
        self.save_path = save_path
        if save_path is None:
            self.save_path = 'Exercise/'
        os.makedirs(self.save_path,exist_ok=True)
        self.ops = ['+', '-', '×', '÷']

    def apply_operator(self, operators, values):
        right = values.pop()
        left = values.pop()
        op = operators.pop()
        
        if op == '+':
            values.append(left + right)
        elif op == '-':
            values.append(left - right)
        elif op == '×':
            values.append(left * right)
        elif op == '÷':
            values.append(left / right)
        return values

    def get_precedence(self, op):
        if op in ('+', '-'):
            return 1
        if op in ('×', '÷'):
            return 2
        return 0

    def generate_fraction_expression_list(self, num_fractions):
        expression_list = []
        for i in range(num_fractions):
            f = fractions.Fraction(random.randint(-10, 10), random.randint(1, 15))
            while f == 0:
                f = fractions.Fraction(random.randint(-10, 10), random.randint(1, 15))
            
            expression_list.append(f)
            if i != num_fractions - 1:
                op = random.choice(self.ops)
                expression_list.append(op)
        
        num_add_sub = expression_list.count('+') + expression_list.count('-')
        k = min(random.randint(0, num_fractions - 2), num_add_sub)
        kuohao_index = []
        for i in range(len(expression_list)):
            if k > 0 and expression_list[i] in ['+', '-'] and [i, ')'] not in kuohao_index:
                kuohao_index.append([i - 1, '('])
                kuohao_index.append([i + 2, ')'])
                k -= 1
                if k == 0:
                    break
                    
        for i in range(len(kuohao_index)):
            expression_list.insert(kuohao_index[i][0] + i, kuohao_index[i][1])
            
        return expression_list

    def evaluate_expression(self, num_fractions):
        while True:
            try:
                expression_list = self.generate_fraction_expression_list(num_fractions)
                operators = []
                values = []
                
                for token in expression_list:
                    if isinstance(token, fractions.Fraction):
                        values.append(token)
                    elif token == '(':
                        operators.append(token)
                    elif token == ')':
                        while operators and operators[-1] != '(':
                            values = self.apply_operator(operators, values)
                        operators.pop()  # 移除左括号
                    else:
                        while (operators and operators[-1] != '(' and
                               self.get_precedence(operators[-1]) >= self.get_precedence(token)):
                            values = self.apply_operator(operators, values)
                        operators.append(token)
                
                while operators:
                    values = self.apply_operator(operators, values)
                
                ret_expression = ''
                for i in expression_list:
                    if isinstance(i, fractions.Fraction) and i < 0:
                        i_ = i
                        if i.denominator in [2, 4, 8, 5, 10, 20] and random.choice([0, 1]) == 1:
                            i_ = float(i)
                        ret_expression += '(' + str(i_) + ')'
                    elif isinstance(i, fractions.Fraction) and i.denominator in [2, 4, 8, 5, 10, 20] and random.choice([0, 1]) == 1:
                        i_ = float(i)
                        ret_expression += str(i_)
                    else:
                        ret_expression += str(i)
                return str(ret_expression), values[0]
            except ZeroDivisionError:
                continue

    def convert_to_latex(self, expression):
        return re.sub(r'(-?\d+)/(\d+)', r'\\frac{\1}{\2}', expression)

    def generate_practice_and_answers(self, num_of_problems,num_of_operands, filename_prefix,write_to_file=False):
        expression_list = []
        answer_list = []
        for i in range(num_of_problems):
            expression, result = self.evaluate_expression(num_of_operands)
            expression = f"t{i + 1}:{expression}="
            result = f"t{i + 1}:{str(result)}"
            expression_list.append(expression)
            answer_list.append(result)

        if write_to_file:
            # Write to files
            with open(os.path.join(self.save_path,f'{filename_prefix}_练习题.txt'), 'w') as f1:
                for expr in expression_list:
                    f1.write(expr + '\n')

            with open(os.path.join(self.save_path,f'{filename_prefix}_答案.txt'), 'w') as f2:
                for ans in answer_list:
                    f2.write(ans + '\n')

        # Generate and save practice questions plot
        plt.figure(figsize=(12, 10))
        plt.title(f'Exercise {filename_prefix}', loc='left', fontsize=20)
        for i, expr in enumerate(expression_list):
            expression = self.convert_to_latex(expr)
            col = 0 if i / num_of_problems < 0.5 else 0.5
            plt.text(col, 1 - i % (num_of_problems // 2) / num_of_problems, f'${expression}$', fontsize=20, ha='left', va='top')
        plt.xlim(0, 1)
        plt.ylim(0.5, 1)
        plt.axis('off')
        plt.savefig(os.path.join(self.save_path,f'{filename_prefix}练习题.png'))

        # Generate and save answers plot
        plt.figure(figsize=(10, 10))
        plt.title(f'Answer {filename_prefix}', loc='left', fontsize=20)
        for i, ans in enumerate(answer_list):
            answer = self.convert_to_latex(ans)
            col = 0 if i / num_of_problems < 0.5 else 0.5
            plt.text(col, 1 - i % (num_of_problems // 2) / num_of_problems, f'${answer}$', fontsize=20, ha='left', va='top')
        plt.xlim(0, 1)
        plt.ylim(0.5, 1)
        plt.axis('off')
        plt.savefig(os.path.join(self.save_path,f'{filename_prefix}答案.png'))

# Example usage:
generator = FractionExpressionGenerator()
generator.generate_practice_and_answers(num_of_problems=20,num_of_operands=2,filename_prefix='21')