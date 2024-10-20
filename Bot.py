import discord
from discord.ext import commands, tasks
import datetime
import json
import asyncio
from datetime import datetime, timedelta
import os
import random

# Print current working directory
print("Current working directory:", os.getcwd())
print("Files in current directory:", os.listdir())

# Bot configuration
intents = discord.Intents.default()
intents.message_content = True
intents.dm_messages = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Remove default help command - ADD THIS LINE HERE
bot.remove_command('help')

# Data structure to store tasks
tasks_data = {}

# Load language files with better error handling
def load_language_files():
    try:
        print("Attempting to load language files...")
        
        en_file_path = os.path.join(os.getcwd(), 'lang_en.json')
        ar_file_path = os.path.join(os.getcwd(), 'lang_ar.json')
        
        print(f"Looking for English file at: {en_file_path}")
        print(f"Looking for Arabic file at: {ar_file_path}")
        
        print(f"English file exists: {os.path.exists(en_file_path)}")
        print(f"Arabic file exists: {os.path.exists(ar_file_path)}")
        
        with open('lang_en.json', 'r', encoding='utf-8') as f:
            en_lang = json.load(f)
            print("Successfully loaded English language file")
            
        with open('lang_ar.json', 'r', encoding='utf-8') as f:
            ar_lang = json.load(f)
            print("Successfully loaded Arabic language file")
            
        return {"en": en_lang, "ar": ar_lang}
    except FileNotFoundError as e:
        print(f"Error loading files: {e}")
        print("Make sure these files exist in the same folder as your bot:")
        print("1. lang_en.json")
        print("2. lang_ar.json")
        exit(1)
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
        print("Please check if the language files contain valid JSON")
        exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        exit(1)

# Load languages with debug information
languages = load_language_files()

# User language preferences
user_languages = {}

