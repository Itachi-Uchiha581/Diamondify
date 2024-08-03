# 💎 Diamondify: Make Your Code Shine! ✨

Ever wrote code so trash it burnt your eyes? 🔥👀 Fear not! Diamondify is here to rescue your retinas and make your code efficient and well-commented!

## 🚀 Quick Start

Before you embark on your Diamondifying Journey, you'll need to set up your secret weapon: the OpenAI API key!

### 🔑 Setting Up Your API Key

Choose your operating system and follow the instructions:

<details>
<summary>💻 Windows</summary>

1. Open the Start menu and search for "Environment Variables"
2. Click on "Edit the system environment variables"
3. Click the "Environment Variables" button
4. Under "System variables", click "New"
5. Set the variable name as `OPENAI_API_KEY`
6. Set the variable value as your OpenAI API key
7. Click "OK" to save

Alternatively, you can use the command prompt:
```bash 
setx OPENAI_API_KEY "your-api-key-here"
```
Remember to restart your command prompt after setting the variable!
</details>

<details>
<summary>🍎 macOS and Linux</summary>

1. Open Terminal
2. Edit your shell configuration file (e.g., `~/.bash_profile`, `~/.zshrc`)
3. Add the following line:
    ```bash
   export OPENAI_API_KEY="your-api-key-here"```
4. Save the file and run: 
    ```bash 
    source ~/.bash_profile
   ```
or ( if you are using Zsh)
```bash
source ~/.zshrc
```
</details>

## 🌟 Usage

Now that you're all set up, let's make some code efficient!

```shell
python diamondify.py [-h] (-f FILE | -d DIRECTORY) [-o OUTPUT] -m MODEL
```

### 🎛️ Options:

- `-h`, `--help`: Show the help message and exit
- `-f FILE`, `--file FILE`: Input file to process
- `-d DIRECTORY`, `--directory DIRECTORY`: Input directory to process
- `-o OUTPUT`, `--output OUTPUT`: Output directory (default: ./output)
- `-m MODEL`, `--model MODEL`: Model to use for processing (default: gpt-4o)

### 💡 Examples:

Clean, and improve the code of a single file ( btw supports any programming language):
```shell
python main.py -f ugly_code.py -m gpt-4o
```
Improve the code of a whole directory:
```shell
python main.py -d messy_project -o shiny_project -m gpt-4o
```
_Note - By default all the code will be saved in a new directory called as output inside the working directory of the terminal_
## 🚀 Watch the Magic Happen!

Sit back and witness Diamondify transform your code from cluttered to clean and efficient! 🧹✨

Diamondify doesn't just make your code prettier - it enhances its efficiency and readability by:

- Optimizing algorithms and data structures 🧠
- Adding clear, concise comments to functions and code blocks 📝
- Improving variable naming for better comprehension 🏷️
- Refactoring complex logic into more manageable chunks 🧩
- Suggesting best practices and design patterns where applicable 🌟

Remember, with great power comes great responsibility. Use Diamondify to learn and improve your coding skills, not just as a quick fix! 🎓

## 🤔 Questions? Issues?

If you encounter any problems or have questions about the improvements Diamondify suggests, feel free to open an issue. We're here to help you understand and elevate your code! 📈

Now go forth and enhance your code with Diamondify! 💎🚀
