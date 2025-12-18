# AI Development Guide - [PROJECT_NAME]

> **Purpose**: [One-line description of what this project does]  
> **Repository**: [GitHub URL]  
> **Status**: [Planning | In Development | Beta | Production]

---

## Project Overview

[2-3 sentences describing what the project does and who it's for. This is the "elevator pitch" for the AI to understand context.]

### Key Features
- **[Feature 1]**: Brief description
- **[Feature 2]**: Brief description
- **[Feature 3]**: Brief description

---

## Tech Stack

> **Note to AI**: The tech stack below should be filled in during project planning. If empty, help the user choose appropriate technologies based on their requirements.

### Language & Runtime
| Component | Choice | Rationale |
|-----------|--------|-----------|
| **Language** | [TBD] | [Why this language?] |
| **Runtime** | [TBD] | [Version requirements] |

### Frameworks & Libraries
| Component | Choice | Purpose |
|-----------|--------|---------|
| **Web Framework** | [TBD] | |
| **Testing** | [TBD] | |
| **Database** | [TBD] | |

### Infrastructure
| Component | Details |
|-----------|---------|
| **Deployment** | [TBD] |
| **CI/CD** | [TBD] |
| **Monitoring** | [TBD] |

---

## Directory Structure

> **Note to AI**: Update this section as the project structure evolves. Keep it current.

```
[project-name]/
├── src/                    # Source code
├── tests/                  # Test files
│   ├── unit/               # Unit tests
│   └── integration/        # Integration tests
├── docs/                   # Documentation
├── .windsurf/              # Windsurf configuration
│   └── rules/              # Project-specific AI rules
├── AI_README.md            # This file
├── CONTRIBUTING.md         # Contribution guidelines
├── TESTING.md              # Testing methodology
├── SECURITY.md             # Security guidelines
├── CHANGELOG.md            # Version history
└── README.md               # User-facing documentation
```

---

## Architecture

### Data Flow
```
[Create a simple ASCII diagram showing how data flows through your system]

Example:
┌─────────┐     ┌─────────┐     ┌─────────┐
│  User   │────▶│   API   │────▶│   DB    │
│Interface│◀────│  Server │◀────│         │
└─────────┘     └─────────┘     └─────────┘
```

### Key Components

1. **[Component Name]** (`path/to/file`)
   - What it does
   - Key responsibilities
   - Important notes

2. **[Component Name]** (`path/to/file`)
   - What it does
   - Key responsibilities

---

## Development Workflow

### Getting Started

```bash
# Clone repository
git clone [repository-url]
cd [project-name]

# Install dependencies
[package manager install command]

# Run development server
[dev server command]
```

### Common Tasks

| Task | Command |
|------|---------|
| Run tests | `[test command]` |
| Build | `[build command]` |
| Lint | `[lint command]` |
| Format | `[format command]` |

---

## Code Patterns & Conventions

> **Note to AI**: Follow these patterns when generating code. Add new patterns as they emerge.

### Naming Conventions
- **Files**: `[convention, e.g., kebab-case, snake_case]`
- **Functions**: `[convention]`
- **Classes**: `[convention]`
- **Constants**: `[convention]`

### Error Handling Pattern
```
[Add language-appropriate example once tech stack is chosen]
```

### Logging Pattern
```
[Add language-appropriate example once tech stack is chosen]
```

---

## API Reference

> **Note to AI**: Document APIs as they're created. Include request/response examples.

### Endpoints

| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET | [Description] |

---

## Environment Variables

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `[VAR_NAME]` | Yes/No | `[default]` | What it configures |

---

## Key Files for AI Assistance

> **Note to AI**: Reference this table when asked to modify the project.

| File | Purpose | When to Modify |
|------|---------|----------------|
| `[file]` | [purpose] | [scenarios] |

---

## External Dependencies

| Service | Purpose | Documentation |
|---------|---------|---------------|
| [Service] | [What it's used for] | [Link] |

---

## Troubleshooting

### Common Issues

1. **[Issue Description]**
   - Cause: [Why it happens]
   - Solution: [How to fix]

---

## Version History

See [CHANGELOG.md](./CHANGELOG.md) for detailed version history.

---

## AI Development Rules

This project uses Windsurf-compatible AI behavior rules located at:

```
.windsurf/rules/project-rules.md
```

These rules are **automatically loaded** by Windsurf. Contributors should:
- Be aware the rules exist and guide AI behavior
- Update rules when establishing new patterns or requirements
- See [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines on maintaining rules

---

## Contact & Support

- **Maintainer**: [Name/Team]
- **Issues**: [Link to issue tracker]
