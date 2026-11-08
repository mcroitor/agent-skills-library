# Установка и использование навыков

## Как использовать

### В VS Code Copilot

Чтобы использовать навыки с GitHub Copilot в VS Code:

1. Для навыка проекта поместите его папку в `.github/skills/`, для личного навыка — в `~/.copilot/skills/`. Файл `SKILL.md` должен находиться непосредственно в папке навыка.
2. Откройте проект в VS Code и начните чат Copilot.
3. Введите `/`, чтобы найти и вызвать навык по имени, или позвольте Copilot загрузить его автоматически, если запрос соответствует описанию навыка.

Также навыками можно управлять через **Chat: Open Customizations** в Command Palette. Подробности о расположении навыков и поведении разных harness см. в [документации VS Code по Agent Skills](https://code.visualstudio.com/docs/agent-customization/agent-skills).

### В OpenCode

OpenCode поддерживает интеграцию со скиллами через:

1. **Копирование скилла в проект**:

   ```bash
    cp -r skills-library/development/php-developer .opencode/skills/development/
   ```

2. **В конфигурации `.opencode/config.yml`**:

   ```yaml
   skills:
     - path: ./skills/development/php-developer/SKILL.md
       enabled: true
     - path: ./skills/development/devops-engineer/SKILL.md
       enabled: true
   ```

3. **Использование в контексте разработки**:
   - Навыки автоматически применяются при создании новых файлов
   - Агент выбирает подходящий навык в зависимости от типа файла
   - Для явного выбора: `@php-developer разработай контроллер`

### Использование с Ollama / llama.cpp в скриптах

Используйте скиллы как контекст для локальных LLM моделей при разработке.

#### Python

**Базовый пример с Ollama**:

```python
import ollama

# Загрузите содержимое скилла
with open('skills-library/development/php-developer/SKILL.md', 'r') as f:
    skill_context = f.read()

# Сформируйте защищенный промпт с явными секциями
system_rules = (
    "You are a senior PHP backend engineer. "
    "Follow the skill context strictly. "
    "If data is missing, state assumptions briefly. "
    "Return only valid PHP code."
)
user_task = "Напиши REST API endpoint на PHP для получения списка пользователей"
full_prompt = (
    f"<system_rules>\n{system_rules}\n</system_rules>\n"
    f"<skill_context>\n{skill_context}\n</skill_context>\n"
    f"<user_task>\n{user_task}\n</user_task>"
)

# Отправьте запрос со структурированным контекстом
response = ollama.generate(
    model="codellama",
    prompt=full_prompt,
    stream=False
)

print(response['response'])
```

**Использование маршрутизации скиллов (рекомендуется)**:

```python
import ollama
from pathlib import Path

# Минимальная карта маршрутов: подключайте только достаточный набор скиллов.
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

# Используйте для генерации кода
prompt = f"""{skills_context}

Задача: Разработай полный REST API на PHP с использованием Laravel для управления постами блога.
Требования:
- CRUD операции для постов
- Аутентификация
- Валидация данных
- Обработка ошибок
"""

response = ollama.generate(
    model="codellama",
    prompt=prompt,
    stream=True
)

for chunk in response:
    print(chunk['response'], end='', flush=True)
```

**Интерактивная работа с контекстом**:

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
        print("Введите 'exit' для выхода")
        while True:
            user_input = input("\nВы: ").strip()
            if user_input.lower() == 'exit':
                break

            response = self.generate(user_input)
            print(f"Ассистент: {response}")

# Используйте
assistant = SkillAssistant('skills-library/development/devops-engineer/SKILL.md')
assistant.chat()
```

#### PHP

**Базовый пример с curl**:

```php
<?php

// Загрузите содержимое скилла
$skillContent = file_get_contents('skills-library/development/cpp-developer/SKILL.md');

// Подготовьте запрос
$prompt = $skillContent . "\n\nОптимизируй этот C++ код для работы с большими данными:\n\nvector<int> data = {...};";

// Отправьте на локальный сервер llama.cpp
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

**Использование маршрутизации скиллов в PHP**:

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

// Используйте
$assistant = new OllamaSkillAssistant();

// Генерируйте код DevOps
$devopsCode = $assistant->generate('Создай Docker Compose для приложения с nginx, php-fpm и postgresql', 'devops');
echo "=== DevOps Solution ===\n$devopsCode\n\n";

// Генерируйте Moodle плагин
$moodleCode = $assistant->generateMoodle('Разработай простой Moodle плагин для создания опросов');
echo "=== Moodle Plugin ===\n$moodleCode\n";
?>
```

**Интеграция со скриптом автоматизации тестов**:

```php
<?php

class TestGeneratorWithSkills {
    private $assistant;

    public function __construct() {
        $this->assistant = new OllamaSkillAssistant();
    }

    public function generateTestScenarios($featureName) {
        $prompt = <<<PROMPT
Напиши тестовые сценарии для функции: $featureName

Требования:
1. Используй BDD Gherkin формат (Feature/Scenario/Given-When-Then) из навыка Test Scenario Writer
2. Включи happy path и edge cases
3. Напиши минимум 5 тестовых сценариев
PROMPT;

        return $this->assistant->generate($prompt);
    }

    public function generatePhpUnitTests($functionSignature) {
        $prompt = <<<PROMPT
На основе навыка Test Writer напиши PHPUnit тесты для функции:

$functionSignature

Требования:
1. Используй Arrange-Act-Assert паттерн
2. Добавь моки где необходимо
3. Покрой граничные случаи
PROMPT;

        return $this->assistant->generate($prompt, 1500);
    }
}

// Используйте
$generator = new TestGeneratorWithSkills();

// Генерируйте сценарии
$scenarios = $generator->generateTestScenarios('пользовательская аутентификация');
file_put_contents('test_scenarios.md', $scenarios);

// Генерируйте unit тесты
$tests = $generator->generatePhpUnitTests('public function authenticateUser($email, $password)');
file_put_contents('AuthTest.php', $tests);
?>
```

#### Рекомендуемые модели и настройка

**Установка Ollama** (для Python):

```bash
# На macOS или Linux
curl -fsSL https://ollama.ai/install.sh | sh

# Скачайте нужную модель
ollama pull codellama
ollama pull llama2

# Запустите сервер
ollama serve
```

**Установка llama.cpp** (для API сервера):

```bash
# Клонируйте репозиторий
git clone https://github.com/ggerganov/llama.cpp.git
cd llama.cpp

# Скомпилируйте
make

# Скачайте GGUF модель и запустите
./server -m model.gguf -ngl 99 --port 8000
```

**Рекомендуемые модели**:

- `codellama:7b` — лучший выбор для генерации кода
- `codellama:13b` — более точный, требует больше памяти
- `mistral:latest` — быстрый и универсальный
- `llama2:latest` — универсальный, хороший баланс

## Зависимости между скиллами

Некоторые скиллы строятся на базе других и требуют понимания базовых скиллов:

```text
Общие навыки
├─→ Brainstorming
├─→ Problem Decomposer
├─→ Research Synthesizer
└─→ Communication Adapter

AI навыки
└─→ Artificial Intelligence Specialist
    ├─→ AI Product Manager ⭐ (производный от)
    └─→ AI Prompt Engineer ⭐ (производный от)

Навыки разработки
├─→ Architect
│   └─→ Web Developer
│       └─→ DevOps Engineer ⭐ (на базе)
├─→ Database Developer
│   └─→ MariaDB Administrator ⭐ (на базе)
│       └─→ Moodle Developer ⭐⭐ (на базе PHP Developer + MariaDB Administrator)
├─→ PHP Developer
│   └─→ Moodle Developer ⭐⭐ (на базе PHP Developer + MariaDB Administrator)
├─→ C++ Developer
│   ├─→ Windows C++ Developer ⭐ (производный от)
│   └─→ Linux C++ Developer ⭐ (производный от)
└─→ Frontend Designer
    ├─→ Bootstrap Designer ⭐ (производный от)
    ├─→ Tailwind Designer ⭐ (производный от)
    └─→ Skeleton Designer ⭐ (производный от)

Навыки работы с документами
├─→ Technical Documentation Specialist
└─→ Scientific Writing Editor
    ├─→ Academic Manuscript Editor ⭐ (производный от)
    └─→ Research Writing Assistant ⭐ (производный от)

Образовательные навыки
├─→ Learning Path Designer
│   └─→ Curriculum Developer ⭐ (производный от)
│       ├─→ Assessment Writer ⭐ (производный от)
│       │   └─→ Rubric Designer ⭐ (производный от)
│       └─→ Quiz Developer ⭐ (производный от)
└─→ Educational Content Reviewer
    └─→ Course Localization Specialist ⭐ (производный от)

Навыки тестирования
├─→ Test Scenario Writer
└─→ Test Writer
```

**Легенда:**

- ⭐ — специализированный скилл (расширение базового)
- ⭐⭐ — комплексный скилл (комбинирование нескольких)
- Производный от — наследует поведенческие контракты (priority rules, constraints, workflow) и специализирует их
- На базе — переиспользует концепции, инструменты или контекст другого скилла без полного наследования поведения

### Примеры использования

**Для Brainstorming:**

```text
Помоги мне придумать идеи для нового функционала в проекте...
```

**Для архитектора:**

```text
Спроектируй архитектуру для масштабируемого e-commerce приложения
```

**Для PHP разработчика:**

```text
Напиши Laravel контроллер для управления пользователями
```

**Для C++ разработчика:**

```text
Оптимизируй этот алгоритм на C++
```

**Для MariaDB администратора:**

```text
Помоги оптимизировать конфигурацию MariaDB для 1M запросов в час
```

**Для Moodle разработчика:**

```text
Разработай плагин для Moodle, который интегрирует систему оценок из внешней системы
```

**Для DevOps инженера:**

```text
Создай GitHub Actions workflow для автоматического деплоя Docker контейнера на production
```

**Для специалиста по технической документации:**

```text
Подготовь API integration guide с prerequisites, примерами и troubleshooting
```

**Для Scientific Writing Editor:**

```text
Отредактируй исследовательский отчет: выровняй научный тон, усили логику claim-evidence и приведи ссылки к стилю IEEE
```

**Для Academic Manuscript Editor:**

```text
Приведи черновик статьи к публикационному IMRAD-формату и подготовь скелет ответа рецензентам
```

**Для Research Writing Assistant:**

```text
Преобразуй заметки экспериментов в связный черновик related work и discussion с evidence-qualified формулировками
```

**Для специалиста по искусственному интеллекту:**

```text
Спроектируй RAG-архитектуру для внутреннего поиска знаний и задай метрики оценки
```

**Для AI Product Manager:**

```text
Определи KPI и rollout-план для AI-ассистента в SaaS-продукте
```

**Для AI Prompt Engineer:**

```text
Создай и сравни версии промптов для строгого JSON-ответа по заданной схеме
```

## Требования

- **Для VS Code Copilot**: VS Code с GitHub Copilot; навыки проекта размещаются в `.github/skills/`, личные навыки — в `~/.copilot/skills/`
- **Для OpenCode**: OpenCode editor с поддержкой интеграции скиллов
- **Для Ollama/llama.cpp**:
  - [Ollama](https://ollama.ai) установлен и запущен, или
  - [llama.cpp](https://github.com/ggerganov/llama.cpp) скомпилирован
  - Модель GGUF формата загруженная (например, `llama2`, `mistral`, `codellama`)
  - Минимум 8GB RAM (16GB рекомендуется для более крупных моделей)

## Расширение

Для добавления новых навыков:

1. Создайте новую папку: `new-skill-name/`
2. Добавьте файл `SKILL.md` с описанием и инструкциями
3. Следуйте структуре существующих навыков
4. Обновите каталоги навыков на английском и русском языках в `_docs/skills.md` и `_docs/skills.ru.md`

## Лучшие практики

- Каждый навык должен быть узкоспециализированным
- Четко определите область применения
- Предоставьте пошаговые инструкции
- Документируйте используемые инструменты и технологии
- Регулярно обновляйте навыки по мере развития технологий

## Метаданные документа

- Версия: 1.5
- Дата создания: 2026
- Автор: Mihail Croitor + GitHub Copilot
