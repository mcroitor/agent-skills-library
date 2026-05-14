# Библиотека навыков

Коллекция навыков для AI агентов.

1. [AI](./ai/) - навыки для работы с искусственным интеллектом
2. [common](./common/) - общие навыки для всех агентов
3. [development](./development/) - навыки для разработки программного обеспечения
4. [documents](./documents/) - навыки для создания и управления документацией (OCR, перевод, структурирование, техническая документация, и т.д.)
5. [education](./education/) - навыки для обучения, создания образовательного контента и проверки знаний
6. [testing](./testing/) - навыки для тестирования и QA

## Доступные навыки

### 1. AI

#### 1.1. Специалист по искусственному интеллекту (`ai/ai-specialist/SKILL.md`)

Проектирование и внедрение AI-функциональности и ML/LLM решений.

- Prompt engineering и RAG-архитектуры
- Оценка качества, безопасность и надежность моделей
- Оптимизация AI-систем и MLOps-практики

#### 1.2. AI Product Manager (`ai/ai-product-manager/SKILL.md`) ⭐ производный от Специалиста по искусственному интеллекту

Продуктовая стратегия и внедрение AI-функциональности.

- Discovery и приоритизация AI-фич
- KPI, rollout и контроль рисков
- Кросс-функциональная координация и итерации

#### 1.3. AI Prompt Engineer (`ai/ai-prompt-engineer/SKILL.md`) ⭐ производный от Специалиста по искусственному интеллекту

Проектирование промптов и контекста для надежных ответов LLM.

- Prompt templates и контроль формата вывода
- Оценка качества промптов и бенчмарки
- RAG-aware prompting и guardrails

### 2. Common

#### 2.1. Brainstorming (`common/brainstorming/SKILL.md`)

Генерация идей, творческое решение проблем, мозговые штурмы.

- Метод SCAMPER
- Mind mapping
- Анализ множества вариантов решения

#### 2.2. Problem Decomposer (`common/problem-decomposer/SKILL.md`)

Структурная декомпозиция сложных задач на понятные и выполнимые шаги.

- Определение границ задачи и ограничений
- Разбиение на подзадачи и упорядочивание зависимостей
- Контрольные точки, риски и план действий

#### 2.3. Research Synthesizer (`common/research-synthesizer/SKILL.md`)

Синтез нескольких источников в краткие выводы с опорой на факты.

- Выделение тем и противоречий
- Оценка уверенности в выводах
- Практические рекомендации и открытые вопросы

#### 2.4. Communication Adapter (`common/communication-adapter/SKILL.md`)

Адаптация коммуникации под аудиторию и нужный уровень детализации.

- Формулировка сообщения под контекст аудитории
- Выбор формата и глубины изложения
- Ясная фиксация решений и следующих шагов

### 3. Development

#### 3.1. Архитектор программного обеспечения (`development/architect/SKILL.md`)

Проектирование архитектуры систем, выбор паттернов, анализ требований.

- Архитектурные паттерны (MVC, CQRS, Microservices)
- Масштабируемость и производительность
- Безопасность и отказоустойчивость

#### 3.2. Разработчик PHP (`development/php-developer/SKILL.md`)

Разработка на PHP, работа с фреймворками, базами данных.

- PHP 8.x синтаксис
- Laravel, Symfony, Slim
- PSR стандарты
- Безопасность приложений

#### 3.3. Разработчик C++ (`development/cpp-developer/SKILL.md`)

Высокопроизводительная разработка, системное программирование.

- Современный C++ (C++17, C++20)
- Smart pointers и RAII
- STL и многопоточность
- Оптимизация производительности

#### 3.4. Web разработчик (`development/web-developer/SKILL.md`)

Полнофункциональная разработка веб-приложений.

- Frontend и Backend разработка
- REST и GraphQL API
- Containerization и Deployment
- Облачные платформы (AWS, Azure, Google Cloud)

#### 3.5. Frontend Designer (базовый) (`development/frontend-designer/SKILL.md`)

Базовый навык проектирования интерфейсов, независимый от конкретного CSS-фреймворка.

- Подход semantic HTML-first
- Базовые принципы responsive дизайна
- Приоритет accessibility
- Design tokens и переиспользуемые паттерны

#### 3.6. Bootstrap Designer (`development/bootstrap-designer/SKILL.md`) ⭐ производный от Frontend Designer

Проектирование интерфейсов на Bootstrap для быстрого выпуска и переиспользуемых компонентов.

