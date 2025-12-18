# 🔨 The Forge

Where ideas are shaped into production-ready code.

> **"Build it right, or build it twice."**  
> *Invest a little structure upfront to avoid expensive rework later.*

---

## What Is This?

The Forge is a **framework template** for AI-assisted development. Whether you're starting fresh or improving an existing codebase, it provides structure and guidelines that help AI assistants (like Windsurf's Cascade) build code that is:

- **Usable** - Works as intended, handles errors gracefully
- **Scalable** - Follows patterns that grow with your project
- **Portable** - Not locked to specific tools or platforms
- **Secure** - Follows security best practices
- **Testable** - Designed with testing in mind

### Who Is This For?

- **Beginners** who want guardrails to avoid common pitfalls
- **Experienced developers** who want AI to follow their standards
- **Teams** who want consistent AI-assisted development practices

---

## Quick Start

Choose your path:

### Path A: New Project (Starting Fresh)

Open Windsurf in an empty directory and follow these prompts:

**Step 1: Initialize with The Forge**

> "I'm starting a new project. Please set it up using The Forge framework from `/path/to/kickstarts/the-forge/templates/`. Copy all templates, create the `.windsurf/rules/` directory, and move project-rules.md into it."

**Step 2: Define your project**

> "I want to build [description of your idea]. Help me fill out AI_README.md with the project name, purpose, and recommended tech stack."

**Step 3: Start building**

> "Let's start building. What's the first component we should create?"

That's it. The framework is in place. As you build, the AI will automatically:
- Follow the rules in `.windsurf/rules/project-rules.md`
- Reference SECURITY.md when handling sensitive operations
- Suggest tests alongside new features (per TESTING.md)

---

### Path B: Existing Project (Adding Structure)

For existing projects, let AI handle the integration. Don't manually copy files — you may have existing documents that need merging, not replacing.

**Step 1: Start the integration**

Open your project in Windsurf and use this prompt:

> "I want to integrate The Forge framework into this existing project. The templates are at `/path/to/kickstarts/the-forge/templates/`. Please:
> 1. Analyze my existing project structure
> 2. Check for any existing files that would conflict (CONTRIBUTING.md, CHANGELOG.md, TESTING.md, AI_README.md, etc.)
> 3. For each template, tell me if we should: create new, merge with existing, or skip
> 4. Start with creating `.windsurf/rules/` and adding the project-rules.md"

**Step 2: Document existing architecture**

> "Help me fill out AI_README.md by analyzing this codebase. Document the current architecture, tech stack, established patterns, and key files."

**Step 3: Security audit**

> "Review the codebase against SECURITY.md guidelines. Identify any gaps or violations, prioritized by severity."

**Step 4: Testing assessment**

> "Based on TESTING.md, analyze test coverage in this project. What areas need tests? What testing patterns should we establish?"

**Step 5: Merge remaining templates**

> "Now help me integrate the remaining Forge templates (CONTRIBUTING.md, CHANGELOG.md) — merge them with any existing files rather than replacing."

**Step 6: Establish baseline**

> "Summarize what we've set up. What are the next priorities for bringing this codebase in line with the framework guidelines?"

---

## What's Included

```
the-forge/
└── templates/
    ├── AI_README.md        # Project context for AI (architecture, patterns, key files)
    ├── CONTRIBUTING.md     # Guidelines for contributors (includes AI development info)
    ├── TESTING.md          # Testing methodology and guidelines
    ├── SECURITY.md         # Security best practices (adapted from Project CodeGuard)
    ├── CHANGELOG.md        # Version history template
    ├── project-rules.md    # Windsurf AI behavior rules (→ .windsurf/rules/)
    └── .gitignore.template # Default .gitignore (rename to .gitignore)
```

### Template Descriptions

