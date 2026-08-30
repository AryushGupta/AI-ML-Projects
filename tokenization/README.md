# Tokenization

Tokenization is the process of breaking text into smaller pieces called **tokens**.

It is one of the first steps used when building systems such as **Large Language Models (LLMs)**.

---

## What is Tokenization?

Computers do not directly understand text the way humans do.

For example, we can easily read:

> I love computers.

But a language model works with numbers.

Tokenization creates a bridge between human-readable text and numbers that a model can process.

The basic process is:

```text
Text
  ↓
Tokens
  ↓
Token IDs
  ↓
Neural Network