# Suggestaions database
activity_suggestions = {
    "gym": {
        "en": [
            "🏋️‍♂️ Pro Tip: Start with dynamic stretches to prevent injury",
            "💪 Remember to follow your workout split plan",
            "🎯 Focus on proper form rather than heavy weights today",
            "⏰ Ideal workout duration: 45-60 minutes for optimal results",
            "🔄 Don't forget your post-workout protein intake",
            "📊 Track your sets and reps to monitor progress",
            "🌊 Stay hydrated - aim for 500ml water during workout"
        ],
        "ar": [
            "🏋️‍♂️ نصيحة احترافية: ابدأ بتمارين الإحماء الديناميكية لمنع الإصابة",
            "💪 تذكر اتباع خطة التمرين الخاصة بك",
            "🎯 ركز على الشكل الصحيح بدلاً من الأوزان الثقيلة اليوم",
            "⏰ المدة المثالية للتمرين: 45-60 دقيقة للحصول على أفضل النتائج",
            "🔄 لا تنس تناول البروتين بعد التمرين",
            "📊 تتبع مجموعاتك وتكراراتك لمراقبة التقدم",
            "🌊 حافظ على رطوبتك - اشرب 500 مل من الماء خلال التمرين"
        ]
    },
    "study": {
        "en": [
            "📚 Pro Tip: Use the Pomodoro Technique (25 min study, 5 min break)",
            "🎯 Set specific goals for this study session",
            "🧠 Try active recall instead of passive reading",
            "📝 Take brief notes to enhance retention",
            "🎵 Consider low-fi music for better focus",
            "💡 Review previous material before starting new topics",
            "🌟 Take regular breaks to maintain concentration"
        ],
        "ar": [
            "📚 نصيحة احترافية: استخدم تقنية بومودورو (25 دقيقة دراسة، 5 دقائق راحة)",
            "🎯 حدد أهدافًا محددة لجلسة الدراسة هذه",
            "🧠 جرب الاسترجاع النشط بدلاً من القراءة السلبية",
            "📝 دون ملاحظات موجزة لتعزيز الحفظ",
            "🎵 فكر في الاستماع إلى موسيقى هادئة للتركيز بشكل أفضل",
            "💡 راجع المواد السابقة قبل بدء مواضيع جديدة",
            "🌟 خذ فترات راحة منتظمة للحفاظ على التركيز"
        ]
    },
    "gaming": {
        "en": [
            "🎮 Remember to maintain good posture while gaming",
            "👀 Use the 20-20-20 rule: Every 20 mins, look 20 feet away for 20 seconds",
            "🔋 Take a 5-minute break every hour to stretch",
            "🎯 Set achievable goals for your gaming session",
            "🌟 Don't forget to stay hydrated while playing",
            "💪 Do some quick hand and wrist exercises between matches",
            "🎧 Check your audio settings for optimal game awareness"
        ],
        "ar": [
            "🎮 تذكر الحفاظ على وضعية جيدة أثناء اللعب",
            "👀 استخدم قاعدة 20-20-20: كل 20 دقيقة، انظر بعيدًا 20 قدمًا لمدة 20 ثانية",
            "🔋 خذ استراحة 5 دقائق كل ساعة للتمدد",
            "🎯 ضع أهدافًا قابلة للتحقيق لجلسة اللعب",
            "🌟 لا تنس شرب الماء أثناء اللعب",
            "💪 قم ببعض تمارين اليد والمعصم السريعة بين المباريات",
            "🎧 تحقق من إعدادات الصوت للحصول على أفضل وعي باللعبة"
        ]
    },
    "work": {
        "en": [
            "💼 Pro Tip: Start with your most important task",
            "📊 Break large tasks into smaller, manageable chunks",
            "🎯 Use the 2-minute rule for small tasks",
            "⏰ Take short breaks to maintain productivity",
            "📱 Consider minimizing digital distractions",
            "🗂️ Organize your workspace before starting",
            "✨ Set clear goals for your work session"
        ],
        "ar": [
            "💼 نصيحة احترافية: ابدأ بأهم مهمة لديك",
            "📊 قسم المهام الكبيرة إلى أجزاء أصغر يمكن إدارتها",
            "🎯 استخدم قاعدة الدقيقتين للمهام الصغيرة",
            "⏰ خذ فترات راحة قصيرة للحفاظ على الإنتاجية",
            "📱 فكر في تقليل المشتتات الرقمية",
            "🗂️ نظم مساحة عملك قبل البدء",
            "✨ ضع أهدافًا واضحة لجلسة العمل"
        ]
    }
}

def get_task_type(task_description):
    """Determine the type of task based on keywords"""
    task_description = task_description.lower()
    keywords = {
        "gym": ["gym", "workout", "exercise", "training", "fitness"],
        "study": ["study", "homework", "exam", "research", "read", "learn"],
        "gaming": ["game", "play", "gaming", "stream", "fortnite", "minecraft", "league"],
        "work": ["work", "meeting", "project", "deadline", "presentation", "email"]
    }
    
    for task_type, words in keywords.items():
        if any(word in task_description for word in words):
            return task_type
    return None

def get_motivation_message(lang):
    """Get a random motivation message based on language"""
    motivations = {
        "en": [
            "💫 You've got this!",
            "🌟 Time to shine!",
            "🚀 Ready to achieve greatness?",
            "💪 Let's make it happen!",
            "✨ Your future self will thank you!"
        ],
        "ar": [
            "💫 أنت قادر على ذلك!",
            "🌟 حان وقت التألق!",
            "🚀 مستعد لتحقيق العظمة؟",
            "💪 هيا نحقق ذلك!",
            "✨ سيشكرك مستقبلك على هذا!"
        ]
    }
    return random.choice(motivations[lang])

def format_reminder_message(task, lang, task_type=None):
    """Create a formatted reminder message with suggestions"""
    motivation = get_motivation_message(lang)
    current_time = datetime.now().strftime("%H:%M")
    
    if lang == "en":
        message = f"```📅 TASK REMINDER\n\n"
        message += f"⏰ Time: {current_time}\n"
        message += f"📝 Task: {task['description']}\n"
        message += f"\n{motivation}```\n"
    else:
        message = f"```📅 تذكير بالمهمة\n\n"
        message += f"⏰ الوقت: {current_time}\n"
        message += f"📝 المهمة: {task['description']}\n"
        message += f"\n{motivation}```\n"
    
    # Add relevant suggestion if task type is recognized
    if task_type and task_type in activity_suggestions:
        suggestion = random.choice(activity_suggestions[task_type][lang])
        message += f"\n{suggestion}"
    
    return message