| File | Purpose |
|------|---------|
| **AI_README.md** | The AI's "brain dump" about your project. Contains architecture, patterns, tech stack, and key files. Keep this updated as your project evolves. |
| **CONTRIBUTING.md** | Guidelines for contributors, including AI-assisted development practices. Ensures future contributors know about and maintain the AI rules. |
| **TESTING.md** | Defines how tests should be written. AI references this when suggesting or writing tests. |
| **SECURITY.md** | Security guidelines adapted from [Project CodeGuard](https://github.com/project-codeguard/rules). Covers secrets, input validation, auth, crypto, and more. |
| **CHANGELOG.md** | Standard changelog format. AI can help maintain this as features are added. |
| **project-rules.md** | Direct instructions for AI behavior. Goes in `.windsurf/rules/` directory. Self-documenting so contributors understand its purpose. |
| **.gitignore.template** | Comprehensive .gitignore with secrets, dependencies, and build artifacts. Rename to `.gitignore` in your project. |

---

## How It Works

```
┌─────────────────────────────────────────────────────────────┐
│                     Your Project                            │
├─────────────────────────────────────────────────────────────┤
│  AI_README.md          ← AI reads for project context       │
│  TESTING.md            ← AI references for test guidance    │
│  SECURITY.md           ← AI follows security practices      │
│  .windsurf/rules/      ← AI follows behavior rules          │
│    └── project-rules.md                                     │
├─────────────────────────────────────────────────────────────┤
│  src/                  ← Your code (AI helps build this)    │
│  tests/                ← Tests (AI suggests alongside code) │
└─────────────────────────────────────────────────────────────┘
```

**The AI reads the framework documents and uses them as guidelines when:**
- Choosing technologies and patterns
- Writing new code
- Suggesting tests
- Handling security-sensitive operations
- Making architectural decisions

---

## Recommended Project Structure

Once you start building, your project might look like:

```
my-project/
├── .windsurf/
│   └── rules/
│       └── project-rules.md    # AI behavior rules
├── src/                        # Source code
├── tests/
│   ├── unit/                   # Unit tests
│   └── integration/            # Integration tests
├── docs/                       # Additional documentation
├── AI_README.md                # AI project context
├── TESTING.md                  # Testing methodology
├── SECURITY.md                 # Security guidelines
├── CHANGELOG.md                # Version history
├── README.md                   # User-facing docs
└── .gitignore
```

---

## Philosophy

### AI Can Generate Code Fast. But Fast Isn't Always Right.

The Forge helps you direct AI to build things properly:

- **Security-first** - Don't hardcode secrets, validate inputs, use proper auth
- **Test-aware** - Consider testability, suggest tests alongside features
- **Pattern-consistent** - Follow established patterns, don't reinvent
- **Documentation-current** - Keep AI_README.md updated as the project evolves

### Guidelines, Not Handcuffs

These are guidelines, not rigid rules. The AI should:
- Follow them by default
- Explain when deviation makes sense
- Ask when uncertain

---

## Maintaining the Framework

Once your project is established, the framework becomes **self-sustaining** through these mechanisms:

### How Contributors Discover the Rules

1. **CONTRIBUTING.md** - Standard file contributors check before submitting PRs
2. **AI_README.md** - Contains a section pointing to the rules file
3. **project-rules.md** - Self-documenting header explains what it is and when to update

### How Rules Stay Enforced

- `.windsurf/rules/project-rules.md` is **automatically loaded** by Windsurf
- Contributors using AI-assisted development get the rules without extra steps
- The rules themselves instruct AI to follow project conventions

### Keeping Rules Current

| When This Happens | Update This |
|-------------------|-------------|
| New code patterns established | `.windsurf/rules/project-rules.md` |
| Architecture changes | `AI_README.md` and rules |
| New testing requirements | `TESTING.md` and rules |
| Security requirements change | `SECURITY.md` and rules |

### Optional: PR Template Reminder

Add `.github/PULL_REQUEST_TEMPLATE.md` to remind contributors:

```markdown
## Checklist
- [ ] Followed patterns in AI_README.md
- [ ] Updated AI_README.md if architecture changed
- [ ] Tests pass
- [ ] No security concerns (checked SECURITY.md)
```

---

## Customization

### Adding Project-Specific Rules

Edit `.windsurf/rules/project-rules.md` to add rules specific to your project:

```markdown
## Project-Specific Rules

- Use [specific framework/library] for [purpose]
- Follow [company style guide] for naming
- All API endpoints must [requirement]
```

### Updating Security Guidelines

The SECURITY.md file is adapted from Project CodeGuard. You can:
- Add industry-specific requirements (HIPAA, PCI-DSS, etc.)
- Remove sections that don't apply
- Link to your organization's security policies

---

## Resources

- **Project CodeGuard**: https://github.com/project-codeguard/rules - Full security ruleset for AI coding
- **multiply-me**: [../multiply-me/](../multiply-me/) - AI agent training and concepts

---

## Contributing & Feedback

This guide is opinionated — and probably has things that don't work perfectly in every scenario. That's where you come in.

**I'd love your feedback:**
- Found something that doesn't work? Open an issue.
- Have a pattern that works better? Submit a PR.
- Just want to chat? Reach out on my [GitHub profile](https://github.com/mrshaun13).

**How to contribute:**
1. Try it in your own projects first
2. Open an issue or PR with your suggestion
3. Include real-world examples if possible

---

> *Crafted by Shaun Robbins — one human + many tokens. Built to reduce toil for everyone to enjoy life a little bit more!*

[← Back to Supercharged](../README.md)
