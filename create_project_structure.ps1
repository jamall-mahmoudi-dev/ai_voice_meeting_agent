# main path project
$base = "C:\path\to\voice_ai_meeting_agent"

# create folders
$folders = @(
    "$base\backend\agents",
    "$base\backend\meetings",
    "$base\docker"
)
foreach ($f in $folders) { New-Item -ItemType Directory -Path $f -Force }

# create files
$files = @(
    "$base\backend\main.py",
    "$base\backend\agents\stt_agent.py",
    "$base\backend\agents\llm_agent.py",
    "$base\backend\agents\tts_agent.py",
    "$base\backend\agents\workflow.py",
    "$base\backend\meetings\mock_meeting.py",
    "$base\backend\config.py",
    "$base\docker\Dockerfile",
    "$base\docker\docker-compose.yml",
    "$base\requirements.txt",
    "$base\README.md"
)

foreach ($file in $files) { New-Item -ItemType File -Path $file -Force }

Write-Host "alll file and folders created "