- Bootstrap grid и композиция компонентов
- Utility-классы для layout и spacing
- Темизация с минимальными переопределениями
- Адаптивность через стандартные breakpoints

#### 3.7. Tailwind Designer (`development/tailwind-designer/SKILL.md`) ⭐ производный от Frontend Designer

Проектирование интерфейсов на Tailwind CSS с utility-first подходом.

- Композиция UI через utility-классы
- Настройка tailwind config и токенов
- Responsive и state-варианты
- Масштабируемость в компонентных проектах

#### 3.8. Skeleton Designer (`development/skeleton-designer/SKILL.md`) ⭐ производный от Frontend Designer

Легковесное проектирование минималистичных интерфейсов на Skeleton CSS.

- Минимальный размер CSS
- 12-колоночная сетка и semantic HTML
- Быстрое прототипирование без лишних зависимостей
- Опциональный стартовый CSS-ассет для расширения темы

#### 3.9. Разработчик баз данных (`development/database-developer/SKILL.md`)

Проектирование и оптимизация баз данных, SQL разработка.

- SQL оптимизация и индексирование
- Нормализация и проектирование схем
- Хранимые процедуры и триггеры
- Реляционные и NoSQL БД

#### 3.10. MariaDB Administrator (`development/mariadb-administrator/SKILL.md`) ⭐ на базе Database Developer

Специализированный администратор баз данных MariaDB.

- Конфигурация и оптимизация MariaDB
- Репликация и Galera Cluster
- Backup и восстановление данных
- Мониторинг производительности

#### 3.11. Moodle Developer (`development/moodle-developer/SKILL.md`) ⭐⭐ на базе PHP Developer + MariaDB Administrator

Разработка и кастомизация Moodle LMS.

- Разработка плагинов для Moodle
- Темизация и кастомизация
- Интеграция внешних систем
- Оптимизация производительности Moodle

#### 3.12. DevOps инженер (`development/devops-engineer/SKILL.md`) ⭐ на базе Web Developer

Контейнеризация, оркестрация и автоматизация деплоя.

- Docker и Docker Compose
- GitHub Actions для CI/CD
- Мониторинг и логирование
- Security и оптимизация инфраструктуры

### 4. Documents

#### 4.1. Специалист по технической документации (`documents/technical-documentation-specialist/SKILL.md`)

Написание технической документации для продуктов, API и эксплуатации.

- Docs-as-code и Markdown-подход
- API-референсы, runbook и migration guides
- Единые стандарты качества документации

#### 4.2. Scientific Writing Editor (`documents/scientific-writing-editor/SKILL.md`)

Базовый навык для улучшения научного текста, прозрачности аргументации и связи утверждений с доказательствами.

- Научный тон и калибровка уверенности
- Логика claim-evidence и ясность аргументов
- Связность текста, переходы и единообразие терминов
- Консистентность цитирования и аккуратность библиографии

#### 4.3. Academic Manuscript Editor (`documents/academic-manuscript-editor/SKILL.md`) ⭐ производный от Scientific Writing Editor

Редактирование рукописей под публикацию с фокусом на IMRAD, требования площадки и работу с ревью.

- Архитектура рукописи и доработка разделов
- Соответствие требованиям журнала/конференции
- Улучшение title/abstract/discussion
- Подготовка submission и response-to-reviewers

#### 4.4. Research Writing Assistant (`documents/research-writing-assistant/SKILL.md`) ⭐ производный от Scientific Writing Editor

Помощь в черновом написании научного текста из заметок, источников и результатов исследования.

- Преобразование заметок в структурированный черновик
- Синтез литературы и related work
- Цитирование в процессе написания и последующая вычитка
- Формулировка вклада, ограничений и направлений future work

### 5. Education

#### 5.1. Learning Path Designer (`education/learning-path-designer/SKILL.md`)

Проектирование траектории обучения, контрольных точек и стратегии прогресса.

- Определение prerequisite
- Проектирование learning outcomes
- Планирование milestones и checkpoints

#### 5.2. Curriculum Developer (`education/curriculum-developer/SKILL.md`) ⭐ производный от Learning Path Designer

Проектирование структуры курса, модулей и последовательности уроков.

- Curriculum mapping
- Планирование модулей и уроков
- Последовательности, выровненные по learning outcomes

#### 5.3. Assessment Writer (`education/assessment-writer/SKILL.md`) ⭐ производный от Curriculum Developer

Проектирование практических оценочных заданий и политики оценивания, с делегированием детальной разработки рубрики при необходимости.

