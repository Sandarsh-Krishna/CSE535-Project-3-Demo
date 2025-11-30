# CSE535-Project-3-Demo

Fragmentation-Aware Android API Adaptation – Demo

  This repo contains a very simple demo of the idea from our project on handling Android API fragmentation using a knowledge graph, an LLM, and a checker agent.

  The goal of this demo is to show the working of the pipeline and our paper at the most basic level.

What this demo shows:

  A small fragmentation knowledge graph that stores information about risky Android APIs and safer alternatives , this is a very tiny version of the dataset we can obtain by researching prior research papers on this topic.

  A checker agent step that compares the manually patched file and compares it with the knowledge graph to determine whether the file is risky or not.

  Screenshots of working of the checker agent with output.

Important note:

  We did not train a new LLM for this demo .

  Instead, this repo uses buggy and patched files that are uploaded and edited manually instead of being automated by a LLM.

  The “LLM output” is represented in a simple, scripted way.

  The focus is on showing the flow (inputs → patch → check → result).

Even with this minimal setup, the demo captures the main idea of the paper at a basic level:

  using structured fragmentation knowledge plus an LLM-style agent and a checker to make Android code more robust across devices.

How to use this repo

  Browse the code files to see how the simple pipeline is implemented.

  Open the screenshots/ folder to see example runs and results.

  Use this repo as a conceptual companion to the report / presentation, not as a full research artifact.