def get_lang(user_id):
    return user_languages.get(str(user_id), "en")

def get_text(key, lang, *args):
    text = languages[lang].get(key, languages["en"][key])
    return text.format(*args) if args else text

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    check_reminders.start()

@bot.command(name='setlang')
async def set_language(ctx, lang):
    if lang not in ['en', 'ar']:
        await ctx.send("Supported languages: en, ar")
        return
    
    user_languages[str(ctx.author.id)] = lang
    response = "Language set to English!" if lang == 'en' else "!تم تغيير اللغة إلى العربية"
    await ctx.send(response)

@bot.command(name='addtask')
async def add_task(ctx, time: str, *, task_description: str):
    user_id = str(ctx.author.id)
    lang = get_lang(user_id)
    
    try:
        task_time = datetime.strptime(time, "%H:%M")
        task_time = task_time.replace(year=datetime.now().year,
                                    month=datetime.now().month,
                                    day=datetime.now().day)
        
        if task_time < datetime.now():
            task_time += timedelta(days=1)
        
        if user_id not in tasks_data:
            tasks_data[user_id] = []
            
        task = {
            "description": task_description,
            "time": task_time.strftime("%H:%M"),
            "completed": False
        }
        
        tasks_data[user_id].append(task)
        
        # Send confirmation
        await ctx.send(get_text("task_added", lang, time))
        
        # Check for activity suggestions
        for activity, suggestions in activity_suggestions.items():
            if activity.lower() in task_description.lower():
                suggestion = suggestions[lang][0]
                await ctx.author.send(suggestion)
                
    except ValueError:
        await ctx.send(get_text("invalid_time", lang))

@bot.command(name='viewtasks')
async def view_tasks(ctx):
    user_id = str(ctx.author.id)
    lang = get_lang(user_id)
    
    if user_id not in tasks_data or not tasks_data[user_id]:
        await ctx.send(get_text("no_tasks", lang))
        return
        
    response = get_text("your_tasks", lang) + "\n"
    for i, task in enumerate(tasks_data[user_id], 1):
        status = "✅" if task["completed"] else "⏳"
        response += get_text("task_list_item", lang, i, status, task['time'], task['description']) + "\n"
    
    await ctx.send(response)

@bot.command(name='removetask')
async def remove_task(ctx, task_number: int):
    user_id = str(ctx.author.id)
    lang = get_lang(user_id)
    
    if user_id not in tasks_data or task_number > len(tasks_data[user_id]):
        await ctx.send(get_text("invalid_task", lang))
        return
        
    removed_task = tasks_data[user_id].pop(task_number - 1)
    await ctx.send(get_text("task_removed", lang, removed_task['description']))

@tasks.loop(minutes=1)
async def check_reminders():
    current_time = datetime.now().strftime("%H:%M")
    
    for user_id, tasks in tasks_data.items():
        for task in tasks:
            if task["time"] == current_time and not task["completed"]:
                user = await bot.fetch_user(int(user_id))
                lang = get_lang(user_id)
                
                # Determine task type and create enhanced reminder
                task_type = get_task_type(task['description'])
                reminder_message = format_reminder_message(task, lang, task_type)
                
                await user.send(reminder_message)
                task["completed"] = True

@bot.command(name='help')
async def help_command(ctx):
    user_id = str(ctx.author.id)
    lang = get_lang(user_id)
    
    help_data = languages[lang]["help"]
    help_text = f"**{help_data['title']}**\n"
    help_text += f"{help_data['setlang']}\n"
    help_text += f"{help_data['addtask']}\n"
    help_text += f"{help_data['viewtasks']}\n"
    help_text += f"{help_data['removetask']}\n"
    help_text += f"{help_data['help']}"
    
    await ctx.send(help_text)

# bot token
bot.run('BOT TOKEN')
