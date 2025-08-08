# Automated Novel Prompt Injection automation for NSFW image gen.

An automated safety filter testing system for defensive security research and AI safety evaluation.

## 🎯 Purpose

This tool is designed for **defensive security research** to test AI safety filters and improve content moderation systems. It helps identify potential vulnerabilities in AI systems to strengthen their defenses.

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- API keys for OpenAI and KIMI

### Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/automator-redteam.git
cd automator-redteam

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your API keys
```

### Usage
```bash
# Interactive mode (beautiful menu)
python3 arth.py

# Automated testing
python3 arth.py --mode auto --iterations 20 --theme "safety testing"

# Generate reports
python3 arth.py --mode report
```

## 📁 Directory Structure

```
automator-redteam/
├── arth.py                 # Main red team terminal
├── requirements.txt        # Python dependencies
├── .gitignore             # Git ignore rules
├── README.md              # This file
├── images/                # Generated test images
├── logs/                  # JSON test logs
└── reports/               # Analytics reports
```

## 🔧 Configuration

Create a `.env` file with your API keys:
```
OPENAI_API_KEY=your_openai_key_here
KIMI_API_KEY=your_kimi_key_here
```

## 🛡️ Features

- **Multi-API Integration**: Gemini API and OpenAI GPT Image 1
- **Safety Testing**: Automated content moderation testing
- **Comprehensive Logging**: JSON format for security analysis
- **Visual Reports**: Generated charts and analytics
- **Interactive Interface**: Terminal-based menu system

## 📊 Output

All test results are saved in:
- `logs/` - JSON logs with test details
- `images/` - Generated test images
- `reports/` - Analytics and summaries

## 🔒 Security Considerations

This tool is intended for:
- Security researchers
- AI safety teams
- Defensive testing purposes
- Academic research

**Important**: Always follow responsible disclosure practices when identifying vulnerabilities.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Submit a pull request with clear description
4. Ensure all tests pass

## 📄 License

This project is released for educational and defensive security research purposes.
