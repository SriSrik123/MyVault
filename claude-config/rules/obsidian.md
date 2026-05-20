# Obsidian Rules

## Before Starting Any Task

1. Load context proactively. **Don't ask Sri for information that's already in the vault.**
   Check these files at the start of any session involving his academics or life:
   - `~/Documents/MyVault/context/about-me.md`
   - `~/Documents/MyVault/context/semester-spring-2026.md`
   - `~/Documents/MyVault/context/study-profile.md`
   - `~/Documents/MyVault/context/goals.md`
   - `~/Documents/MyVault/second-brain/notes/TODO.md`

2. When Sri references a course by code (CS-270, SE-201, PHYS-102, etc.), go read its
   syllabus and assignments index first:
   - `~/Documents/MyVault/second-brain/notes/<course-folder>/syllabus.md`
   - `~/Documents/MyVault/second-brain/notes/<course-folder>/assignments/index.md`
   - `~/Documents/MyVault/second-brain/notes/<course-folder>/exams/index.md`

3. When Sri mentions a person, check `context/relationships.md`.

4. When Sri mentions a project, check `context/projects.md`.

## Searching the Vault

**Keyword search (use this first):**
```bash
find ~/Documents/MyVault -name "*.md" | xargs grep -l "KEYWORD" 2>/dev/null
```

**Read a specific file:**
```bash
cat ~/Documents/MyVault/context/about-me.md
```

**Find all notes for a course:**
```bash
ls ~/Documents/MyVault/second-brain/notes/math-foundations-cs/lectures/
```

**Search for deadline patterns:**
```bash
grep -r "due" ~/Documents/MyVault/second-brain/notes/TODO.md
```

## Writing to the Vault

- **New lecture notes** → `~/Documents/MyVault/second-brain/notes/<course>/lectures/YYYY-MM-DD-topic.md`
- **Daily briefing** → `~/Documents/MyVault/context/daily-logs/YYYY-MM-DD.md`
- **Task updates** → edit `~/Documents/MyVault/second-brain/notes/TODO.md` in place
- **Context updates** → edit the relevant file in `~/Documents/MyVault/context/`

## Never

- Ask Sri to repeat information that's already in the vault
- Create a new context file that duplicates an existing one
- Write notes to any location other than the paths above
