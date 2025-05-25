# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python-based image generation project that uses the Replicate API. The project structure is minimal with the main functionality located in `replicate/generate.py`.

## Development Commands

Since this project doesn't have formal dependency management or build tools configured yet, development is straightforward:

- Run the image generation script: `python replicate/generate.py`
- Install dependencies as needed: `pip install <package-name>`

## Architecture

- `replicate/` - Contains the main image generation functionality using Replicate's API
- `replicate/generate.py` - Main script for generating images (currently empty)

## Notes

This project is in early development with minimal tooling. Future development may require adding:
- Requirements management (requirements.txt or pyproject.toml)
- Testing framework setup
- Environment configuration for API keys