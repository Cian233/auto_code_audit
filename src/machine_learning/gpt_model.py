# src/machine_learning/gpt_model.py

from transformers import AutoModelForCausalLM, AutoTokenizer
from typing import List, Dict

from .model_interface import ModelInterface

class GPTModel(ModelInterface):
    """
    使用 GPT 模型实现的代码分析器。
    """

    def __init__(self):
        # 加载预训练的 GPT 模型和分词器
        self.tokenizer = AutoTokenizer.from_pretrained("gpt2")
        # 请在此处加载经过微调的模型用于漏洞检测
        self.model = AutoModelForCausalLM.from_pretrained("path/to/your/fine-tuned-model")
        self.model.eval()

    def analyze_code(self, code_snippet: str, language: str) -> List[Dict]:
        """
        使用 GPT 分析代码片段，检测潜在的漏洞。

        Args:
            code_snippet (str): 要分析的代码片段。
            language (str): 代码的编程语言。

        Returns:
            List[Dict]: 检测到的漏洞列表。
        """
        # 构建提示词，让模型分析代码
        prompt = f"分析以下{language}代码，找出其中的安全漏洞：\n\n{code_snippet}\n\n漏洞列表："

        inputs = self.tokenizer.encode(prompt, return_tensors="pt", truncation=True, max_length=1024)

        output_sequences = self.model.generate(
            input_ids=inputs,
            max_length=inputs.shape[1] + 100,
            temperature=0.7,
            top_k=50,
            top_p=0.95,
            do_sample=True,
            num_return_sequences=1,
        )

        generated_text = self.tokenizer.decode(output_sequences[0], skip_special_tokens=True)

        # 从生成的文本中提取漏洞信息
        vulnerabilities = self._extract_vulnerabilities(generated_text, prompt)

        return vulnerabilities

    def _extract_vulnerabilities(self, generated_text: str, prompt: str) -> List[Dict]:
        """
        从生成的文本中提取漏洞信息。

        Args:
            generated_text (str): 模型生成的文本。
            prompt (str): 输入的提示词，用于截取新生成的内容。

        Returns:
            List[Dict]: 检测到的漏洞列表。
        """
        # 截取模型新生成的内容
        new_content = generated_text[len(prompt):].strip()

        result = []

        if new_content:
            # 简单示例：按行解析漏洞列表
            lines = new_content.split('\n')
            for line in lines:
                if line.strip():
                    issue = {
                        'vulnerability': line.strip(),
                        'confidence': 0.7,  # 示例值
                        'details': 'GPT 模型检测到的潜在漏洞。',
                        'location': 'N/A'
                    }
                    result.append(issue)
        else:
            # 未检测到漏洞
            pass

        return result
