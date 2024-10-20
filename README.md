🤖 TaskMaster Discord Bot
A feature-rich Discord bot for task management and reminders with built-in multi-language support (English & Arabic) and smart activity suggestions.
✨ Features

📅 Task Management: Add, view, and remove tasks with timestamps
🌍 Multi-language Support: Switch between English and Arabic
🎯 Smart Activity Suggestions: Get contextual tips based on task type
⏰ Automated Reminders: Receive notifications when tasks are due
💪 Activity-Specific Tips: Specialized suggestions for gym, study, gaming, and work tasks
🎨 Beautiful Formatted Messages: Clean and aesthetic task displays

🛠️ Installation

Clone this repository

bashCopygit clone https://github.com/yourusername/taskmaster-discord-bot.git
cd taskmaster-discord-bot

Install required dependencies

bashCopypip install -r requirements.txt

Create a Discord bot and get your token:

Go to Discord Developer Portal
Create a New Application
Go to the Bot section
Create a bot and copy the token


Configure the bot:

Open bot.py
Replace bot.run('') with your bot token: bot.run('your-token-here')



📋 Requirements
Copydiscord.py>=2.0.0
python-dateutil>=2.8.2
💻 Commands

!setlang [en/ar] - Set your preferred language
!addtask [HH:MM] [task] - Add a new task
!viewtasks - View all your tasks
!removetask [number] - Remove a task by number
!help - Show help message

🌟 Smart Features
Activity Categories
The bot automatically categorizes tasks and provides relevant suggestions for:

🏋️‍♂️ Gym/Workout sessions
📚 Study sessions
🎮 Gaming sessions
💼 Work tasks

Intelligent Reminders

Contextual suggestions based on task type
Motivational messages in your preferred language
Clean, formatted reminder messages

📁 Project Structure
Copytaskmaster-discord-bot/
│
├── bot.py                 # Main bot file
├── create_lang_files.py   # Language file generator
├── lang_en.json          # English language strings
├── lang_ar.json          # Arabic language strings
├── requirements.txt      # Project dependencies
└── README.md            # Documentation
🚀 Getting Started

Install the bot in your server using:
Copyhttps://discord.com/api/oauth2/authorize?client_id=YOUR_CLIENT_ID&permissions=8&scope=bot
(Replace YOUR_CLIENT_ID with your bot's client ID)
Set your preferred language:
Copy!setlang en  # For English
!setlang ar  # For Arabic

Start adding tasks:
Copy!addtask 14:30 Study for math exam
!addtask 17:00 Gym workout


🤝 Contributing
Contributions are welcome! Feel free to:

Fork the repository
Create a feature branch (git checkout -b feature/AmazingFeature)
Commit your changes (git commit -m 'Add some AmazingFeature')
Push to the branch (git push origin feature/AmazingFeature)
Open a Pull Request

📝 License
This project is licensed under the MIT License - see the LICENSE file for details.
