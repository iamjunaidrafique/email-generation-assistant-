# Email Generation Assistant

## Overview
This project is an AI-powered Email Generation Assistant that creates professional emails based on:
- Intent
- Key Facts
- Tone

## Objective
Automate high-quality email drafting using advanced prompt engineering techniques.

## Prompting Technique
We used Role-Based Prompting + Few-Shot Examples to guide the LLM in generating structured and professional emails.

## Project Structure
- prompt_template.txt → Prompt used for generation
- evaluation.json → Test scenarios
- evaluation.csv → Evaluation results
- metrics.json → Custom metric definitions and averages
- report.pdf → Final analysis report

## Custom Metrics
1. Fact Recall Score – Measures inclusion of key facts
2. Tone Accuracy Score – Measures tone alignment
3. Clarity & Conciseness Score – Measures readability and brevity

## How to Run
1. Load scenarios from evaluation.json
2. Apply prompt_template.txt
3. Generate outputs using LLM
4. Evaluate using custom metrics script

## Results
See metrics.json and evaluation.csv for detailed results.
