# JailbreakTracer: Explainable Detection of Jailbreaking Prompts in LLMs Using Synthetic Data Generation

***Accepted*** in `IEEE Access Journal`

## Methodology
![Methodology](assets/jailbreaktracer.png)

Overview of the **JailbreakTracer** Methodology. The methodology comprises five major components: (1) data collection from jailbreak attack research papers and prompt labeling; (2) synthetic toxic prompt generation using a fine-tuned GPT model, followed by attack validation via LLMs; (3) data preprocessing; (4) training of a transformer-based classifier with explainability provided via LIME; and (5) performance evaluation.

## Dataset
Download our dataset from [Kaggle](https://www.kaggle.com/datasets/faiyazabdullah/jailbreaktracer-corpus)

## Codes
Codes for toxic prompt classification can be found in [G1](G1/notebooks) directory.\
Codes for forbidden question reasoning can be found in [G2](G2/notebooks) directory.

## Model Weights
Download the [Fine-Tuned GPT Model](https://drive.google.com/file/d/1k2F2TVdPMG4df8BA1e2lekYHugp3zhR3/view?usp=sharing) to generate synthetic toxic/jailbreaking prompts.\
Download the [JailBreakBERT Model](https://drive.google.com/uc?export=download&id=1cwQfIAN7_3Yt_jcYjlB3n4Tot2JTTRC2) and the [JailBreakRoBERTa Model](https://drive.google.com/file/d/1Y2H_ZbAv6Vs7Z0eaVDhMztujZOZz-sIS/view?usp=sharing) to classify the prompt whether it is regular or toxic.\
Download the [Forbidden Question Classifier](https://drive.google.com/file/d/1TmsP_Qo67LdDGzrqoh7guxtBwuzaqw9m/view?usp=sharing) to understand the reason why certain questions are flagged as inappropriate, sensitive, or restricted based on predefined rules and ethical considerations.

## Result Comparison with Existing Works

| **Method** | **Accuracy** | **ASR** |
|------------|--------------|---------|
| AutoDefense [Zeng et al., 2024](https://arxiv.org/abs/2403.04783) | 92.91% | 55.74% |
| Llama Guard [Inan et al., 2023](https://arxiv.org/abs/2312.06674) | 94.5% | 37.32% |
| LLM Self Defense [Phute et al., 2023](https://arxiv.org/abs/2308.07308) | 77% | - |
| SMOOTHLLM [Robey et al., 2023](https://arxiv.org/abs/2310.03684) | - | 92% |
| Prompt Adversarial Tuning [Mo et al., 2024](https://arxiv.org/abs/2402.06255) | - | 0.8% |
| Heuristic-based [Chu et al., 2024](https://arxiv.org/abs/2402.05668) | - | 85.0% |
| AutoDAN [Liu et al., 2023](https://arxiv.org/abs/2310.04451) | - | 70% |
| Generation Exploitation [Chu et al., 2024](https://arxiv.org/abs/2402.05668) | - | 68% |
| DrAttack [Li et al., 2024](https://arxiv.org/abs/2402.16914) | - | 62% |
| **JailbreakTracer (Ours)** | **97.25%** | **91.9%** |

## Cite
<pre>
@ARTICLE{11036671,
  author={Sayeedi, Md. Faiyaz Abdullah and Hossain, Maaz Bin and Hassan, Md. Kamrul and Afrin, Sabrina and Sabit, Molla Md and Hossain, Md. Shohrab},
  journal={IEEE Access}, 
  title={JailbreakTracer: Explainable Detection of Jailbreaking Prompts in LLMs Using Synthetic Data Generation}, 
  year={2025},
  volume={},
  number={},
  pages={1-1},
  keywords={Ethics;Cognition;Synthetic data;Natural language processing;Artificial intelligence;Adaptation models;Security;Robustness;Prevention and mitigation;Passwords;Natural Language Processing;Large Language Models;Jailbreaking;Text Classification;Synthetic Data;Generative AI;Explainable AI},
  doi={10.1109/ACCESS.2025.3579996}}
</pre>

## Contact
For any queries, please contact us at msayeedi212049@bscse.uiu.ac.bd
