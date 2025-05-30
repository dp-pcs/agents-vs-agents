#!/bin/bash

echo "🚀 Running all benchmark runners..."

# LangChain
python runners/runner_langchain_openai_claude.py
python runners/runner_langchain_claude_openai.py

# LangGraph
python runners/runner_langgraph_openai_claude.py
python runners/runner_langgraph_claude_openai.py

# CrewAI
python runners/runner_crewai_openai_claude.py

echo "❌ Skipping runner_crewai_claude_openai.py (unsupported)"

# AutoGen
python runners/runner_autogen_openai_claude.py

echo "❌ Skipping runner_autogen_claude_openai.py (unsupported)"

# Generate final summary
echo "📊 Generating benchmark summary..."
python results/benchmark_summary.py

echo "✅ All benchmarks complete."