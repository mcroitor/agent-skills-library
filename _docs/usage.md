# Installing and Using Skills

## How to Use

### In VS Code Copilot

To use skills with GitHub Copilot in VS Code:

1. For a project skill, place its folder under `.github/skills/`; for a personal skill, place it under `~/.copilot/skills/`. Keep `SKILL.md` directly inside the skill's own folder.
2. Open the project in VS Code and start a Copilot Chat session.
3. Type `/` to find and invoke a skill by its name, or let Copilot load it when a request matches the skill description.

You can also use **Chat: Open Customizations** from the Command Palette to create, browse, and manage workspace or user skills. Refer to the [VS Code Agent Skills documentation](https://code.visualstudio.com/docs/agent-customization/agent-skills) for supported locations and harness-specific behavior.

### In OpenCode

OpenCode supports skill integration through:

1. **Copying skill to project**:

   ```bash
    cp -r skills-library/development/php-developer .opencode/skills/development/
   ```

2. **In `.opencode/config.yml` configuration**:

   ```yaml
   skills:
     - path: ./skills/development/php-developer/SKILL.md
       enabled: true
     - path: ./skills/development/devops-engineer/SKILL.md
       enabled: true
   ```

3. **Usage in development context**:
   - Skills are automatically applied when creating new files
   - Agent selects appropriate skill based on file type
   - For explicit selection: `@php-developer develop controller`

### Using with Ollama / llama.cpp in Scripts

Use skills as context for local LLM models during development.

#### Python

**Basic example with Ollama**:

```python
import ollama

# Load skill content
with open('skills-library/development/php-developer/SKILL.md', 'r') as f:
    skill_context = f.read()

# Build a guarded prompt with explicit sections and output policy
system_rules = (
    "You are a senior PHP backend engineer. "
    "Follow the skill context strictly. "
    "If data is missing, state assumptions briefly. "
    "Return only valid PHP code."
)
user_task = "Write a REST API endpoint in PHP to get user list"
full_prompt = (
    f"<system_rules>\n{system_rules}\n</system_rules>\n"
    f"<skill_context>\n{skill_context}\n</skill_context>\n"
    f"<user_task>\n{user_task}\n</user_task>"
)

# Send request with structured context
response = ollama.generate(
    model="codellama",
    prompt=full_prompt,
    stream=False
)

print(response['response'])
```

**Using routed skill selection (recommended)**:

```python
import ollama
from pathlib import Path

# Minimal routing map: pick only the smallest sufficient skill set.
ROUTES = {
    "php_api": [
        "skills-library/development/php-developer/SKILL.md",
        "skills-library/development/web-developer/SKILL.md",
    ],
    "devops": [
        "skills-library/development/devops-engineer/SKILL.md",
    ],
}

def load_context(skill_paths):
    chunks = []
    for path in skill_paths:
        with open(Path(path), 'r', encoding='utf-8') as f:
            chunks.append(f.read())
    return "\n\n".join(chunks)

task_type = "php_api"
skills_context = load_context(ROUTES[task_type])

# Use for code generation
prompt = f"""{skills_context}

Task: Develop a complete REST API in PHP using Laravel to manage blog posts.
Requirements:
- CRUD operations for posts
- Authentication
- Data validation
- Error handling
"""

response = ollama.generate(
    model="codellama",
    prompt=prompt,
    stream=True
)

for chunk in response:
    print(chunk['response'], end='', flush=True)
```

**Interactive context usage**:

```python
import ollama

class SkillAssistant:
    def __init__(self, skill_path):
        with open(skill_path, 'r') as f:
            self.skill_context = f.read()
        self.model = "codellama"

    def generate(self, user_prompt):
        full_prompt = (
            "<system_rules>\n"
            "You are a DevOps expert. Reply concisely and with actionable steps.\n"
            "If commands are risky, include a warning.\n"
            "</system_rules>\n"
            f"<skill_context>\n{self.skill_context}\n</skill_context>\n"
            f"<user_task>\n{user_prompt}\n</user_task>"
        )
        response = ollama.generate(
            model=self.model,
            prompt=full_prompt,
            stream=False
        )
        return response['response']

    def chat(self):
        print("Type 'exit' to quit")
        while True:
            user_input = input("\nYou: ").strip()
            if user_input.lower() == 'exit':
                break

            response = self.generate(user_input)
            print(f"Assistant: {response}")

# Usage
assistant = SkillAssistant('skills-library/development/devops-engineer/SKILL.md')
assistant.chat()
```

#### PHP

**Basic example with curl**:

```php
<?php

// Load skill content
$skillContent = file_get_contents('skills-library/development/cpp-developer/SKILL.md');

// Prepare request
$prompt = $skillContent . "\n\nOptimize this C++ code for working with large data:\n\nvector<int> data = {...};";

// Send to local llama.cpp server
$ch = curl_init('http://localhost:8000/completion');
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode([
    'prompt' => $prompt,
    'n_predict' => 500,
    'temperature' => 0.7
]));
curl_setopt($ch, CURLOPT_HTTPHEADER, ['Content-Type: application/json']);

$response = curl_exec($ch);
$result = json_decode($response, true);

echo $result['content'];
curl_close($ch);
?>
```

**Using multiple skills in PHP**:

```php
<?php

class OllamaSkillAssistant {
    private $serverUrl = 'http://localhost:8000';
    private $model = 'codellama';
    private $skillsContext = '';
    private $routes = [
        'php_api' => [
            'skills-library/development/php-developer/SKILL.md',
            'skills-library/development/web-developer/SKILL.md'
        ],
        'moodle' => [
            'skills-library/development/moodle-developer/SKILL.md',
            'skills-library/development/php-developer/SKILL.md',
            'skills-library/development/mariadb-administrator/SKILL.md'
        ],
        'devops' => [
            'skills-library/development/devops-engineer/SKILL.md'
        ]
    ];

    private function loadRoute(string $routeKey): void {
        $this->skillsContext = '';
        foreach ($this->routes[$routeKey] as $file) {
            $this->skillsContext .= file_get_contents($file) . "\n\n";
        }
    }

    public function generate($prompt, $routeKey = 'php_api', $maxTokens = 1000) {
        // Backward-compatible: allow passing maxTokens as the 2nd positional argument.

        if (is_int($routeKey)) {

            $maxTokens = $routeKey;

            $routeKey = 'php_api';

        }



        $this->loadRoute($routeKey);

        $systemRules = "You are a senior software engineer. Use the provided skill context strictly. Return practical, production-oriented output.";
        $fullPrompt = "<system_rules>\n" . $systemRules . "\n</system_rules>\n"
            . "<skill_context>\n" . $this->skillsContext . "\n</skill_context>\n"
            . "<user_task>\n" . $prompt . "\n</user_task>";

        $ch = curl_init($this->serverUrl . '/completion');
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($ch, CURLOPT_POST, true);
        curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode([
            'prompt' => $fullPrompt,
            'n_predict' => $maxTokens,
            'temperature' => 0.7,
            'stop' => ["\n\n", "---"]
        ]));
        curl_setopt($ch, CURLOPT_HTTPHEADER, ['Content-Type: application/json']);

        $response = curl_exec($ch);
        curl_close($ch);

        $result = json_decode($response, true);
        return $result['content'] ?? '';
    }

    public function generateMoodle($prompt) {
        return $this->generate($prompt, 'moodle');
    }
}

// Usage
$assistant = new OllamaSkillAssistant();

// Generate DevOps code
$devopsCode = $assistant->generate('Create Docker Compose for application with nginx, php-fpm and postgresql', 'devops');
echo "=== DevOps Solution ===\n$devopsCode\n\n";

// Generate Moodle plugin
$moodleCode = $assistant->generateMoodle('Develop a simple Moodle plugin for creating surveys');
echo "=== Moodle Plugin ===\n$moodleCode\n";
?>
```

**Integration with test automation script**:

```php
<?php

class TestGeneratorWithSkills {
    private $assistant;

    public function __construct() {
        $this->assistant = new OllamaSkillAssistant();
    }

    public function generateTestScenarios($featureName) {
        $prompt = <<<PROMPT
Write test scenarios for function: $featureName

Requirements:
1. Use BDD Gherkin format (Feature/Scenario/Given-When-Then) from Test Scenario Writer skill
2. Include happy path and edge cases
3. Write at least 5 test scenarios
PROMPT;

        return $this->assistant->generate($prompt);
    }

    public function generatePhpUnitTests($functionSignature) {
        $prompt = <<<PROMPT
Based on Test Writer skill, write PHPUnit tests for function:

$functionSignature

Requirements:
1. Use Arrange-Act-Assert pattern
2. Add mocks where necessary
3. Cover edge cases
PROMPT;

        return $this->assistant->generate($prompt, 1500);
    }
}

// Usage
$generator = new TestGeneratorWithSkills();

// Generate scenarios
$scenarios = $generator->generateTestScenarios('user authentication');
file_put_contents('test_scenarios.md', $scenarios);

// Generate unit tests
$tests = $generator->generatePhpUnitTests('public function authenticateUser($email, $password)');
file_put_contents('AuthTest.php', $tests);
?>
```

#### Recommended Models and Setup

**Ollama Installation** (for Python):

```bash
# On macOS or Linux
curl -fsSL https://ollama.ai/install.sh | sh

# Download required model
ollama pull codellama
ollama pull llama2

# Start server
ollama serve
```

**llama.cpp Installation** (for API server):

```bash
# Clone repository
git clone https://github.com/ggerganov/llama.cpp.git
cd llama.cpp

# Compile
make

# Download GGUF model and run
./server -m model.gguf -ngl 99 --port 8000
```

**Recommended Models**:

- `codellama:7b` — best choice for code generation
- `codellama:13b` — more accurate, requires more memory
- `mistral:latest` — fast and universal
- `llama2:latest` — universal, good balance

## Skill Dependencies

Some skills are built on others and require understanding of base skills:

```text
Common Skills
├─→ Brainstorming
├─→ Problem Decomposer
├─→ Research Synthesizer
└─→ Communication Adapter

AI Skills
└─→ Artificial Intelligence Specialist
    ├─→ AI Product Manager ⭐ (Derived from)
    └─→ AI Prompt Engineer ⭐ (Derived from)

Development Skills
├─→ Architect
│   └─→ Web Developer
│       └─→ DevOps Engineer ⭐ (Based on)
├─→ Database Developer
│   └─→ MariaDB Administrator ⭐ (Based on)
│       └─→ Moodle Developer ⭐⭐ (Based on PHP Developer + MariaDB Administrator)
├─→ PHP Developer
│   └─→ Moodle Developer ⭐⭐ (Based on PHP Developer + MariaDB Administrator)
├─→ C++ Developer
│   ├─→ Windows C++ Developer ⭐ (Derived from)
│   └─→ Linux C++ Developer ⭐ (Derived from)
└─→ Frontend Designer
    ├─→ Bootstrap Designer ⭐ (Derived from)
    ├─→ Tailwind Designer ⭐ (Derived from)
    └─→ Skeleton Designer ⭐ (Derived from)

Document Skills
├─→ Technical Documentation Specialist
└─→ Scientific Writing Editor
    ├─→ Academic Manuscript Editor ⭐ (Derived from)
    └─→ Research Writing Assistant ⭐ (Derived from)

Education Skills
├─→ Learning Path Designer
│   └─→ Curriculum Developer ⭐ (Derived from)
│       ├─→ Assessment Writer ⭐ (Derived from)
│       │   └─→ Rubric Designer ⭐ (Derived from)
│       └─→ Quiz Developer ⭐ (Derived from)
└─→ Educational Content Reviewer
    └─→ Course Localization Specialist ⭐ (Derived from)

Testing Skills
├─→ Test Scenario Writer
└─→ Test Writer
```

**Legend and Glossary:**

- ⭐ — specialized skill (extension of base)
- ⭐⭐ — complex skill (combination of multiple)
- Derived from — inherits behavior contracts (priority rules, constraints, workflow) and specializes them
- Based on — reuses concepts, tools, or context from another skill without full behavior inheritance

### Usage Examples

**For Brainstorming:**

```text
Help me come up with ideas for new features in the project...
```

**For Architect:**

```text
Design architecture for a scalable e-commerce application
```

**For PHP Developer:**

```text
Write a Laravel controller for user management
```

**For C++ Developer:**

```text
Optimize this algorithm in C++
```

**For MariaDB Administrator:**

```text
Help optimize MariaDB configuration for 1M requests per hour
```

**For Moodle Developer:**

```text
Develop a Moodle plugin that integrates grading system from external system
```

**For DevOps Engineer:**

```text
Create GitHub Actions workflow for automatic Docker container deployment to production
```

**For Technical Documentation Specialist:**

```text
Create an API integration guide with prerequisites, examples, and troubleshooting
```

**For Scientific Writing Editor:**

```text
Edit this research report for scientific tone, claim-evidence clarity, and consistent IEEE citations
```

**For Academic Manuscript Editor:**

```text
Revise this paper draft into submission-ready IMRAD structure and prepare a reviewer response outline
```

**For Research Writing Assistant:**

```text
Convert these experiment notes into a coherent related-work and discussion draft with evidence-qualified language
```

**For Artificial Intelligence Specialist:**

```text
Design a RAG architecture for internal knowledge search with evaluation metrics
```

**For AI Product Manager:**

```text
Define KPI and rollout plan for an AI assistant feature in a SaaS product
```

**For AI Prompt Engineer:**

```text
Create and benchmark prompt variants for structured JSON output with strict schema
```

## Requirements

- **For VS Code Copilot**: VS Code with GitHub Copilot; use `.github/skills/` for project skills or `~/.copilot/skills/` for personal skills
- **For OpenCode**: OpenCode editor with skill integration support
- **For Ollama/llama.cpp**:
  - [Ollama](https://ollama.ai) installed and running, or
  - [llama.cpp](https://github.com/ggerganov/llama.cpp) compiled
  - GGUF format model loaded (e.g., `llama2`, `mistral`, `codellama`)
  - Minimum 8GB RAM (16GB recommended for larger models)

## Extension

To add new skills:

1. Create new folder: `new-skill-name/`
2. Add `SKILL.md` file with description and instructions
3. Follow existing skill structure
4. Update the English and Russian skill catalogs in `_docs/skills.md` and `_docs/skills.ru.md`

## Best Practices

- Each skill should be narrowly specialized
- Clearly define area of application
- Provide step-by-step instructions
- Document tools and technologies used
- Regularly update skills as technologies evolve

## Document metadata

- Version: 1.5
- Created: 2026
- Author: Mihail Croitor + GitHub Copilot
