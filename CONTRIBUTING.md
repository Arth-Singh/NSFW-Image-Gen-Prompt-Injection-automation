# Contributing to ARTH AI Red Team Terminal

Thank you for your interest in contributing to this defensive security research tool!

## Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/automator-redteam.git
   cd automator-redteam
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your actual API keys
   ```

## Testing

Run the test suite:
```bash
python arth.py --mode auto --iterations 5 --theme "test suite"
```

## Code Style

- Follow PEP 8 guidelines
- Use meaningful variable names
- Add docstrings for all functions
- Maintain defensive programming practices

## Security Guidelines

This tool is for **defensive security research only**:
- All testing should be for improving AI safety
- Follow responsible disclosure practices
- Do not use for malicious purposes
- Respect rate limits and API terms of service

## Pull Request Process

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Make your changes
4. Test thoroughly
5. Submit a pull request with clear description

## Reporting Issues

When reporting issues:
- Use the issue template
- Include reproduction steps
- Provide relevant log files (sanitized)
- Specify environment details