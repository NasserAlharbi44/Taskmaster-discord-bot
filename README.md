*🤖 TaskMaster Discord Bot*
-
A feature-rich Discord bot for task management and reminders with built-in multi-language support (English & Arabic) and smart activity suggestions.

*✨ Features*
-
📅 Task Management: Add, view, and remove tasks with timestamps

🌍 Multi-language Support: Switch between English and Arabic

🎯 Smart Activity Suggestions: Get contextual tips based on task type

⏰ Automated Reminders: Receive notifications when tasks are due

💪 Activity-Specific Tips: Specialized suggestions for gym, study, gaming, and work tasks

🎨 Beautiful Formatted Messages: Clean and aesthetic task displays

*🛠️ Installation*
-
 Clone this repository

`git clone https://github.com/yourusername/taskmaster-discord-bot.git`

`cd taskmaster-discord-bot`

Install required dependencies

`pip install -r requirements.txt`

*Create a Discord bot and get your token:*
-

1- Go to the Discord Developer Portal

2- Create a New Application

3- Go to the Bot section

4- Create a bot and copy the token

Configure the bot

1- Open bot.py

2- Replace bot.run('') with your bot token: bot.run('your-token-here')

*📋 Requirements*
-
`discord.py>=2.0.0`

`python-dateutil>=2.8.2`

`pip install discord.py`

`pip install pytz`

*💻 Commands*
-
!setlang [en/ar] - Set your preferred language

!addtask [HH:MM] [task] - Add a new task

!viewtasks - View all your tasks

!removetask [number] - Remove a task by number

!help - Show help message

*🌟 Smart Features*
-
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

*📁 Project Structure*
-
taskmaster-discord-bot

bot.py >>>                  # Main bot file

create_lang_files.py >>>   # Language file generator

lang_en.json >>>          # English language strings

lang_ar.json >>>         # Arabic language strings

requirements.txt >>>      # Project dependencies
 
README.md >>>            # Documentation

*🤝 Contributing*
-
Contributions are welcome! Feel free to:

1- Fork the repository

2- Create a feature branch (git checkout -b feature/AmazingFeature)

3- Commit your changes (git commit -m 'Add some AmazingFeature')

4- Push to the branch (git push origin feature/AmazingFeature)

5- Open a Pull Request

*📝 License*
-
This project is licensed under the MIT License - see the LICENSE file for details.