- Определение области оценочных критериев
- Проектирование performance-based оценивания
- Политика scoring и проверка alignment

#### 5.4. Rubric Designer (`education/rubric-designer/SKILL.md`) ⭐ производный от Assessment Writer

Проектирование оценочных рубрик с наблюдаемыми критериями, уровнями и калиброванной моделью scoring.

- Выбор стратегии analytic/holistic rubric
- Таблица критериев и архитектура уровней
- Калибровка дескрипторов и проверка качества

#### 5.5. Quiz Developer (`education/quiz-developer/SKILL.md`) ⭐ производный от Curriculum Developer

Разработка квизов/экзаменов, создание банка вопросов и практических тестов на базе исходного материала.

- Маппинг покрытия тем
- Генерация question bank
- Проектирование single choice и multiple select вопросов
- Ответы и объяснения

#### 5.6. Educational Content Reviewer (`education/educational-content-reviewer/SKILL.md`)

Проверка учебных материалов на ясность, точность, структуру и педагогическое качество.

- Проверка точности и ясности
- Проверка покрытия и структуры
- Приоритизация правок

#### 5.7. Course Localization Specialist (`education/course-localization-specialist/SKILL.md`) ⭐ производный от Educational Content Reviewer

Локализация курсов и учебных материалов под другой язык и региональный контекст.

- Адаптация терминологии
- Культурная и региональная адаптация
- Проверка fidelity и consistency

### 6. Testing

#### 6.1. Специалист по тестовым сценариям (`testing/test-scenario-writer/SKILL.md`)

Проектирование BDD-сценариев в формате Gherkin/Cucumber для приемки и покрытия поведения.

- Проектирование сценариев Given/When/Then
- Boundary Value Analysis
- Планирование поведенческого покрытия
- QA методологии

#### 6.2. Специалист по написанию тестов (`testing/test-writer/SKILL.md`)

Автоматизация тестирования, написание unit, integration и e2e тестов.

- Unit тестирование
- Integration и e2e тесты
- CI/CD интеграция
- Code coverage метрики

## Структура папок

```text
<repo_root>/
├── cspell.json
├── README.md
├── README.ru.md (этот файл)
├── ai/
│   ├── ai-product-manager/
│   │   └── SKILL.md
│   ├── ai-prompt-engineer/
│   │   └── SKILL.md
│   └── ai-specialist/
│       └── SKILL.md
├── common/
│   ├── brainstorming/
│   │   └── SKILL.md
│   ├── communication-adapter/
│   │   └── SKILL.md
│   ├── problem-decomposer/
│   │   └── SKILL.md
│   └── research-synthesizer/
│       └── SKILL.md
├── development/
│   ├── architect/
│   │   └── SKILL.md
│   ├── bootstrap-designer/
│   │   └── SKILL.md
│   ├── cpp-developer/
│   │   └── SKILL.md
│   ├── database-developer/
│   │   └── SKILL.md
│   ├── devops-engineer/
│   │   └── SKILL.md
│   ├── frontend-designer/
│   │   └── SKILL.md
│   ├── mariadb-administrator/
│   │   └── SKILL.md
│   ├── moodle-developer/
│   │   └── SKILL.md
│   ├── php-developer/
│   │   └── SKILL.md
│   ├── skeleton-designer/
│   │   ├── assets/
│   │   │   └── skeleton-designer-base.css
│   │   └── SKILL.md
│   ├── tailwind-designer/
│   │   └── SKILL.md
│   └── web-developer/
│       └── SKILL.md
├── documents/
│   ├── academic-manuscript-editor/
│   │   └── SKILL.md
│   ├── research-writing-assistant/
│   │   └── SKILL.md
│   ├── scientific-writing-editor/
│   │   └── SKILL.md
│   └── technical-documentation-specialist/
│       └── SKILL.md
├── education/
│   ├── assessment-writer/
│   │   └── SKILL.md
│   ├── course-localization-specialist/
│   │   └── SKILL.md
│   ├── curriculum-developer/
│   │   └── SKILL.md
│   ├── educational-content-reviewer/
│   │   └── SKILL.md
│   ├── learning-path-designer/
│   │   └── SKILL.md
│   ├── rubric-designer/
│   │   └── SKILL.md
│   └── quiz-developer/
│       └── SKILL.md
└── testing/
    ├── test-scenario-writer/
    │   └── SKILL.md
    └── test-writer/
        └── SKILL.md
```

## Как использовать

### В VS Code Copilot

Чтобы использовать навыки в VS Code:

1. Скопируйте необходимые папки в `~/.vscode/extensions/copilot/skills/` или в папку VS Code User Extensions
2. Укажите путь к навыкам в VS Code settings
3. Обратитесь к агенту с именем навыка

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

**Использование нескольких скиллов**:

```python
import ollama
from pathlib import Path

# Загрузите несколько скиллов
skills_context = ""
skills_dir = Path('skills-library')

for skill_file in skills_dir.rglob('SKILL.md'):
    with open(skill_file, 'r') as f:
        skills_context += f.read() + "\n\n"

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

**Использование нескольких скиллов в PHP**:

```php
<?php

class OllamaSkillAssistant {
    private $serverUrl = 'http://localhost:8000';
    private $model = 'codellama';
    private $skillsContext = '';
    
    public function __construct($skillsDir = 'skills-library') {
        $this->loadSkills($skillsDir);
    }
    
    private function loadSkills($skillsDir) {
        $files = glob("$skillsDir/*/*/SKILL.md");
        foreach ($files as $file) {
            $this->skillsContext .= file_get_contents($file) . "\n\n";
        }
    }
    
    public function generate($prompt, $maxTokens = 1000) {
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
        // Загрузите только нужные скиллы
        $moodleSkills = file_get_contents('skills-library/development/moodle-developer/SKILL.md');
        $phpSkills = file_get_contents('skills-library/development/php-developer/SKILL.md');
        
        $fullPrompt = $moodleSkills . "\n" . $phpSkills . "\n\n" . $prompt;
        
        return $this->generate($fullPrompt);
    }
}

// Используйте
$assistant = new OllamaSkillAssistant();

// Генерируйте код DevOps
$devopsCode = $assistant->generate('Создай Docker Compose для приложения с nginx, php-fpm и postgresql');
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
Brainstorming (основной)
├─→ Problem Decomposer (основной)
├─→ Research Synthesizer (основной)
├─→ Communication Adapter (основной)
│
├─→ Архитектор ПО (Software Architect, основной)
│   └─→ Web Developer
│       ├─→ DevOps Engineer ⭐
│       └─→ Moodle Developer ⭐⭐
│
├─→ PHP Developer (основной)
│   └─→ Moodle Developer ⭐⭐ (требует также MariaDB Administrator)
│
├─→ Database Developer (основной)
│   └─→ MariaDB Administrator ⭐
│       └─→ Moodle Developer ⭐⭐
│
├─→ Специалист по искусственному интеллекту (Artificial Intelligence Specialist, основной)
│   ├─→ AI Product Manager ⭐
│   └─→ AI Prompt Engineer ⭐
│
├─→ Специалист по технической документации (Technical Documentation Specialist, основной)
├─→ Scientific Writing Editor (основной)
│   ├─→ Academic Manuscript Editor ⭐
│   └─→ Research Writing Assistant ⭐
├─→ Education (основной)
│   ├─→ Learning Path Designer (основной)
│   │   └─→ Curriculum Developer ⭐
│   │       ├─→ Assessment Writer ⭐
│   │       │   └─→ Rubric Designer ⭐
│   │       └─→ Quiz Developer ⭐
│   └─→ Educational Content Reviewer (основной)
│       └─→ Course Localization Specialist ⭐
├─→ C++ Developer (основной)
├─→ Frontend Designer (основной)
│   ├─→ Bootstrap Designer ⭐
│   ├─→ Tailwind Designer ⭐
│   └─→ Skeleton Designer ⭐
├─→ Web Developer (основной)
│   ├─→ DevOps Engineer ⭐
│   └─→ Moodle Developer ⭐⭐
├─→ Test Scenario Writer (основной)
└─→ Test Writer (основной)
```

**Легенда:**

- ⭐ — специализированный скилл (расширение базового)
- ⭐⭐ — комплексный скилл (комбинирование нескольких)

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

- **Для VS Code Copilot**: VS Code с Copilot расширением и правильная конфигурация путей в `.vscode/settings.json`
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
4. Обновите этот README

## Лучшие практики

- Каждый навык должен быть узкоспециализированным
- Четко определите область применения
- Предоставьте пошаговые инструкции
- Документируйте используемые инструменты и технологии
- Регулярно обновляйте навыки по мере развития технологий

---

**Версия**: 1.5  
**Дата создания**: 2026  
**Автор**: Mihail Croitor + GitHub Copilot
